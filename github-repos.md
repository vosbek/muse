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

## Sep 27 — @sebastianhardy_ "5 guardrail repos before your agent writes another line" (Sebastian Hardy)

Framed as guardrails for safety and quality — the post opens with "one in four AI skills people share online has a security hole." Links were DM-gated; repos identified from the video and verified on GitHub:

### 9.0 — [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) · 19.5k ⭐ · Apache-2.0 · Python
**Value prop:** NVIDIA's security scanner for AI agent skills — detects vulnerabilities, malicious patterns, prompt injection, and data exfiltration *before* you install a skill.
**Score:** remit 3 + local 2 + maturity 2 + deploy 2. *Why it matters for us:* a team standardizing on Copilot + a skill library is building a software supply chain; this is the intake scanner for it. Highest-priority install of the five.
**Source:** https://www.instagram.com/p/DdzSy8yxipJ/

### 8.5 — [JayPokale/Chisle](https://github.com/JayPokale/Chisle) · 624 ⭐ · MIT · JavaScript
**Value prop:** Cuts your AI coding agent's token bill on three axes: terse prose, YAGNI-first code, and tool-output compression. Stops the agent rambling and building things you never asked for.
**Score:** remit 4 + local 2 + maturity 1 + deploy 1.5. *Why it matters for us:* pure tokenomics — output verbosity and unasked-for code are the two most taxable agent behaviors, and this attacks both at the source.
**Source:** https://www.instagram.com/p/DdzSy8yxipJ/

### 7.5 — [ibelick/ui-skills](https://github.com/ibelick/ui-skills) · 9.4k ⭐ · MIT · TypeScript
**Value prop:** Skills for design engineers — the design rules pros follow (spacing, motion, accessibility) so agent-built apps stop looking like generic AI output.
**Score:** remit 1.5 + local 2 + maturity 2 + deploy 2. *Why it matters for us:* same thesis as Impeccable — encoded taste cuts the design re-roll loop, which is token burn.
**Source:** https://www.instagram.com/p/DdzSy8yxipJ/

### 7.0 — [reticlehq/reticle](https://github.com/reticlehq/reticle) · 1.2k ⭐ · TypeScript
**Value prop:** "Jev-style machine-native runtime perception" — opens your real app and verifies what the agent claims it built, instead of trusting "done."
**Score:** remit 2.5 + local 1.5 + maturity 1 + deploy 1.5. *Why it matters for us:* closes the verification gap every agent demo hand-waves past. **License unasserted in the API — check before enterprise use.**
**Source:** https://www.instagram.com/p/DdzSy8yxipJ/

### 7.0 — [dmmulroy/anti-slop](https://github.com/dmmulroy/anti-slop) · 5.2k ⭐ · MIT · TypeScript
**Value prop:** Opinionated Oxlint rules that reject low-evidence TypeScript/JavaScript patterns — catches the lazy shortcuts AI loves to write before they land.
**Score:** remit 1.5 + local 2 + maturity 1.5 + deploy 2. *Why it matters for us:* a lint gate is the cheapest quality control on machine-written code; pairs with the reviewer-subagent pattern from the Pocock talk.
**Source:** https://www.instagram.com/p/DdzSy8yxipJ/

## Sep 22 — @githubsignals "System One Harness: AI That Never Lies" (Github Signals)

### 8.0 — [HarnessRouter/SystemOneHarness](https://github.com/HarnessRouter/SystemOneHarness) · 202 ⭐ · Apache-2.0 · Python
**Value prop:** The System One harness for System One models — run Jev and other decision models locally or via HarnessRouter.ai. The model picks one action from a strict list of options instead of generating text, tracks its own confidence, and refuses to act when unsure — producing a verifiable record of every decision. (The video's "never lies / perfect for banking" framing is the creator's; the mechanism is real, the guarantees are bounded by the option set you define.)
**Score:** remit 4 + local 2 + maturity 0.5 + deploy 1.5. *Why it matters for us:* this is the harness half of the Jev thesis — OpenJev is the decision server, this is the runtime that runs it locally. Together they're the full local-first decision stack. Young repo (3 weeks), watch for hardening.
**Source:** https://www.instagram.com/p/Ddnh350ijC7/

## Oct 6 — Web find: chamnan (answer to the Oct 4 context-cost tooling ask)

### 7.0 — [ArcticFox2029/chamnan](https://github.com/ArcticFox2029/chamnan) · 9 ⭐ · MIT · Python
**Value prop:** A repo-local engineering-context index — commits an architecture index, impact map, session records, and decisions as Markdown beside the code, so an agent *reads* instead of re-scanning the repo every session. No network calls, no embedding model, no daemon: Python stdlib only. Ships a CLI plus adapters for 22 agents including Copilot. Measured: 11.56M tokens → 51,937-token index (28.8x on the published corpus).
**Score:** remit 3 + local 2 + maturity 0.5 + deploy 1.5. *Why it matters for us:* this is the agent-side half of the context-cost answer — the tokenomics deep dive already covers the serving half (routing, caching, compression, observability). Honest caveats, straight from its README: the author's 223x figure is on an unpublished corpus (not independently reproducible); the README itself cites studies arguing *against* context files (it claims efficiency, not correctness: −29% runtime, −17% output tokens); 9 stars means you're an early adopter. Suggested pilot: run it on one repo and measure real Copilot savings with ccusage (already in the playbook stack).
**Source:** web research, Oct 2026

## Oct 3 — @meow.codes "openai/symphony" (GIT Dev)

### 7.5 — [openai/symphony](https://github.com/openai/symphony) · 27.6k ⭐ · Apache-2.0 · Elixir
**Value prop:** OpenAI's official harness for turning project work into isolated, autonomous implementation runs — connect it to Linear, it monitors incoming work and spawns agents per task. The standout is the automated proof-of-work pipeline: agents verify CI status, run complexity analyses, gather PR feedback, and produce walkthrough videos before anything merges. Ships a general spec plus an experimental Elixir reference implementation for teams practicing harness engineering.
**Score:** remit 3 + local 1 + maturity 2 + deploy 1.5. *Why it matters for us:* "manage work instead of supervising coding agents" is the factory-talk thesis made official — and the proof-of-work pipeline (CI + complexity + PR feedback + video walkthrough as merge gates) is the verification pattern every enterprise agent deployment needs. Experimental status keeps deploy at 1.5.
**Source:** https://www.instagram.com/p/DeD1oLtgbPy/

## Oct 2 — @marc.kaz "definitive-opensource" (Marc Kaz)

### 7.0 — [mustbeperfect/definitive-opensource](https://github.com/mustbeperfect/definitive-opensource) · 3.6k ⭐ · MIT
**Value prop:** A human-vetted map of 840 open-source apps you can actually use — AI, chat, editors, media, productivity — with Windows/macOS/Linux/self-hosted lists, active-vs-abandoned tags, and security alerts. The anti-awesome-list: curated against dead repos, not a dump of them.
**Score:** remit 1.5 + local 1.5 + maturity 2 + deploy 2. *Why it matters for us:* it's the discovery layer for the local-first stack — when the answer is "replace the paid cloud app with a self-hosted one," this is where you look first. A directory, not a tool, so it scores on usefulness rather than direct remit fit.
**Source:** https://www.instagram.com/p/Dd_6oRisdsT/
