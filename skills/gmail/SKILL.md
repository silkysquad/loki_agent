---
name: gmail
description: Send and read emails via Gmail with IMAP/SMTP. Uses app password authentication. Perfect for email automation, monitoring, and notifications.
---

# Gmail Skill

Send and read emails via Gmail using IMAP/SMTP with app password authentication.

## Quick Start

```bash
# Test connection
python3 scripts/gmail.py doctor

# Check unread count
python3 scripts/gmail.py unread

# Search emails
python3 scripts/gmail.py search "invoice"

# Get specific email
python3 scripts/gmail.py get INBOX 1234

# Send email
python3 scripts/gmail.py send "recipient@example.com" "Subject" "Body text"

# Send HTML email
python3 scripts/gmail.py send-html "to@example.com" "Subject" "<h1>Hello!</h1>"
```

## Setup

**Credentials are stored in:** `skills/gmail/gmail-credentials.sh`

The app password has been configured. To use manually:

```bash
# Source credentials (run from skill directory)
source scripts/gmail-credentials.sh

# Or create ~/.gmail_config manually:
echo '{"email": "pettibone@gmail.com", "password": "your-app-password"}' > ~/.gmail_config
```

## Commands

| Command | Description |
|---------|-------------|
| `unread` | Count unread emails in INBOX |
| `search "query"` | Search emails by subject/sender/content |
| `get FOLDER ID` | Get full email content |
| `send "to" "subject" "body"` | Send plain text email |
| `send-html "to" "subject" "<html>"` | Send HTML email |
| `doctor` | Test IMAP/SMTP connection |

## Examples

### Morning Briefing
```bash
# Check unread
python3 scripts/gmail.py unread
# Output: {"unread_count": 5}
```

### Search for Recent Emails
```bash
python3 scripts/gmail.py search "RebelFi"
# Returns matching emails as JSON
```

### Send Notification
```bash
python3 scripts/gmail.py send "simon@example.com" "Handshake Deployed" "The escrow contract is live!"
```

## Requirements

- Python 3.x (no external dependencies - uses stdlib)
- Gmail account with 2FA enabled
- App Password (already configured)

## Troubleshooting

**"Authentication failed"**: Check that app password is correct and 2FA is enabled on the Gmail account.

**"Connection timeout":** Check network/firewall allows IMAP (993) and SMTP (587).

**Credentials not found:** Run `source skills/gmail/gmail-credentials.sh` or ensure `~/.gmail_config` exists.
