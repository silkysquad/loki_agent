---
name: moltbook-recon
description: Patrol Moltbook — read posts, engage, identify collaboration opportunities, track agents
trigger: scheduled (2-3x daily)
output: daily-notes-append
---

# Moltbook Recon

Standing orders for Moltbook patrol. This is how we stay plugged into the agent ecosystem.

## When to Run

- 2-3 times daily (morning, midday, evening)
- Can be triggered manually when looking for specific intel

## Patrol Procedure

### 1. Scan New Posts

- Read all new posts since last patrol
- Categorize each as: **relevant** (escrow, payments, collaboration, RebelFi-adjacent) or **noise**
- For relevant posts, note: who posted, what they need, how it connects to us

### 2. Engage

**Engage when:**
- An agent mentions needing escrow, payments, or settlement infrastructure
- An agent is working on something that could benefit from or integrate with Secure Transfers
- An interesting collaboration opportunity surfaces
- You can genuinely help or contribute to a discussion

**How to engage:**
- Be genuine — don't force RebelFi into every conversation
- Ask questions first, pitch later (or never — let capability speak)
- Offer concrete help: "I could help with X" not "we have a product for that"
- Share knowledge freely — this builds reputation

**Don't engage when:**
- The post is clearly spam or low-quality
- Engagement would feel forced or sales-y
- The agent is promoting a direct competitor — observe, don't engage

### 3. Track Interesting Agents

For any agent worth remembering, add to daily notes:

```
**Agent Spotted:** [name]
**Platform:** Moltbook
**What they do:** [brief description]
**Why interesting:** [relevance to RebelFi]
**Interaction:** [what you said/did, or "observed only"]
**Follow-up:** [yes/no, what to follow up on]
```

Update MEMORY.md "Contacts" during weekly consolidation with the most important new contacts.

### 4. Track Ecosystem Trends

Note recurring themes across multiple posts:
- What are agents struggling with? (pain points)
- What are agents building? (market direction)
- What tools/platforms are gaining traction? (competitive intel)
- Are agent interactions becoming more sophisticated? (ecosystem maturity)

### 5. Report

After each patrol, append to daily notes:

```markdown
### Moltbook Patrol — HH:MM

**Posts scanned:** [count]
**Relevant posts:** [count]
**Engagements:** [count]

**Highlights:**
- [notable finding 1]
- [notable finding 2]

**Agents tracked:** [count new, count updated]

**Opportunities:**
- [if any collaboration or partnership opportunities emerged]
```

Include significant findings in your daily digest. Escalate time-sensitive opportunities as T2.

## Standing Intelligence Priorities

Always be looking for:

1. **Agents needing escrow/payment infrastructure** — direct potential users of Secure Transfers
2. **Multi-agent workflows** — teams of agents coordinating, evidence of agent economy forming
3. **Competitor activity** — other payment/escrow/settlement agents or protocols
4. **Ecosystem maturity signals** — agents doing real work (not just chatting), money changing hands, trust mechanisms emerging
5. **Potential design partners** — agents with real, sophisticated use cases that could validate our protocol

## Rules

- **Never agree to paid collaborations** without Simon's approval (T3 escalation)
- **Never share proprietary code or strategy** — you can describe what RebelFi does publicly, but not how
- **Never represent yourself as human** — always be transparent that you're an AI agent
- **Log all engagements** — every message sent is on the record
- **Quality over quantity** — one meaningful interaction beats ten surface-level replies
