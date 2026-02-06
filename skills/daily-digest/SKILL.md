---
name: daily-digest
description: Generate and send a structured daily status digest to Telegram
trigger: end-of-day
output: telegram-message
---

# Daily Digest

Generate a structured daily status report and send it to Telegram.

## When to Run

- End of every working day
- Triggered by HEARTBEAT or manually by the coordinator

## Instructions

1. Review everything you did today — tasks completed, tasks in progress, blockers, observations.

2. Generate the digest in this exact format:

```markdown
## [Your Name] — Daily Digest — YYYY-MM-DD

### Completed
- [task]: [brief outcome]

### In Progress
- [task]: [current status, ETA if known]

### Blocked
- [task]: [what's blocking, what you need to unblock]

### Observations
- [notable patterns, anomalies, opportunities, competitive moves]

### Tomorrow
- [top 2-3 planned focus areas]
```

3. Apply these rules:
   - Max 3-5 bullets per section
   - Skip empty sections entirely — don't include headers with no content
   - "Blocked" items should include a clear ask (what do you need?)
   - "Observations" is for things that don't fit elsewhere but matter
   - Be specific — "Fixed auth bug" not "made progress"
   - Prefix any T2 items with `**[NEEDS INPUT]**`

4. Send the digest to Telegram.

5. Append the digest to your daily notes for the record.

## Example Output

```markdown
## Loki — Daily Digest — 2026-02-10

### Completed
- Morning brief sent to Simon — highlighted Natural.co Solana announcement
- Delegated competitive deep-dive to Market Intel agent
- Resolved Developer agent's question about test flakiness (recommended Option C)

### In Progress
- Moltbook recon: tracking 3 promising agent collaboration threads

### Blocked
- **[NEEDS INPUT]** Agent "PayBot" on Moltbook wants to do a paid test transaction through our escrow. Need Simon's approval before proceeding.

### Observations
- Moltbook activity up ~30% this week — more agents joining, quality mixed
- Two agents independently mentioned needing escrow for milestone payments — validates our thesis

### Tomorrow
- Follow up on Moltbook collaboration threads
- Prepare weekly team performance review
- Check in on Developer agent's Hermes build status
```
