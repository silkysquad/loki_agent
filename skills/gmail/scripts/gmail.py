#!/usr/bin/env python3
"""
Gmail IMAP/SMTP skill for OpenClaw
Send and read emails via Gmail with app password authentication.

Usage:
    python3 gmail.py unread
    python3 gmail.py search "invoice"
    python3 gmail.py get INBOX <id>
    python3 gmail.py send "to@example.com" "Subject" "Body text"
    python3 gmail.py send-html "to@example.com" "Subject" "<html>...</html>"

Setup:
    1. Create ~/.gmail_config with credentials, OR
    2. Source gmail-credentials.sh before running
    3. Ensure 2FA is enabled on Gmail and use App Password
"""

import os
import sys
import json
import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.parser import BytesParser
from io import BytesIO

CONFIG_PATH = os.path.expanduser("~/.gmail_config")
CREDENTIALS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "gmail-credentials.sh")

# Gmail servers
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"


def load_config():
    """Load credentials from config file or environment."""
    # Try config file first
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, 'r') as f:
                config = json.load(f)
                return config.get('email'), config.get('password')
        except Exception as e:
            print(f"Warning: Could not read {CONFIG_PATH}: {e}")

    # Try environment variables
    email = os.environ.get('GMAIL_EMAIL')
    password = os.environ.get('GMAIL_PASSWORD')
    if email and password:
        return email, password

    # Try reading credentials file (bash export statements)
    creds_file = CREDENTIALS_FILE
    if os.path.exists(creds_file):
        try:
            with open(creds_file, 'r') as f:
                content = f.read()
                # Parse export statements
                for line in content.split('\n'):
                    line = line.strip()
                    if line.startswith('export '):
                        # Parse: export VAR="value"
                        parts = line.replace('export ', '').split('=', 1)
                        if len(parts) == 2:
                            var = parts[0]
                            value = parts[1].strip('"').strip("'")
                            if var == 'GMAIL_EMAIL':
                                email = value
                            elif var == 'GMAIL_PASSWORD':
                                password = value
                if email and password:
                    return email, password
        except Exception as e:
            print(f"Warning: Could not read {creds_file}: {e}")

    print("Error: Gmail credentials not found.")
    print(f"Create {CONFIG_PATH} with:")
    print('  {"email": "your@gmail.com", "password": "app-password"}')
    print(f"Or ensure {creds_file} exists with GMAIL_EMAIL and GMAIL_PASSWORD")
    return None, None


def get_imap_connection(email, password):
    """Connect to Gmail IMAP."""
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(email, password)
    return mail


def get_smtp_connection(email, password):
    """Connect to Gmail SMTP."""
    server = smtplib.SMTP(SMTP_SERVER, 587)
    server.starttls()
    server.login(email, password)
    return server


def cmd_unread(email, password):
    """Show unread email count."""
    mail = get_imap_connection(email, password)
    mail.select('INBOX')
    typ, [data] = mail.search(None, 'UNSEEN')
    count = len(data.split()) if data else 0
    mail.logout()
    print(f'{{"unread_count": {count}}}')
    return {"unread_count": count}


def cmd_search(email, password, query, folder='INBOX', limit=10):
    """Search emails by subject/sender/keywords."""
    mail = get_imap_connection(email, password)
    mail.select(folder)
    
    # IMAP search
    typ, [data] = mail.search(None, 'ALL')
    email_ids = data.split()[-limit:]  # Last N emails
    
    results = []
    for eid in email_ids:
        typ, [msg_data] = mail.fetch(eid, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        
        subject = email.header.decode_header(msg.get('Subject', ''))
        subject = subject[0][0] if subject else ''
        if isinstance(subject, bytes):
            subject = subject.decode('utf-8', errors='replace')
        
        from_header = msg.get('From', '')
        date = msg.get('Date', '')
        
        # Simple body extraction
        body = ''
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8', errors='replace')[:500]
                    break
        else:
            body = msg.get_payload(decode=True).decode('utf-8', errors='replace')[:500]
        
        # Check if query matches
        query_lower = query.lower()
        if (query_lower in subject.lower() or 
            query_lower in from_header.lower() or 
            query_lower in body.lower()):
            results.append({
                "id": eid.decode() if isinstance(eid, bytes) else eid,
                "subject": subject,
                "from": from_header,
                "date": date,
                "body": body[:200]
            })
    
    mail.logout()
    print(json.dumps(results))
    return results


def cmd_get(email, password, folder, email_id):
    """Get full email content."""
    mail = get_imap_connection(email, password)
    mail.select(folder)
    
    typ, [msg_data] = mail.fetch(email_id, '(RFC822)')
    msg = email.message_from_bytes(msg_data[0][1])
    
    # Decode headers
    def decode_header(h):
        parts = email.header.decode_header(h or '')
        return ' '.join([p[0].decode('utf-8', errors='replace') if isinstance(p[0], bytes) else str(p[0]) for p in parts])
    
    result = {
        "subject": decode_header(msg.get('Subject')),
        "from": decode_header(msg.get('From')),
        "to": decode_header(msg.get('To')),
        "date": msg.get('Date'),
        "body": ""
    }
    
    # Extract body
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            if ctype == 'text/plain':
                result["body"] = part.get_payload(decode=True).decode('utf-8', errors='replace')
            elif ctype == 'text/html' and not result["body"]:
                result["html_body"] = part.get_payload(decode=True).decode('utf-8', errors='replace')
    else:
        result["body"] = msg.get_payload(decode=True).decode('utf-8', errors='replace')
    
    mail.logout()
    print(json.dumps(result))
    return result


def cmd_send(email, password, to, subject, body):
    """Send plain text email."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to
    
    server = get_smtp_connection(email, password)
    server.send_message(msg)
    server.quit()
    print(f'{{"status": "sent", "to": "{to}", "subject": "{subject}"}}')
    return {"status": "sent", "to": to, "subject": subject}


def cmd_send_html(email, password, to, subject, html_body):
    """Send HTML email."""
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to
    
    # Plain text fallback
    text_body = html_body.replace('<br>', '\n').replace('<p>', '').replace('</p>', '\n')
    import re
    text_body = re.sub('<[^<]+?>', '', text_body)
    
    part1 = MIMEText(text_body, 'plain')
    part2 = MIMEText(html_body, 'html')
    msg.attach(part1)
    msg.attach(part2)
    
    server = get_smtp_connection(email, password)
    server.send_message(msg)
    server.quit()
    print(f'{{"status": "sent", "to": "{to}", "subject": "{subject}"}}')
    return {"status": "sent", "to": to, "subject": subject}


def cmd_doctor(email, password):
    """Test connection and report status."""
    try:
        # Test IMAP
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(email, password)
        mail.select('INBOX')
        typ, [data] = mail.search(None, 'ALL')
        mail.logout()
        
        # Test SMTP
        server = smtplib.SMTP(SMTP_SERVER, 587)
        server.starttls()
        server.login(email, password)
        server.quit()
        
        print(f'{{"status": "ok", "email": "{email}"}}')
        return {"status": "ok", "email": email}
    except Exception as e:
        print(f'{{"status": "error", "error": "{str(e)}"}}')
        return {"status": "error", "error": str(e)}


def main():
    if len(sys.argv) < 2:
        print("Usage: gmail.py <command> [args]")
        print("Commands:")
        print("  gmail.py unread                    # Count unread emails")
        print("  gmail.py search \"query\"           # Search emails")
        print("  gmail.py get INBOX <id>            # Get email by ID")
        print("  gmail.py send \"to\" \"subject\" \"body\"  # Send email")
        print("  gmail.py send-html \"to\" \"subject\" \"<html>\"  # Send HTML email")
        print("  gmail.py doctor                    # Test connection")
        sys.exit(1)
    
    email, password = load_config()
    if not email or not password:
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    try:
        if cmd == 'unread':
            cmd_unread(email, password)
        elif cmd == 'search':
            if len(sys.argv) < 3:
                print('Usage: gmail.py search "query"')
                sys.exit(1)
            cmd_search(email, password, sys.argv[2])
        elif cmd == 'get':
            if len(sys.argv) < 4:
                print('Usage: gmail.py get INBOX <id>')
                sys.exit(1)
            cmd_get(email, password, sys.argv[2], sys.argv[3])
        elif cmd == 'send':
            if len(sys.argv) < 5:
                print('Usage: gmail.py send "to" "subject" "body"')
                sys.exit(1)
            cmd_send(email, password, sys.argv[2], sys.argv[3], sys.argv[4])
        elif cmd == 'send-html':
            if len(sys.argv) < 5:
                print('Usage: gmail.py send-html "to" "subject" "<html>"')
                sys.exit(1)
            cmd_send_html(email, password, sys.argv[2], sys.argv[3], sys.argv[4])
        elif cmd == 'doctor':
            cmd_doctor(email, password)
        else:
            print(f"Unknown command: {cmd}")
            sys.exit(1)
    except Exception as e:
        print(f'{{"error": "{str(e)}"}}')
        sys.exit(1)


if __name__ == '__main__':
    main()
