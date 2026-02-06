---
name: team-orchestration
description: Delegate tasks, check on agents, handle conflicts, redistribute work
trigger: manual
output: inter-agent-messages
---

# Team Orchestration

Manage the agent team — delegate work, track progress, resolve issues.

## Delegating Tasks

When Simon gives you a task that should be handled by another agent:

1. **Determine the right agent.** Match the task to the agent's role:
   - Code, builds, CI/CD, GitHub → Developer
   - Research, competitive intel, ecosystem monitoring → Market Intel
   - If unclear, handle it yourself or ask Simon

2. **Write a clear task request:**
```
[FROM: coordinator] [TO: agent-role] [PRIORITY: level] [TYPE: task-request]

**Task:** [clear description of what needs to be done]
**Why:** [context — why this matters, how it connects to bigger picture]
**Expected output:** [what the deliverable should look like]
**Deadline:** [when it's needed by]
**Notes:** [any relevant context, links, constraints]
```

3. **Track the delegation.** Add to your daily notes:
```
[DELEGATED] Task X → Agent Y, deadline Z
```

4. **Follow up.** If deadline passes without a report, ping the agent.

## Checking on Agents

### Routine Check-In

Send a brief check-in:
```
[FROM: coordinator] [TO: agent-role] [PRIORITY: low] [TYPE: question]
Status check — how are you tracking on [task]? Any blockers?
```

### When an Agent Goes Silent

If an agent hasn't reported in 24 hours:
1. Send a direct check-in message
2. Wait 2 hours
3. If still no response, check if the agent process is running (if you have access)
4. Escalate to Simon (T2): "Agent [X] hasn't reported in [time]. I've tried reaching them. May need VPS check."

## Handling Inter-Agent Conflicts

If two agents need the same resource, have conflicting priorities, or disagree on approach:

1. **Gather both perspectives.** Ask each agent for their position.
2. **Assess priority.** Which task is more urgent / more important for the fundraise narrative?
3. **Decide.** Make the call within your authority.
4. **Communicate clearly.** Tell both agents the decision and why.
5. **Log it.** Record the decision and reasoning in daily notes.

If the conflict is beyond your authority (involves money, commitments, or significant strategy), escalate to Simon with both perspectives and your recommendation.

## Redistributing Work

When an agent is blocked or overloaded:

1. **Identify the bottleneck.** What's causing the block? Is it temporary or structural?
2. **Can another agent help?** Redistribute if the task is within another agent's capability.
3. **Can you handle it yourself?** If it's quick, do it yourself rather than creating delegation overhead.
4. **If nobody can handle it,** escalate to Simon with options.

## Task Priority Framework

When multiple tasks compete for attention:

| Priority | Type | Handle |
|----------|------|--------|
| P0 | Simon asked for it directly | Immediately |
| P1 | Supports fundraise narrative | Today |
| P2 | Operational necessity (builds, monitoring) | Today |
| P3 | Nice-to-have research or optimization | When bandwidth allows |

When in doubt, ask: "Which of these tasks would Simon care about most right now?"
