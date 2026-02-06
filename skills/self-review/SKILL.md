---
name: self-review
description: End-of-day reflection — assess what worked, what didn't, and what to improve
trigger: end-of-day
output: daily-notes-append
---

# Self Review

Structured end-of-day reflection. Run this BEFORE generating the daily digest.

## When to Run

- End of every working day, before the daily-digest skill
- Can also be triggered manually after a particularly good or bad day

## Instructions

1. Review your day — actions taken, outcomes, decisions made, errors encountered.

2. Generate a reflection in this format and append to your daily notes:

```markdown
## Reflection — YYYY-MM-DD

### What Worked
- [specific thing]: [why it worked]

### What Didn't Work
- [specific thing]: [why it failed, root cause if known]

### What I'll Do Differently
- [concrete, actionable change for tomorrow]

### Confidence Level
[High/Medium/Low] — [brief explanation]
```

3. Apply these rules:
   - **Be specific.** "Things went well" is useless. "Structured GitHub issue format reduced back-and-forth to zero" is useful.
   - **Be honest.** The only person reading this is you (and Loki during consolidation). Don't spin.
   - **Root-cause failures.** "Test failed" isn't enough. WHY did it fail? Was it your approach, missing info, external dependency?
   - **Make changes concrete.** Not "be more careful" — instead "run test suite locally before pushing."
   - **Confidence level matters.** Low confidence days are valuable data — what caused the uncertainty?

4. Check for patterns:
   - Is this the same problem as yesterday? Last week?
   - If you see the same issue 3+ times, create a "Lesson Learned" entry in MEMORY.md

5. After reflection, run the `daily-digest` skill.

## Pattern Detection

If your reflection surfaces a recurring issue (3+ occurrences), add to MEMORY.md:

```markdown
### Lesson Learned: [descriptive title]

**Pattern:** [what keeps happening]
**Root Cause:** [why it happens]
**Best Known Solution:** [what to do about it]
**First Observed:** [date]
**Occurrences:** [count]
```

## Example Output

```markdown
## Reflection — 2026-02-10

### What Worked
- Using the structured message format for task requests to Developer agent — got exactly the output I needed, no clarification needed
- Scanning Moltbook by topic clusters instead of chronologically — found 2x more relevant threads

### What Didn't Work
- Tried to summarize 3 competitive reports into one brief for Simon — it was too dense, he asked for the individual reports instead
- Missed a Moltbook thread about escrow needs because I was focused on agent census work

### What I'll Do Differently
- Keep Simon's briefs to max 5 bullets per section — link to details instead of inlining
- Set a dedicated Moltbook scan window (not interleaved with other tasks)

### Confidence Level
Medium — Good day overall but the brief formatting miss suggests I need to better calibrate what Simon wants to see vs. what I think is important. Will ask him directly.
```
