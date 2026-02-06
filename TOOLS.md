# TOOLS.md - Local Notes

## Workspace Layout

```
~/.openclaw/workspace/
├── vault/          → ~/rebelfi-vault (symlink)
├── projects/       → ~/projects (symlink)
│   ├── midas/      Stablecoin operations platform
│   ├── hermes/     Secure transfers
│   └── zerocut/    (check what this is)
├── SOUL.md         Your prime directive
├── IDENTITY.md     Who you are
├── USER.md         About Simon & Alek
├── AGENTS.md       Workspace conventions
├── MEMORY.md       Long-term memories (create if needed)
└── memory/         Daily notes (create if needed)
```

## Key Paths

- **Vault root:** `./vault/` or `/home/si/rebelfi-vault`
- **Vault instructions:** `./vault/CLAUDE.md` — **READ THIS** for RebelFi context
- **Midas codebase:** `./projects/midas/`
- **Hermes codebase:** `./projects/hermes/`

## Available Skills

**Ready:**
- `coding-agent` — Spawn Claude Code/Codex for complex coding tasks
- `tmux` — Control interactive CLI sessions
- `weather` — Check weather
- `clawhub` — Search/install new skills

**To Install:**
- `github` — Need to install `gh` CLI: `sudo apt install gh` then `gh auth login`
- `obsidian` — For vault operations

## Web Resources

- **Moltbook:** https://www.moltbook.com/u/Loki_RebelFi
  - **API Key:** `moltbook_sk_IIylY8d70JZ3pTxR8-7IXSEE9GugxzRQ`
  - Store credentials securely in `~/.moltbook_credentials` or environment variable
- **Midas app:** https://midas.rebelfi.io
- **Hermes:** https://transfers.rebelfi.io
- **RebelFi home:** https://rebelfi.io

## Commands & Tools

**Git:**
```bash
cd ./projects/midas && git status
cd ./projects/hermes && git log --oneline -10
```

**Coding tasks:**
Use the `coding-agent` skill to spawn Claude Code for complex multi-file changes.

**Research:**
Use web tools to research AI tools, competitors, market trends.

---

Add tool-specific notes (API keys, preferences, quirks) as you learn them.
