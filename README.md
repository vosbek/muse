# AI Skills Playbook

One place for everything saved — so the AI keeps the best of all of it.

This repo implements the 3-step system from [@stilesai's reel](https://www.instagram.com/reel/Dd9DCEZh3In/):

1. **Collect** — Put every saved reel, guide, and freebie in one place, organized by topic. That's what the nine folders below are: 39 tech/AI reels plus 92 X bookmarks (Aug–Sep 2026), each distilled into what it actually teaches.
2. **Compare** — When multiple creators teach the same skill, compare them and keep only what actually works. Duplicates get merged; the collection holds exactly one best version of each skill.
3. **Stack** — Combine the refined skills into reusable project setups, so every new project starts with the AI already knowing the playbook. Finished setups live in `setups/`.

## The collection

| # | Category | Reels | X posts | What it covers |
|---|----------|-------|---------|----------------|
| 01 | [claude-code-agents](01-claude-code-agents/) | 8 | 18 | Claude Code skills, subagents, guides, dynamic workflows |
| 02 | [jev-context-economics](02-jev-context-economics/) | 3 | 33 | Jev decision models, MCP tool selection, retrieval economics, SLMs |
| 03 | [agent-memory](03-agent-memory/) | 5 | 13 | Memory systems, continual learning, agentic coding graphs, harness failure modes |
| 04 | [automation](04-automation/) | 5 | 1 | Power Automate, browser automation, Gmail agent builder, NotebookLM, Obsidian-for-agents |
| 05 | [prompts-evals](05-prompts-evals/) | 1 | 0 | Prompt testing methodology |
| 06 | [design-vibe-coding](06-design-vibe-coding/) | 7 | 4 | Design skills, animation libraries, landing-page agent teams, vibe-coding practice |
| 07 | [ai-news](07-ai-news/) | 2 | 11 | Model takes and predictions (Opus, Gemini, Qwen) |
| 08 | [tools-apis](08-tools-apis/) | 5 | 5 | Voice AI apps, agentic browsers, local agents, free APIs, HF Spaces |
| 09 | [learn](09-learn/) | 3 | 7 | Fundamentals, project ideas, free tutorials |

Start with [COMBINED.md](COMBINED.md) — the cross-cutting patterns across all 131 items (39 reels + 92 X posts), plus what's highest-leverage for a tokenomics + context-management remit.

## How to use it

**Adding a skill (Step 1):** copy `templates/skill-card.md`, fill it in, file it under the right topic. One skill per file, always with a source link back to the reel.

**Deduplicating (Step 2):** two creators teaching the same thing? Use `templates/skill-compare.md` to note what each gets right, keep the winner, merge anything worth salvaging, drop the rest.

**Starting a project (Step 3):** copy `templates/project-setup.md` into `setups/`, pick the skills the project needs, paste the playbook into your AI tool. The AI starts with the playbook, not a blank slate.

## Maintenance

- New save → skill card, filed by topic. Two minutes.
- Same skill twice → compare, keep the best, drop the rest.
- New project → stack a setup from proven skills.

The collection compounds. That's the whole point.
