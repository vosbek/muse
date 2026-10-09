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

## Oct 2 — @liamjohnston.ai "SkillOpt-Sleep" (Liam Johnston)

### 8.0 — [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) · 18.1k ⭐ · MIT · Python
**Value prop:** Microsoft's text-space optimizer for agent skills: it reviews your past Claude Code sessions, finds recurring tasks and repeated corrections, and proposes edits to your skills and project instructions — validated on held-out examples before you accept, with human review and automatic backups. "Learn while you sleep": schedule runs overnight, review proposals in the morning. The mechanism is the GEPA pattern from the playbook (trajectory-driven edits, validation-gated updates), pointed at skills instead of prompts.
**Score:** remit 3 + local 1.5 + maturity 2 + deploy 1.5. *Why it matters for us:* every repeated correction you make to Copilot is a skill edit you haven't written yet — this automates exactly that capture loop. Honest caveats from the author: preview software, real runs consume model allowance/budget, session-derived content goes to your configured provider — start with non-sensitive work.
**Source:** https://www.instagram.com/p/DeAWXL3iACs/

## Sep 25 — @qendresahhoti "5 infrastructure repos" (Qendresa Hoti)

"Five GitHub repositories the AI builder community cannot stop talking about — and none of them is a model. This week it's all infrastructure, the stuff around the model that decides whether your agent is fast, honest, and yours. The harness is the story now."

### 8.5 — [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon) · 1.8k ⭐ · MIT · Go
**Value prop:** The cross-harness, self-improving memory layer for AI agents — carries your corrections across Claude Code, Cursor, Codex, and 20+ more tools, instead of each tool forgetting everything.
**Score:** remit 4 + local 2 + maturity 1 + deploy 1.5. *Why it matters for us:* cross-harness memory is the playbook's own thesis (Project Four, the memory-maps work) — this is the closest shipping implementation. Self-improving layer means corrections compound instead of repeating.
**Source:** https://www.instagram.com/p/DduETr9iOkf/

### 8.0 — [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) · 189k ⭐ · AGPL-3.0 · TypeScript
**Value prop:** Turns any messy page or PDF into clean Markdown your agent can actually read — search, scrape, and interact with the web at scale. The ingestion front door, same category as MinerU.
**Score:** remit 3 + local 1 + maturity 2 + deploy 2. *Why it matters for us:* "retrieve, don't stuff" needs clean input; this is the most adopted web→Markdown pipeline in existence. **AGPL-3.0 — legal review before enterprise use or modification.**
**Source:** https://www.instagram.com/p/DduETr9iOkf/

### 6.5 — [kitasota/jev-ultrafast](https://github.com/kitasota/jev-ultrafast) · 0 ⭐ · MIT · Python
**Value prop:** A browser agent that *chooses* instead of generating — picks from what the page offers (Jev-style decision pattern applied to browsing), with seven-second searches as the demo claim.
**Score:** remit 4 + local 1.5 + maturity 0 + deploy 1. *Why it matters for us:* the decision-instead-of-generation pattern is the cheapest tokenomics lever in the playbook, and browsing is where agents currently burn the most tokens guessing. Two weeks old, zero stars — pattern to watch, not code to adopt yet.
**Source:** https://www.instagram.com/p/DduETr9iOkf/

### 6.5 — [jamiepine/voicebox](https://github.com/jamiepine/voicebox) · 56.5k ⭐ · MIT · TypeScript
**Value prop:** The open-source AI voice studio — clone, dictate, create. Hold a key, talk, it types; nothing leaves your laptop.
**Score:** remit 1 + local 2 + maturity 2 + deploy 1.5. *Why it matters for us:* local-first voice input for the team's workflow; low remit fit beyond that, but the local-only posture is the pattern to note.
**Source:** https://www.instagram.com/p/DduETr9iOkf/

### 6.0 — [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) · 93k ⭐ · MIT · TypeScript
**Value prop:** The open-source CapCut alternative — videos stay on your machine.
**Score:** remit 0.5 + local 2 + maturity 2 + deploy 1.5. *Why it matters for us:* minimal direct remit fit (video editing, not agent infra) — included for completeness of the roundup; the local-first distribution model is the only transferable lesson.
**Source:** https://www.instagram.com/p/DduETr9iOkf/

## Sep 25 — @entrenology "5 open-source AI projects exploding" (Entrenology)

Framed for solo builders ("execution speed of an entire engineering team"); the caption also funnels toward a paid ebook, but all five repos are independently verified below — all MIT, all pushed within the last 3 days:

### 9.5 — [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) · 73.7k ⭐ · MIT · TypeScript
**Value prop:** Free MIT AI gateway: one endpoint, 359 providers (150+ free), 1200+ models. Route across the entire market from a single integration instead of wiring each provider.
**Score:** remit 4 + local 1.5 + maturity 2 + deploy 2. *Why it matters for us:* this is the cheapest-model-routing lever as free infrastructure — 150+ free providers means the "route by difficulty" tactic can start at $0. Highest score on this page to date, and the most direct bill-cutter in the set.
**Source:** https://www.instagram.com/p/DdtRDoSCll-/

### 8.5 — [mattpocock/skills](https://github.com/mattpocock/skills) · 278k ⭐ · MIT · Shell
**Value prop:** Portable engineering skills for AI coding agents, straight from Matt Pocock's own .agents directory — "Skills for Real Engineers."
**Score:** remit 2.5 + local 2 + maturity 2 + deploy 2. *Why it matters for us:* the playbook's own skill-system thesis, from the practitioner who gave the "Fixing the PR Bottleneck" talk — a reference implementation of encoded team taste.
**Source:** https://www.instagram.com/p/DdtRDoSCll-/

### 8.0 — [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) · 244.6k ⭐ · MIT · TypeScript
**Value prop:** "Everything is a Plugin" — a runtime that turns models into agents through a plugin architecture.
**Score:** remit 2.5 + local 1.5 + maturity 2 + deploy 1.5. *Why it matters for us:* harness engineering is the factory-talk thesis; a 244k-star plugin runtime is the reference architecture to study before building your own.
**Source:** https://www.instagram.com/p/DdtRDoSCll-/

### 8.0 — [stablyai/orca](https://github.com/stablyai/orca) · 86.5k ⭐ · MIT · TypeScript
**Value prop:** An ADE (agentic development environment) for working with a fleet of parallel agents — run any coding agent with your own subscription, in parallel workspaces.
**Score:** remit 2.5 + local 1.5 + maturity 2 + deploy 2. *Why it matters for us:* parallel-agent fleets are where the next cost blowup lives; "use your own subscription" is the cost-control framing, and fleet management is the missing ops layer.
**Source:** https://www.instagram.com/p/DdtRDoSCll-/

### 7.5 — [tt-a1i/archify](https://github.com/tt-a1i/archify) · 78.7k ⭐ · MIT · JavaScript
**Value prop:** Turns any idea, plan, or codebase into a beautiful interactive diagram — shipped as an agent skill for Claude Code, Codex, and more.
**Score:** remit 2 + local 1.5 + maturity 2 + deploy 2. *Why it matters for us:* architecture diagrams are onboarding context — generated, visual, and agent-consumable, they cut the "read the whole repo to understand it" token tax for every new agent session.
**Source:** https://www.instagram.com/p/DdtRDoSCll-/

## Oct 7 — @justinmendez.ai "diagram-design" (Justin Mendez)

A single repo, not a roundup — recommended for the jump in his agent's diagram quality ("visual diagrams that actually make sense to a human"). Trending on GitHub again this week on a 2.5.10 release:

### 8.0 — [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 44.8k ⭐ · MIT · HTML
**Value prop:** Editorial diagram design as an agent skill — 42 diagram types as self-contained HTML + SVG, no build step, no JS, no external images. Scrapes your website's style tokens and matches the brand in 60 seconds. New in 2.5.10: ten more layout grammars (Sankey, fishbone, Wardley map, kanban, user journey, deployment, dependency graph, UML class, story map, database schema). Works with Claude Code, Codex, **GitHub Copilot**, Factory Droid, and Pi — "No shadows. No Mermaid slop."
**Score:** remit 2 + local 2 + maturity 2 + deploy 2. *Why it matters for us:* this playbook's standing bar is diagrams-or-infographics, not walls of text — and the failure mode this repo fixes (generic rounded-box Mermaid slop) is exactly the one we keep fighting. A Copilot-compatible skill the whole team can install, outputting brand-matched editorial diagrams; also redraws existing draw.io/Mermaid/Excalidraw sources. Project site: diagramdesign.dev.
**Source:** https://www.instagram.com/reel/DeMvIM-IdSR/

## Oct 8 — @kem_glitch "glitch-walk" (Kem @ GlitchCatClub)

A single repo, not a roundup — a free skill that shows how your own project works, launched the same day as the reel ("not finished — just started working on it today"):

### 4.5 — [Glitch-Cat-Club/glitch-skills](https://github.com/Glitch-Cat-Club/glitch-skills) · 2 ⭐ · MIT · Python
**Value prop:** Ask "what happens when I…?" about your own project and get a page with the real screens, every hidden step in order, and the code behind each step (file + line, click to reveal) — aimed at the vibe-coded "black box" problem. Skill-folder install (SKILL.md + Python scripts via `uv`, builds a self-contained HTML page).
**Score:** remit 2 + local 1 + maturity 0.5 + deploy 1. *Why it matters for us:* codebase comprehension as context compression — a generated "how this works" page cuts the per-session "read the whole repo" token tax, same family as diagram-design and archify. Scored honestly: the concept is strong and MIT-licensed, but it's day-zero (2 stars, author-flagged unfinished) and Copilot compatibility is undeclared — watch, don't deploy yet.
**Source:** https://www.instagram.com/reel/DePJAUftlJD/

## Oct 9 — @git.radar "context-mode" (Git Radar)

A single repo, not a roundup — an MCP server for context window optimization in AI coding agents, surfaced by @git.radar's repo roundup:

### 8.5 — [mksglu/context-mode](https://github.com/mksglu/context-mode) · 25.9k ⭐ · Elastic-2.0 · TypeScript
**Value prop:** Context window optimization for AI coding agents — sandboxes tool output (claimed 98% reduction), persists session memory in SQLite, "Think in Code" (the LLM programs its analysis instead of reading files), and enforces routing across 17 platforms via MCP + hooks. Slash commands (/ctx-stats, /ctx-index), works with Claude Code, VS Code, Cursor, JetBrains, OpenCode.
**Score:** remit 3.5 + local 2 + maturity 1.5 + deploy 1.5. *Why it matters for us:* this is the context-layer thesis in a box — tool-output sandboxing is exactly the "select useful information, filter/compress" step from the Context Engineering pipeline in 02, and session memory is the 03 problem. Scored honestly: the 98%/99% savings claims are vendor marketing, unverified; **Elastic License 2.0 is source-available, not OSI open-source — no managed-service use, get legal review before enterprise deployment**; and Copilot compatibility is undeclared (VS Code is listed, but his team is Copilot-only). Still the strongest context-economics repo on the page — pilot before committing.
**Source:** https://www.instagram.com/reel/Dd6qqdaAfpI/
