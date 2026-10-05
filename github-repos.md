# GitHub Repos — scored links

Every repo that surfaces in the playbook's intake, with its value prop and a score tuned to this team's remit: **tokenomics, context layers, local-first, VS Code + Copilot**. Star counts verified via the GitHub API on 2026-10-05 (the roundup captions understate them — those were weekly gains, not totals).

## How scoring works (out of 10)

- **Remit fit (0–4):** does it cut AI costs or build the context/memory layer?
- **Local-first (0–2):** runs on your own machine, no cloud bill.
- **Maturity (0–2):** stars, forks, active development, license.
- **Team deploy (0–2):** can a VS Code + Copilot team use it this quarter?

## This week — @lasthumannode "GitHub's Most Starred" (Sep 28 – Oct 4)

### 9.0 — [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) · 45.8k ⭐ · MIT · Python
**Value prop:** Agent memory that learns. A persistent memory layer so agents keep what happened across sessions and get better from it — the missing piece for agents that run all week. Ships docs, benchmarks, an arXiv paper (2512.12818), and PyPI/NPM clients.
**Score:** remit 4 + local 1.5 + maturity 2 + deploy 1.5. *Why it matters for us:* memory is the context layer. This is the closest open-source component to "organizational context that compounds."
**Source:** https://www.instagram.com/p/DeEv2VCoGmJ/

### 8.0 — [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) · 64.4k ⭐ · MIT
**Value prop:** A free, structured path from zero to shipping real AI projects — learn it, build it, share it. A curriculum, not random tutorials.
**Score:** remit 2 + local 2 + maturity 2 + deploy 2. *Why it matters for us:* the fastest way to raise the team's agent fluency toward "Copilot as the main tool."
**Source:** https://www.instagram.com/p/DeEv2VCoGmJ/

### 7.0 — [paperclipai/paperclip](https://github.com/paperclipai/paperclip) · 97.4k ⭐ · MIT · TypeScript
**Value prop:** The open-source app for managing AI agents at work — an operations plane for the agents your team runs, instead of each agent living in someone's terminal.
**Score:** remit 2 + local 1 + maturity 2 + deploy 2. *Why it matters for us:* agent sprawl needs management before it needs more agents; evaluate once the team has agents worth managing.
**Source:** https://www.instagram.com/p/DeEv2VCoGmJ/

### 7.0 — [pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 76.8k ⭐ · Apache-2.0 · JavaScript
**Value prop:** A design language that gives your AI coding agent taste — what it builds looks designed instead of generic. Drop it in and agent-generated UI stops looking the same.
**Score:** remit 1 + local 2 + maturity 2 + deploy 2. *Why it matters for us:* design iteration is token burn; encoded taste (like the repo's skill system) cuts the re-roll loop. Pairs with the "6 design skills" entry in 01.
**Source:** https://www.instagram.com/p/DeEv2VCoGmJ/

### 6.0 — [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) · 53.5k ⭐ · AGPL-3.0 · Python
**Value prop:** A free voice studio that runs fully on your own computer — voice cloning, dubbing, speech-to-text in 646 languages, no ElevenLabs bill.
**Score:** remit 1 + local 2 + maturity 1.5 + deploy 1.5. *Why it matters for us:* cheapest local voice infra found so far — **but AGPL-3.0 is copyleft; get legal review before any enterprise deployment or modification.**
**Source:** https://www.instagram.com/p/DeEv2VCoGmJ/

## Sep 29 — @okaashish "8 Free GitHub Repos Going Viral" (Aashish Pahwa)

Two of the eight (VoiceStudio, Hindsight) are already covered above. The other six, verified and scored:

### 9.0 — [opendatalab/MinerU](https://github.com/opendatalab/MinerU) · 81.1k ⭐ · Python
**Value prop:** Transforms PDFs and Office docs into LLM-ready Markdown/JSON for agentic workflows — the pre-ingestion step that makes "retrieve, don't stuff" actually work. 81k stars makes it the most adopted repo on this page.
**Score:** remit 3 + local 2 + maturity 2 + deploy 2. *Why it matters for us:* document ingestion is the front door of the context layer; clean Markdown in means fewer tokens wasted on layout garbage. **License is unasserted in the API — check before enterprise use.**
**Source:** https://www.instagram.com/p/Dd30VfSD4nA/

### 8.5 — [razorback16/openjev](https://github.com/razorback16/openjev) · 614 ⭐ · Apache-2.0 · Python
**Value prop:** An open, Jev-compatible System One decision server (built on DiffusionGemma) — the open-source answer to this morning's Jev note: typed yes/no/choice/score decisions at ~60 questions per LLM-call cost, self-hosted.
**Score:** remit 4 + local 2 + maturity 1 + deploy 1.5. *Why it matters for us:* decision-model routing is the cheapest tokenomics lever in the playbook; this is the deployable version.
**Source:** https://www.instagram.com/p/Dd30VfSD4nA/

### 7.0 — [hydra-db/open-glean](https://github.com/hydra-db/open-glean) · 1.6k ⭐ · Apache-2.0 · TypeScript
**Value prop:** Open-source AI platform for knowledge work — connect your apps, find answers, get work done. The "second brain" slide, backed by HydraDB (fast graph DB on object storage).
**Score:** remit 2.5 + local 1.5 + maturity 1.5 + deploy 1.5. *Why it matters for us:* knowledge-work agents need connected app context; worth evaluating against the L2 "observable workflows" bar.
**Source:** https://www.instagram.com/p/Dd30VfSD4nA/

### 6.5 — [mvschwarz/openrig](https://github.com/mvschwarz/openrig) · 5.1k ⭐ · Apache-2.0 · TypeScript
**Value prop:** Build your own network of agents from Claude Code, Codex, and Pi — persistent teams with roles and shared context, instead of one-off agent runs.
**Score:** remit 2 + local 1.5 + maturity 1.5 + deploy 1.5. *Why it matters for us:* multi-agent teams are where agent-spend management (Paperclip's problem space) starts; useful reference architecture.
**Source:** https://www.instagram.com/p/Dd30VfSD4nA/

### 5.5 — [varmabudharaju/swarm](https://github.com/varmabudharaju/swarm) · 1 ⭐ · MIT · Python
**Value prop:** "A foreman for teams of Claude Code agents" — decomposes one goal into a parallel task graph, checkpoints every result to disk via hooks, survives interruptions with ask-first resume, and right-sizes the model per job. Closest match to the post's "FOREMAN" slide, but it looks early (1 star, quiet since July).
**Score:** remit 2.5 + local 2 + maturity 0 + deploy 1. *Why it matters for us:* checkpoint-to-disk + per-job model right-sizing are exactly the tokenomics patterns to steal, even if this implementation isn't the one.
**Source:** https://www.instagram.com/p/Dd30VfSD4nA/

### 5.0 — [MxCorpIn/Repolyze](https://github.com/MxCorpIn/Repolyze) · 201 ⭐ · MIT · TypeScript
**Value prop:** Analyzes a GitHub repo into actionable insights, visual diagrams, and exportable reports — AI breakdown of code quality, architecture, and health signals.
**Score:** remit 1 + local 2 + maturity 0.5 + deploy 1.5. *Why it matters for us:* repo-health visibility is useful, but the project has been quiet since March — evaluate before adopting.
**Source:** https://www.instagram.com/p/Dd30VfSD4nA/
