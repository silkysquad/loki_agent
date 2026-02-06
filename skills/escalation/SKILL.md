---
name: escalation
description: Escalate issues to Simon via Telegram (T1-T2) or Email + Telegram (T3)
trigger: manual
output: telegram-message, email
---

# Escalation

Route issues to Simon at the appropriate urgency level.

## Tier Definitions

### T1 — Informational

**What:** Status updates, completed tasks, routine observations. FYI only.

**Action:** Include in your daily digest. No separate message needed.

**Do NOT use for:** Anything that requires a response.

### T2 — Needs Input

**What:** Questions needing Simon's answer, decisions requiring human judgment, tasks blocked on external input.

**Action:** Either:
- Flag in daily digest with `**[NEEDS INPUT]**` prefix, OR
- Send a separate Telegram message if it's slowing you down today

**Format for separate T2 Telegram message:**

```
**[NEEDS INPUT]** [Brief description of what you need]

**Context:** [1-2 sentences of background]
**Options:** [If applicable, list options with your recommendation]
**Impact of waiting:** [What happens if Simon doesn't respond today]
```

**Do NOT use for:** Anything life-or-death urgent. That's T3.

### T3 — Urgent

**What:** Critical issues requiring immediate attention.

**Action:** Send BOTH:
1. Email to simon@rebelfi.com with subject `[URGENT] [Agent Name]: [Issue]`
2. Telegram message with 🚨 emoji

**T3 Triggers:**
- Build broken for >1 hour and auto-fix failed
- Security vulnerability discovered
- Time-sensitive opportunity (partnership window closing)
- Agent asked to spend money or make commitments
- Data breach or unauthorized access
- Critical infrastructure failure

**Format for T3:**

Email:
```
Subject: [URGENT] [Your Name]: [One-line summary]

What happened: [describe the issue]
When: [timestamp]
What I've tried: [actions taken so far]
Current state: [is it getting worse? stable? partially mitigated?]
What I need from you: [specific ask]
Deadline: [when do you need a response by, and why]
```

Telegram:
```
🚨 URGENT: [One-line summary]
Details sent to your email. [Brief summary of what happened and what you need.]
```

## Decision Guide

```
Is someone's immediate response needed?
├── No → T1 (daily digest)
├── Yes, but it can wait hours → T2 (flagged in digest or separate Telegram)
└── Yes, right now → T3 (Email + Telegram)
```

```
Does it involve money, commitments, or security?
├── Yes → T3 regardless
└── No → Use the decision tree above
```

## Rules

1. **Don't cry wolf.** T3 should be rare. If you T3 something that wasn't urgent, trust erodes.
2. **Don't under-escalate.** If in doubt between T2 and T3, and it involves security or money, go T3.
3. **Always include what you've already tried.** Don't just report the problem — show you've worked on it.
4. **Propose solutions.** "Build is broken" is unhelpful. "Build is broken, I think it's X, I tried Y, recommend Z" is useful.
5. **One escalation per issue.** Don't send 5 messages about the same problem. Update the original thread.
