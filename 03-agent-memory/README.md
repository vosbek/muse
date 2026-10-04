# 03 — Agent Memory

**Thesis:** A model without memory re-pays the same context tax every session. These five reels converge on one conclusion from different angles: memory must be an explicit, engineered subsystem — hierarchical stores, background consolidation, lesson files, cross-harness transcripts — not something you hope the context window handles. And the fourth reel adds the crucial warning: when agents fail, suspect the harness (the layer between model and files) before you suspect the model.

### A real agentic coding graph: Project Four
- **Creator:** @agentic.james · **Date:** 2026-08-15
- **What it suggests:** A from-scratch build of "cross-harness-memory": a tool that centralizes transcripts across Codex, Claude Code, and OpenCode into one searchable store other agents can query. The architecture: a local database, harness adapters that parse each tool's transcripts, and an agent plugin for access. The build process itself is the lesson — a Coordinator thread defines requirements and goal contracts, then spawns worker threads with their own slash-goal prompts to figure out how many threads are needed and what each contract should be; threads converge into a centralized deployed-runtime evaluation that verifies the code in production by running headless Claude Code, Codex, and OpenCode CLIs; a final thread checks scalability and edge cases before independent review and push to a private GitHub repo. It ran mostly autonomously while he did other work. Two takeaways: memory should be harness-agnostic (transcripts from every tool, one store), and verification should be runtime-based (does it work headless in production?), not review-based.
- **Repos/tools:** Private GitHub repo (planned community release); Codex, Claude Code, OpenCode CLIs
- **Extractable skill:** Cross-harness memory — centralize transcripts from every agent tool into one searchable local store; verify agent-built systems with headless production runs.
- **Source:** https://www.instagram.com/reel/DcFJ_VBjfRK/

### Long-term memory in three skills: /memory, /recall, /rem sleep
- **Creator:** @agentic.james · **Date:** 2026-01-22
- **What it suggests:** A clean three-part decomposition of agent memory. The Memory skill stores information in a hierarchical folder structure (hierarchy matters — flat dumps become unsearchable). The REM Sleep skill is a background process that records conversation transcripts into the Memory store without interrupting the main agent. The Recall skill is another background process that retrieves relevant memories for the current task. The architecture mirrors the Jev pattern: capture and retrieval happen outside the main context, in background processes, and only relevant memories surface into the working session. The naming is doing conceptual work too — memory isn't one feature, it's three (store, consolidate, retrieve), and conflating them is why naive "remember this" implementations fail.
- **Repos/tools:** Claude Code (skills)
- **Extractable skill:** Memory as three subsystems — hierarchical storage, background consolidation, background retrieval; never let bookkeeping touch the main thread.
- **Source:** https://www.instagram.com/reel/DT1UnU_DdMR/

### Continual learning with a nested memory tree
- **Creator:** @agentic.james · **Date:** 2026-01-06
- **What it suggests:** Taking the memory idea further: persistent memory plus continual learning, built on a nested tree structure for organizing information specifically to prevent context bloat. The key mechanism is background subagents that manage the memory tree — pruning, reorganizing, consolidating — without interfering with the main agent's context. This solves the scaling problem that kills simpler memory systems: a lessons file or folder store works for weeks, then grows into its own context hog. A tree with active gardeners stays useful. The system was still in development at recording time, but the design principle stands alone: memory needs maintenance labor, and that labor should be agent-driven and off the main thread.
- **Repos/tools:** Claude Code (subagents; system in development)
- **Extractable skill:** Gardened memory — use a nested structure plus background subagents for pruning/consolidation, so memory stays an asset instead of becoming bloat.
- **Source:** https://www.instagram.com/reel/DTMMKKZjYJQ/

### The harness is the hidden layer (why coding agents really fail)
- **Creator:** @brooke.bytes · **Date:** 2026-07-23
- **What it suggests:** A summary of an Amazon research paper (arXiv 2606.17454) with the most important technical claim in this collection: between the model and your files sits the harness — the layer translating model intent into edits and reporting results back — and most coding-agent failures live there, in the intent-execution gap. The canonical failure: the model asks for a one-line change, the harness misapplies it (replacing text in three classes, or matching a short fragment inside longer lines), and the model blames itself and spirals. The fixes, built into the open-source Strands Agents harness (SSA), are all harness-level: expand context until matches are unique, require whole-line matches, show a feedback diff after every edit so the model can verify, and reject bad edits upfront. SSA matched or beat vendor-published scores across 21 models (Claude, GPT, Gemini, Grok, Qwen) on Terminal Bench 2 — model-agnostic, and improvements compound across every model you plug in. The strategic read: when agents fail, audit the edit/verify loop before upgrading the model.
- **Repos/tools:** Strands Agents SDK (AWS, open source on GitHub); paper arXiv 2606.17454
- **Extractable skill:** Harness-first debugging — verify unique matches, whole-line edits, post-edit diffs, and upfront rejection before blaming model quality.
- **Source:** https://www.instagram.com/reel/DbJRhHIRzlc/

### A self-improving agent via lessons.md
- **Creator:** @keshavsuki · **Date:** 2026-03-14
- **What it suggests:** The simplest continual-learning loop in the collection, in three steps: after any correction, append the lesson to a `tasks/lessons.md` file; read that file at the start of every session; apply the relevant rule before touching any code. Done consistently for a month, the agent adapts to your patterns and preferences. It's deliberately low-tech — no vector DB, no framework — which is the point: the failure mode of memory systems is usually adoption friction, not sophistication. A markdown file you'll actually maintain beats an architecture you won't. This is the minimum viable version of everything the fancier memory reels describe, and it's the right starting point before graduating to hierarchical stores or background gardeners.
- **Repos/tools:** None (markdown file + discipline)
- **Extractable skill:** lessons.md loop — capture corrections immediately, re-read at session start, apply before acting. Start here before building anything fancier.
- **Source:** https://www.instagram.com/reel/DV4a43ZjkMa/
