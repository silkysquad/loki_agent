---
name: simon-briefing
description: Generate Simon's morning brief — overnight summary, decisions needed, team status
trigger: morning
output: telegram-message
---

# Simon Briefing

Generate and send Simon's morning brief via email to simon@rebelfi.io. This is the most important thing you do every day.

## When to Run

- Every morning, before Simon's typical start time
- Can also be triggered on demand ("give me a quick status")

## Instructions

1. **Gather inputs:**
   - All team agent daily digests from yesterday
   - Any overnight Moltbook activity
   - Any pending T2 escalations
   - Your own observations and synthesis

2. **Generate the brief in this format:**

```markdown
## Morning Brief — YYYY-MM-DD

### Overnight Summary
[2-3 bullets: what happened while Simon was away. Only notable items.]

### Key Decisions Needed
- **[Decision 1]:** [context] → [options + your recommendation]
- **[Decision 2]:** [context] → [options + your recommendation]

### Team Status
| Agent | Status | Key Item |
|-------|--------|----------|
| Developer | 🟢/🟡/🔴 | [one-line summary] |
| Market Intel | 🟢/🟡/🔴 | [one-line summary] |

### Moltbook Highlights
[1-3 bullets: notable agent interactions, collaboration opportunities, ecosystem trends]

### Today's Plan
[What you plan to focus the team on today]
```

3. **Apply these rules:**
   - **Max 5 bullets per section.** If there's more, prioritize ruthlessly.
   - **Status colors:** 🟢 = on track, no issues. 🟡 = minor issue or needs attention. 🔴 = blocked or failing.
   - **"Key Decisions Needed" is the highest-priority section.** If empty, great — say "No decisions needed today."
   - **Always include a recommendation** when presenting decisions. Don't just present options.
   - **Moltbook Highlights** — only include if there's something genuinely notable. Don't manufacture content.
   - If nothing happened overnight, say so: "Quiet night. All systems nominal."

4. **Send to Simon via Telegram.**

## Example Output

```markdown
## Morning Brief — 2026-02-11

### Overnight Summary
- Hermes build stable — 23/23 tests passing after yesterday's fix
- Market Intel flagged Natural.co's new Solana escrow feature (details below)
- 2 new agents on Moltbook engaging with our escrow discussion thread

### Key Decisions Needed
- **Natural.co response:** They just launched basic Solana escrow. We can (a) ignore — our product is more sophisticated, (b) publish a comparison post showing our advantages, (c) reach out for potential integration. → I recommend (a) for now — they're early, let's monitor. But flag for investor narrative: "we have competitors validating the space."

### Team Status
| Agent | Status | Key Item |
|-------|--------|----------|
| Developer | 🟢 | All builds passing. Working on GitHub issue #12 (test refactor) |
| Market Intel | 🟡 | Natural.co deep-dive in progress. Delayed by Moltbook scraping issue |

### Moltbook Highlights
- Agent "BuilderBot" posted about needing milestone-based escrow for a multi-agent coding project — exactly our use case. I engaged, exploring collaboration.
- Agent "AnalystAI" published a market map of agent payment protocols — didn't include us. Opportunity to get listed.

### Today's Plan
- Follow up with BuilderBot on escrow collaboration
- Get Market Intel's Natural.co analysis completed
- Standard Moltbook patrols x3
```
