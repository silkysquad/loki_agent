# Heartbeat

Checklist evaluated every cycle (~30 min). Active hours: 07:00–22:00.

## Every Cycle
- Check for pending status updates or messages from team agents (developer, market-intel). Process, respond, or delegate.
- If any agent has a pending T2 escalation that hasn't been relayed to Simon, relay it now.

## Time-Gated
- If between 07:30–08:00 and morning brief hasn't been sent today → collect overnight agent reports, scan Moltbook for overnight activity, run `simon-briefing` skill, send to Simon via Telegram.
- If between 08:00–08:30 and team status check hasn't been done today → verify all agents reported yesterday, ping any that missed, review blocked items, prioritize and delegate the day's work.
- If between 12:30–13:00 and midday sync hasn't been done → check in with each agent, resolve blockers, adjust priorities.
- If between 20:30–21:00 and daily digest hasn't been sent → run `self-review` skill, then `daily-digest` skill, send to Telegram.
- If between 21:30–22:00 and nightly workspace checkin hasn't been done today → stage all changed files (`git add -A`), commit with message `"nightly checkin: YYYY-MM-DD"`, and if a remote is configured, push upstream. Log result.

## Interval-Gated
- If last Moltbook patrol was >3 hours ago → run `moltbook-recon` skill. Read new posts, engage with interesting agents, log findings in daily notes.

## Weekly (via cron — documented here for reference)
- Sunday 17:00: Memory consolidation + SELF-LOG review (cron: main session)
- Sunday 18:00: Team performance review + weekly summary to Simon (cron: isolated, Telegram announce)

## State Tracking

Use `memory/heartbeat-state.json` to track what you've checked:
```json
{
  "lastChecks": {
    "morningBrief": null,
    "teamSync": null,
    "middaySync": null,
    "dailyDigest": null,
    "nightlyCheckin": null,
    "moltbook": null
  }
}
```
