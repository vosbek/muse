# Tools & Capabilities Inventory — instructions already in the playbook

Everything below has a distilled write-up with usage instructions in the repo / on the site. Format per item: **tool — capability**, and where to find the instructions.

## Claude Code & Agents (26 items)

- **Turn Instagram Saves into a Notion content system** — tools: Notion (database + API), Claude Code / Codex · skill: Scheduled intake automation — define a schema, connect the source, sync on a cadence, then run a transform step that converts raw captures into usable output.
- **Dynamic workflows: let the agent write its own orchestration** — tools: Claude Code (dynamic workflows), Langfuse (trace observability) · skill: Agent-written orchestration — provide coordination tools, not fixed graphs; always keep trace inspection as the verification step.
- **The 6 design skills worth keeping (after testing 70+)** — tools: stitch-skill, taste-skill, impeccable, remotion, hyperframes, gsap (skill names as presented) · skill: Skill portfolio review — regularly test your installed skills against real tasks, keep the winners, delete the rest. A small set of proven skills beats a large set of maybe-skills.
- **YouTube pipeline skill: offload analysis to free engines** — tools: Claude Code (custom skills), NotebookLM (notebooklm.google.com) · skill: Free-engine offload — identify the comprehension-heavy step in a workflow, route it to a free external engine, import only the synthesis.
- **Three systems to unlock Claude Code's design power** — tools: Google Stitch (MCP), Nano Banana 2, UI UX Pro Max (GitHub skill library), 21st.dev · skill: Reference-driven generation — never ask an agent to design from nothing; feed it mockups, encoded taste, and real components first.
- **Three Claude Code skills: GSD, superpowers, skill-creator** — tools: [obra/superpowers](https://github.com/obra/superpowers), Anthropic skill-creator (official), GSD v1.9.6 · skill: Skill-stack thinking — install an execution-discipline skill, a capability library, and a capture tool; the last one is how the other two keep improving.
- **One frontend-design skill replaces 18 months of vibe-coding** — tools: Claude Code / Codex (skills feature) · skill: Taste-encoding — when a workflow finally produces great output, capture it as a skill immediately; that's the moment 18 months of learning becomes a file.
- **Top 3 subagents: Explorer, Research Documenter, Historian** — tools: Claude Code (subagents) · skill: Context-labor division — push discovery, parallel research, and checkpointing into subagents; keep the main thread for judgment and edits only.
- **AI Engineer Paris talk: /retro, /pr, and getting more from agents** — tools: None linked in post text. · skill: Encode repeatable agent workflows (retrospectives, PR prep) as named commands, not ad-hoc prompts.
- **Getting the most out of Opus 5.5: hand over whole tasks, define "done"** — tools: claude.dev (blog link card in post) · skill: Delegate whole tasks with an explicit definition of done and scheduled check-ins instead of micromanaging steps.
- **A real-world Opus 5.5 benchmark on actual knowledge-work tasks** — tools: Mike's Checks benchmark — checks.every.to/p/mikes-checks · skill: Evaluate models on your own real work tasks, not just synthetic benchmarks, before committing workflows to them.
- **A Jev plugin for Claude that audits tool calls and compacts context in 1 second** — tools: None linked in post text (Jev plugin for Claude; @typesafeai mentioned). · skill: Audit and compact your agent's tool-call trace with a cheap model in real time to control long-session costs.
- **shadcn/lint: a linter for Tailwind design systems built for agents** — tools: shadcn/lint (announced by @shadcn; no URL in post text) · skill: Adopt agent-first tooling (like design-system linters) that enforces consistency on machine-written code.
- **Skill-driven development: a full CRM dashboard in two days with Claude** — tools: Skills — skills.sh/jakubkrehel/sk; skills.sh/emilkowalski/s… (display truncated in source). Demo app — sales-crm-kargulstudio.vercel.app · skill: Build a reusable skill library and compose skills to drive full-app builds instead of writing one-off prompts.
- **Put HTML-explainer instructions in your CLAUDE.md / AGENTS.md** — tools: None linked in post text. · skill: Write output-format instructions once into CLAUDE.md/AGENTS.md so every future session inherits them.
- **24 reusable agent skills distilled from 14 years at Google** — tools: None linked in post text. · skill: Accumulate agent leverage as a library of reusable skills, not as one-off prompts or single agents.
- **Second batch (Aug 24 – Sep 12)**
- **claude plugin eval — measure what your plugin actually adds** — tools: Claude Code (claude plugin eval) · skill: Eval every customization — measure plugin/skill delta against baseline before and after changes.
- **Spotify's internal Claude Code setup that cut token spend** — tools: None linked in visible text. · skill: Standardize the winning harness org-wide; token savings multiply by headcount.
- **/show-me — a skill that makes PR descriptions readable** — tools: github.com/humanlayer/skills (skills/plugins/show-me) · skill: Package recurring jobs (PR descriptions, reviews) as installable skills, not prompts.
- **Claude Commerce Agents — open-source blueprint for shopping agents** — tools: Claude Commerce Agents (open source; link at permalink) · skill: Start new agent domains from reference architectures, not blank prompts.
- **Audit your skills with /claude-api prompt-audit** — tools: Claude Code (/claude-api prompt-audit) · skill: Re-audit skills on every model upgrade; instructions tuned for the old model are technical debt.
- **Anthropic's prompt that eliminates "claudese"** — tools: platform.claude.com (Prompting Claude Fable 5.1) · skill: Treat output-style guidance as a versioned dependency; refresh it from vendor docs per model.
- **Two account recommendations for learning Claude (brief)** — tools: None. · skill: Curate a learning feed of practitioner accounts; the field moves too fast for static docs alone.
- **Hackathon winner's full Claude Code setup: 68 subagents, 286 skills** — tools: Full setup open-sourced (link at permalink) · skill: At scale, the agent setup is a system — study large open setups for subagent/skill organization patterns.
- **VS Code Learn: Java, idea to agent-ready (brief)** — tools: aka.ms/VSCode/Learn-Java · skill: Learn tools through their agent workflows; that's where vendors now put the leverage.

## Jevons / Context Economics (37 items)

- **jevgrep: cut coding-agent cost ~30% with better file retrieval** — tools: [dshng/jevgrep](https://github.com/dshng/jevgrep) (npm: `@dshng/jevgrep`) · skill: Retrieval-first cost control — instrument $/task, then optimize the finding step (targeted search returning exact lines) before upgrading models.
- **Jev: choose MCP tools without polluting the main context** — tools: MCP servers (pattern-level; no single repo) · skill: Decision-model isolation — route every selection problem (tools, models, next actions) through a small model in its own context; inject only outcomes into the main session.
- **SLMs will replace LLMs — because the economics demand it** — tools: None (prediction/thesis) · skill: Two-tier model strategy — default narrow work to SLMs; require evidence (not habit) before spending frontier tokens.
- **Open-source adapter that decouples your agent from any single LLM provider** — tools: None linked in post text (TypeSafe AI / @typesafeai mentioned). · skill: Decouple your routing layer from your generation provider so models become swappable commodities.
- **A research-agent CLI claiming 40% lower coding-agent cost on SWE-bench** — tools: jevgrep — github.com/dzhng/jevgrep · skill: Put a cheap decision model in front of your coding agent's research loop and measure cost-per-task on SWE-bench.
- **The Jev founder's 12-page guide to pairing Jev with LLMs** — tools: None linked in post text (PDF location not in visible text). · skill: Route binary and classification decisions to a cheap decision model, never to a frontier autoregressive model.
- **System One models: the ultra-fast decision-model wave** — tools: None linked in post text. · skill: Use System One–style fast decision models for harness routing and gating layers where latency dominates.
- **Pairing Jev with Opus 5.5 in a builder's agentic harness** — tools: None linked in post text. · skill: Split your harness: cheap decision model decides, frontier model executes.
- **The Jev setup guide for maximum quality at minimum cost** — tools: None linked in post text. · skill: Treat your model config as a cost-quality optimization problem and share exact configs, not vibes.
- **Using Jev at ticket creation to prompt for missing follow-up questions** — tools: None linked in post text (@typesafeai mentioned). · skill: Deploy cheap decision models at intake funnels to detect missing information before humans touch the ticket.
- **20 must-use Jev skills for agent setups** — tools: jev-ultrafast (browser agent) — github.com/browser-use/je… (display truncated in source); fast-jev-compaction (context compression) — github.com/tamaratran/fas… (display truncated in source) · skill: Package decision-model capabilities as reusable skills (browse, compact, render) instead of one-off prompts.
- **A PDF on building a Jev harness for coding agents** — tools: None linked in post text. · skill: Build your coding-agent harness with a cheap decision layer in front of the expensive generation model.
- **Jev makes agent evals dramatically cheaper** — tools: None linked in post text. · skill: Run your agent evals on a cheap local decision model so measurement costs approach zero.
- **Jev as an industry-scale moment, with a 10-step setup roadmap** — tools: None linked in post text. · skill: Treat the decision model as your agent's control plane: its job is choosing the next action.
- **SimpleJev: open-weights decision models with vision, classifying 1,697 events** — tools: None linked in post text (SimpleJev by @Richelle_Ji). · skill: Shape open-weight models into structured classifiers instead of renting the decision layer from an API.
- **Third-party demo: instant generative UI from json-render plus Jev** — tools: json-render (generative UI skill mentioned; no URL in post text) · skill: Have decision models emit structured UI specs (JSON) instead of rendered text for instant generative interfaces.
- **Jev cloned 3 days after launch: the model is not the moat** — tools: CUA-S1 — github.com/trycua/cua · skill: Build on the cheap-decision-layer pattern, not on any single vendor's model, because clones arrive in days.
- **Jev's pricing hook: cents per million input tokens** — tools: None (pricing signal, not a tool). · skill: Price your decision layer separately from your generation layer; cents-per-million changes what you can afford to run on every call.
- **Three-layer agent architecture: deterministic filters first** — tools: None (architecture take). · skill: Put deterministic programmatic filters first; only spend model calls on what survives the rules.
- **A Jev model router mod for Claude Code via AI Gateway** — tools: None linked in post text (@typesafeai and @vercel AI Gateway mentioned). · skill: Implement your cost split in the router: route decision calls to the cheap model, generation calls to the frontier model.
- **LLMs vs. Jev, clearly explained** — tools: None linked in post text. · skill: Adopt decision models for decision-shaped work, not as a faster drop-in for generation.
- **An open-source Jev clone that already outperforms it** — tools: Laya (open-source Jev-class model) — huggingface.co/convaiinnovati… (display truncated in source) · skill: Track open clones of decision models; the best local-first option may already beat the API version.
- **If you're confused about Jev, study this harness article** — tools: None linked in post text. · skill: When a new model class lands, find the practitioner's canonical explainer and study it before the commentary.
- **Bespoke Nimble: fully open 9B decision model with open data and recipe** — tools: Bespoke Nimble — github.com/bespokelabsai/… (display truncated in source); huggingface.co/bespokelabs/Be… (display truncated in source) · skill: Prefer open-data, open-recipe decision models when you need to audit, reproduce, or self-host the decision layer.
- **CUA's 2.8MB model: System One models go tiny** — tools: CUA-S1 — github.com/trycua/cua · skill: Push tiny decision models to the edge; at megabyte scale, per-decision cost effectively vanishes.
- **The one-line definition: decisions, not generation** — tools: None linked in post text. · skill: Classify every model call in your harness as decision-shaped or generation-shaped, then match the model to the shape.
- **Jev as a literal if statement** — tools: Demo — bably-lang.southpolesteve.workers.dev · skill: Treat decision-model calls as control flow (if statements), not as chat completions.
- **The 45-second Jev explainer practitioners converged on** — tools: None linked in post text. · skill: Onboard teams to a new model pattern with the shortest clear explainer first, depth later.
- **A skeptic's take: the simple question behind the Jev launch** — tools: None linked in post text. · skill: Look for model advances that come from better problem decomposition, not just bigger models.
- **Jev for PR review: ~200x cheaper than Claude, half a second** — tools: None linked in post text. · skill: Run decision-shaped checks (like PR review) on every event once the cost multiple makes it free in practice.
- **jev(): a PostgreSQL extension for natural-language database search** — tools: None linked in post text. · skill: Consider decision models as a direct natural-language interface to structured data, bypassing embedding pipelines where possible.
- **A visual explanation of Jev built on Qwen2.5-RLCD** — tools: Qwen2.5-RLCD (open model on Hugging Face; no URL in post text) · skill: Ground new model claims in their mechanism (single-decoder, non-autoregressive) before adopting the hype framing.
- **A 45-second TL;DR that makes Jev's simple core idea click** — tools: None linked in post text. · skill: If an idea is truly simple, teach it in under a minute; length signals the teacher doesn't get it yet.
- **The founder's question: why haven't superhuman chat models led to AGI?** — tools: None linked in post text. · skill: Question whether you're climbing the right ladder: generation scale vs. decision quality are different games.
- **Second batch (Aug 24 – Sep 12)**
- **GitHub: "Using more tokens doesn't always mean better results"** — tools: github.blog (How we make AI coding more cost efficient without sacrificing task quality) · skill: Define efficiency as context-sufficiency per dollar; use GitHub's published framing to anchor the enterprise tokenomics program.
- **Claude Platform: cutting cost without cutting quality** — tools: Claude Platform docs (article link at permalink) · skill: The big three cost levers — prompt caching, instruction hygiene, effort routing — applied systematically.

## Agent Memory (18 items)

- **A real agentic coding graph: Project Four** — tools: Private GitHub repo (planned community release); Codex, Claude Code, OpenCode CLIs · skill: Cross-harness memory — centralize transcripts from every agent tool into one searchable local store; verify agent-built systems with headless production runs.
- **Long-term memory in three skills: /memory, /recall, /rem sleep** — tools: Claude Code (skills) · skill: Memory as three subsystems — hierarchical storage, background consolidation, background retrieval; never let bookkeeping touch the main thread.
- **Continual learning with a nested memory tree** — tools: Claude Code (subagents; system in development) · skill: Gardened memory — use a nested structure plus background subagents for pruning/consolidation, so memory stays an asset instead of becoming bloat.
- **The harness is the hidden layer (why coding agents really fail)** — tools: Strands Agents SDK (AWS, open source on GitHub); paper arXiv 2606.17454 · skill: Harness-first debugging — verify unique matches, whole-line edits, post-edit diffs, and upfront rejection before blaming model quality.
- **A self-improving agent via lessons.md** — tools: None (markdown file + discipline) · skill: lessons.md loop — capture corrections immediately, re-read at session start, apply before acting. Start here before building anything fancier.
- **Unreal Agent: an open-source harness claiming state-of-the-art cost efficiency** — tools: None linked in post text. · skill: Optimize the harness itself (orchestration, memory, retries), not just the model, for the next cost multiple.
- **Graph engineering for agents: Jev fits the LangGraph memory model** — tools: None linked in post text (LangGraph mentioned). · skill: Model agent memory as a graph and put cheap decision models at the routing nodes.
- **Second batch (Aug 24 – Sep 12)**
- **The clearest agent-harness explainer, turned into a guide** — tools: None linked in post text. · skill: Onboard agent builders with harness-first mental models before model specifics.
- **Production AI agents inside a PE portco's prior-auth pipeline** — tools: None linked in post text. · skill: Deploy agents inside existing regulated workflows with human gates; paperwork-heavy processes are the best first targets.
- **The harness deep-dive: it's not the model** — tools: None linked in post text. · skill: When an agent fails, debug the harness (loop, tools, state, evals) before blaming the model.
- **Endorsement of the harness breakdown** — tools: None. · skill: Weight explainers by independent practitioner convergence, not by like counts alone.
- **Agent primitives should graduate from Slack markdown files** — tools: None linked in post text. · skill: Give agent primitives a real supply chain — versioned, owned, distributed, deprecable — not Slack folklore.
- **Agent customization converges on Skills, not prompt files** — tools: GitHub Copilot (AHP harness engine) · skill: Build all agent customization as Skills; prompt files are the legacy format.
- **Inside a real AI Factory at LimestoneHQ** — tools: None linked in post text. · skill: Study production factory postmortems for the ticket-to-merge failure modes; that's where the real design constraints live.
- **The enterprise AI factory explainer, endorsed** — tools: None. · skill: Same as above — treat practitioner-converged explainers as canonical.
- **Tobi open-sources self-improving-loop infra (tangleml)** — tools: tangleml.com · skill: Adopt self-improving-loop infrastructure; systems that don't learn from operation pay a permanent tax.
- **The 1% of AI engineers build self-improving systems (×2)** — tools: None. · skill: Build the feedback loop, not just the agent; self-improvement is the senior skill.

## Automation (7 items)

- **Power Automate: the daily email recap flow** — tools: Microsoft Power Automate (make.powerautomate.com), Outlook · skill: Deterministic-first triage — use scheduled flows with keyword rules for routine sorting; escalate only the ambiguous cases to AI.
- **MarkItDown + Obsidian: make your files usable for agents first** — tools: [microsoft/markitdown](https://github.com/microsoft/markitdown), Obsidian (obsidian.md) · skill: Ingest-then-reason — convert all source material to clean markdown before any agent touches it; treat input hygiene as a cost control.
- **NotebookLM as a free content engine for Claude Code** — tools: NotebookLM (notebooklm.google.com), Claude Code, plus a GitHub repo for the integration shown in the video · skill: Free-engine content pipeline — draft with NotebookLM's free generation, refine with your own voice in Claude Code.
- **Automate any browser task with Claude Code + Playwright** — tools: Claude Code, Playwright MCP server · skill: Demonstrate-then-automate — narrate the task once, let the agent build the Playwright automation, save it as a slash command.
- **Google's Gmail agent builder — and why Zapier still wins on breadth** — tools: Google AI agent builder (Gmail), Zapier (zapier.com) · skill: Breadth-first platform evaluation — score automation tools on integration coverage and escape hatches before committing workflows to them.
- **Second batch (Aug 24 – Sep 12)**
- **A PR review agent that survived production at a PE-backed client** — tools: None linked in post text. · skill: Ship PR review as the first production agent: bounded, high-volume, human keeps merge authority.

## Prompts & Evals (1 items)

- **How to run experiments on prompts when output quality is critical** — tools: None (methodology) · skill: Rule-ROI testing — for each prompt rule, run repeated trials, measure aggregate quality and latency, keep only rules that prove their worth; default to fewer, deterministic rules.

## Design & Vibe Coding (12 items)

- **Free interface starter skins for AI-built UIs** — tools: Free starter-skins repo (via @kem_glitch), Claude Code · skill: Reference-first UI — start every AI-built interface from a concrete skin or reference, not from a blank prompt.
- **Four JS animation libraries for modern sites** — tools: GSAP (gsap.com), Anime.js (animejs.com), Motion.dev (motion.dev), React Spring (react-spring.dev) · skill: Motion taxonomy — map each animation need to its purpose-built library; encode the mapping in your design skill.
- **Landing pages via five-agent teams** — tools: Claude Code (agent teams) · skill: Diverge-then-synthesize — synthesize one strong skill, fan out N agents with anti-convergence communication, merge the best elements.
- **3D animated sites: Nano Banana Pro + Veo 3 + GSAP** — tools: Nano Banana Pro (Google), Veo 3 (Google), GSAP (gsap.com) · skill: Chained generation with structured handoffs — image model → video model → frame dissection → scroll animation, with explicit metadata at each boundary.
- **Four levels to de-genericize vibe-coded apps** — tools: Mobbin (mobbin.com), 21st.dev, Google Stitch, Figma MCP · skill: The constraint ladder — references → specific prompts with avoid-lists → locked style guide → Figma MCP; climb as far as the project warrants.
- **Vibe prototyping inside big tech** — tools: Internal AI tooling (Instagram/Meta) · skill: Demo-driven proposals — replace the doc-and-meeting cycle with a 24-hour clickable prototype wherever decisions are slow.
- **Nine UI design languages for vibe-coding** — tools: Manus AI (manus.ai) · skill: Named-style vocabulary — encode design languages as named tokens in your design skill; one word replaces pages of prompt.
- **Your project architecture on an interactive canvas** — tools: None linked in post text (OpenShip). · skill: Give every generated architecture an interactive visual map so humans can comprehend what agents built.
- **Why builders are endorsing OpenShip** — tools: None (opinion/endorsement). · skill: Track which open-source dev tools earn same-day builder endorsements; that's your evaluation shortlist.
- **A transitions library built for agent-generated UIs** — tools: transitions.dev · skill: Give your UI agents a transitions library so generated interfaces ship with polish, not just function.
- **Second batch (Aug 24 – Sep 12)**
- **Generative UI goes 3D: Blender MCP + Astra + Tripo** — tools: Blender MCP, Astra, Tripo (3D generation) · skill: Route generative UI through professional tools via MCP; the output ceiling follows the tool, not the model.

## AI News (14 items)

- **Opus 4.5 is amazing — Claude Code is the problem** — tools: Qwen-Agents / Qwen Code 3.0 (open source, Qwen), Claude Code, Opus 4.5 (Anthropic) · skill: Stack-separated evaluation — benchmark model vs. harness independently on your real tasks; re-test open alternatives regularly.
- **Gemini grounding with Google Maps: 250M real-world locations** — tools: Gemini app (Google), Google Maps Platform · skill: Data-moat evaluation — when choosing platforms, score proprietary live-data access as heavily as model benchmarks.
- **Six lessons on getting the most out of bots, from Grok Bot's leads** — tools: None (news). · skill: Default to delegating keyboard-and-mouse work to bots; learn the delegation playbook from teams that ship them.
- **The week in agents: xAI, Meta, OpenAI, Anthropic roundup** — tools: None (news). · skill: Run a weekly scan of agent releases across labs instead of relying on sporadic deep dives.
- **GitHub Copilot models deprecated Oct 19, 2026 — don't hard-tie to one model** — tools: None (news). Changelog — github.blog/changelog/2026… (display truncated in source) · skill: Keep prompts, skills, and evals portable; treat model deprecation as a routine operational event.
- **New Jira canvas in the GitHub Copilot app** — tools: None (news). · skill: Evaluate agent surfaces that turn tickets directly into action to shorten the ticket-to-code path.
- **Claude now writes 80% of Anthropic's code; engineers ship 8x more** — tools: None (news). Blog — claude.com/blog/agentic-c… (display truncated in source) · skill: Measure your own agent-written code share and throughput; don't manage by vendor benchmarks alone.
- **Second batch (Aug 24 – Sep 12)**
- **GitHub's HydraFusion: frontier-level coding from the orchestrator** — tools: gh.io/githubcopilotd (Project HydraFusion) · skill: Evaluate coding assistants on orchestration quality; the router is the product.
- **Hands-on with HydraFusion: "exactly how you'd want a teammate to work"** — tools: gh.io/GitHubCopilotD · skill: Eval agent tools on teammate-behavior, not just benchmarks.
- **HydraFusion in plain English** — tools: None. · skill: When a launch spawns instant explainers, treat the category as fast-moving and track it closely.
- **Lerna: use HydraFusion in the Copilot CLI, watch subagents live** — tools: github.com/sirredbeard/Lerna · skill: Demand subagent observability in any orchestrator; fan-out without visibility is undebuggable.
- **"Hydrafusion is here!" (brief)** — tools: None. · skill: None — pointer.
- **"I've got some bad news…" (brief)** — tools: None. · skill: None — stub.

## Tools & APIs (11 items)

- **public-apis: free APIs for everything** — tools: [public-apis/public-apis](https://github.com/public-apis/public-apis) · skill: API-first data sourcing — check the free directory before building scrapers or buying tiers.
- **Three voice AI apps that beat typing** — tools: WhisperFlow, SuperWhisper, Voice Inc (open source) · skill: Voice-first capture — dictate-then-polish for anything long-form; default to local processing where privacy matters.
- **A real AI agent in 44 lines, running entirely locally** — tools: [huggingface/smolagents](https://github.com/huggingface/smolagents), Qwen3 30B (open weights) · skill: Local-agent baseline — before reaching for a cloud agent, check what smolagents + an open model + two tools can already do.
- **Fellou: the agentic browser** — tools: Fellou (agentic browser) · skill: API-less automation assessment — for sites with no API, agentic browsers are the answer; vet them on credential security and audit trails first.
- **Showcase AI work on Hugging Face Spaces** — tools: Hugging Face Spaces (huggingface.co/spaces) · skill: Demo-driven distribution — publish an interactive Space with every significant AI project, not just the code.
- **Debug Visualizer: see your data structures inside VS Code** — tools: Debug Visualizer (VS Code extension; no URL in post text) · skill: Visualize data structures during debugging instead of reading raw dumps, especially when reviewing agent-written code.
- **Link collection: skill evaluation and agent infrastructure** — tools: NVIDIA SkillEvaluator — github.com/NVIDIA/skillev… (display truncated in source); microsoft.github.io/waza/; Harbor framework — github.com/harbor-framewo… (display truncated in source); microsoft.github.io/apm/; github.com/marketplace/re… (display truncated in source) · skill: Pair every skill library with an evaluation framework so skills stay trustworthy as they accumulate.
- **Alibaba open-sourced its production code reviewer** — tools: None linked in post text (repo link not in visible text — see permalink). · skill: Study production-hardened open-source reviewers before building your own review automation.
- **Second batch (Aug 24 – Sep 12)**
- **Every PR ships with an interactive walkthrough — open-sourced** — tools: github.com/coldteadotai/pr-walkthrough · skill: Make interactive PR walkthroughs the team standard; generate them with agents.
- **The agentic setup that ships faster than 99% of devs (brief)** — tools: None linked in post text. · skill: Invest in the setup; velocity compounds from the harness.

## Learn AI (11 items)

- **Build a Second Brain on graph fundamentals** — tools: Obsidian (graph view), markdown; Clief Notes community (link in bio) · skill: Graph-first knowledge design — model your domain as nodes (nouns) and edges (verbs) in markdown before involving any AI.
- **Eight AI projects that teach more than college** — tools: ChatGPT (custom GPTs), Lovable.dev (lovable.dev), Bolt.new (bolt.new) · skill: Project-based onboarding — learn AI tooling by shipping eight increasingly-integrated builds, not by watching tutorials.
- **Free AI automation tutorials: N8N, Make, Voiceflow** — tools: N8N (n8n.io), Make.com (make.com), Voiceflow (voiceflow.com); YouTube tutorials (links in the reel) · skill: Tutorial-then-implement — use the free N8N/Make/Voiceflow tutorials as the conceptual base, then build the repo's automation patterns for real.
- **What fine-tuning actually updates inside the model** — tools: None linked in post text. · skill: Learn what fine-tuning actually updates inside the model before spending budget on it.
- **The senior engineer death spiral** — tools: None linked in post text. Essay — sunilpai.dev/posts/the-seni… (display truncated in source) · skill: Study how senior engineers stay leveraged (not hollowed out) as agents absorb more of the work.
- **Load-testing a system design in a simulator** — tools: None linked in post text. · skill: Validate system designs by simulating target load, not just whiteboarding the architecture.
- **Second batch (Aug 24 – Sep 12)**
- **Kiro's manifesto: frontier engineering for AI-tool developers** — tools: kiro.dev · skill: Name your engineering discipline for AI-assisted work; vague unease becomes improvable practice once it's specified.
- **Uber published what its agents actually cost** — tools: None linked in post text. · skill: Benchmark your agent program against published at-scale numbers (Uber: 70%+ agent PRs); cost-per-PR is the metric.
- **"Software Factories" — the emerging-architecture article** — tools: None linked in post text. · skill: Track the software-factory category as it consolidates; reference architectures are emerging now.
- **Running a Software Factory Efficiently at Uber Scale** — tools: None linked in post text. · skill: Map Uber's factory phases to your rollout; treat their efficiency work as the peer benchmark.

## AI Engineer talk notes (37)

- **Talk Notes: "Lessons from Generating 12 Trillion Synthetic Tokens" — Bogdan Gaza, DatologyAI** — `ai-engineer-talks/12-trillion-synthetic-tokens.md`
- **Talk Notes: "How We Built an Agent That Improves Itself" — Zubin Aysola, Weights & Biases** — `ai-engineer-talks/agent-that-improves-itself.md`
- **Talk Notes: "Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough" — Vlad Luzin, Band** — `ai-engineer-talks/agents-solitary-confinement.md`
- **Talk Notes: "AI-Generated Code Is Already Competing With Human Code" — Daksh Gupta, Greptile** — `ai-engineer-talks/ai-code-competing-human.md`
- **Talk Notes: "An AI Research Agent That Runs Your Experiments" — Tim Sweeney, Weights & Biases** — `ai-engineer-talks/ai-research-agent-experiments.md`
- **Talk Notes: "Autoresearch Made Our Models 3x Faster" — Tejas Bhakta, Morph** — `ai-engineer-talks/autoresearch-3x-faster.md`
- **Talk Notes: "Why 99% Accurate Browser Agents Still Fail" — Derek Meegan, Browserbase** — `ai-engineer-talks/browser-agents-99-percent.md`
- **Talk Notes: "The Chief AI Officer: Scientist, Architect, Coach" — Rania Khalaf, WSO2** — `ai-engineer-talks/chief-ai-officer.md`
- **Talk Notes: "We Let Claude Code and Codex Race Human Researchers" — Elie Bakouch, Prime Intellect** — `ai-engineer-talks/claude-code-codex-race.md`
- **Talk Notes: "Your Coding Agent Is 6 Months Out of Date" — Jakub Hojsan, Exa** — `ai-engineer-talks/coding-agent-out-of-date.md`
- **Talk Notes: "I Turned Coding Agents Into a Strategy Game" — Ido Salomon, AgentCraft** — `ai-engineer-talks/coding-agents-strategy-game.md`
- **Talk Notes: "The Death of the Code Review: What the Data Actually Says" — Laurie Voss, Arize AI** — `ai-engineer-talks/death-of-code-review.md`
- **Talk Notes: "Fixing the PR Bottleneck" — Matt Pocock, AIHero** — `ai-engineer-talks/fixing-pr-bottleneck.md`
- **Talk Notes: "Beating RL With Reflection: GEPA and Optimize Anything" — Lakshya A. Agrawal, GEPA** — `ai-engineer-talks/gepa-optimize-anything.md`
- **Talk Notes: "Get Out of the Model's Way" — Kevin Hou, Google Antigravity** — `ai-engineer-talks/get-out-of-models-way.md`
- **Talk Notes: "GLM-5.2: Open Weights, Near-Frontier Intelligence" — Zixuan Li, Z.ai** — `ai-engineer-talks/glm-5-2-open-weights.md`
- **Talk Notes: "Stop Rationing Tokens: Let the Harness Pick the Model" — Žilvinas Urbonas & Laurent Gil, Cast AI** — `ai-engineer-talks/harness-picks-model.md`
- **Talk Notes: "An Interaction Is All You Need" — Ivan Leo, Google DeepMind** — `ai-engineer-talks/interaction-is-all-you-need.md`
- **Talk Notes: "Your LLM App Returned 200 OK. It Was Still Wrong." — Marina Petzel, Datadog** — `ai-engineer-talks/llm-app-200-ok-wrong.md`
- **Talk Notes: "Long-Horizon Agents Need Experiments, Not Just Prompts" — Erina Karati, Supercell** — `ai-engineer-talks/long-horizon-agents-experiments.md`
- **Talk Notes: "The Loop Is the Product" — Roland Gavrilescu, Introspection** — `ai-engineer-talks/loop-is-the-product.md`
- **Talk Notes: "MCP Doesn't Suck. Your Agent Does." — Jan Čurn, Apify** — `ai-engineer-talks/mcp-doesnt-suck.md`
- **Talk Notes: "No, That's Not a Software Factory" — Ryan Cooke, WorkOS** — `ai-engineer-talks/not-a-software-factory.md`
- **Talk Notes: "What Makes Open Models Fast in Production" — Sujee Maniyam, Nebius** — `ai-engineer-talks/open-models-fast-production.md`
- **Talk Notes: "Orchestras, Not Factories: How the Fastest Builders Work" — Charlie Holtz, Conductor** — `ai-engineer-talks/orchestras-not-factories.md`
- **Talk Notes: "I Built a Personal AI Agent on a Raspberry Pi" — Jeremy Adams, Neo4j** — `ai-engineer-talks/raspberry-pi-agent.md`
- **Talk Notes: "Scale the Judgment, Not the Model" — Andrew Orobator, Reddit** — `ai-engineer-talks/scale-the-judgment.md`
- **Talk Notes: "The 5 Levels of Self-Driving Production" — Eric Schwartz, Traversal** — `ai-engineer-talks/self-driving-production.md`
- **Talk Notes: "GPU Died. Training Didn't: Self-Healing Training at Scale" — Connor Guerrero & Young Jeong, Crusoe** — `ai-engineer-talks/self-healing-training.md`
- **Talk Notes: "Building Self-Improving Agent Software Factories" — Suraj Gupta, Warp** — `ai-engineer-talks/self-improving-factories.md`
- **Talk Notes: "The State of AI in Software Development: Data from 400+ Orgs" — Justin Reock, DX** — `ai-engineer-talks/state-of-ai-dev-400-orgs.md`
- **Talk Notes: "Stop Fine-Tuning to Fix Retrieval Problems" — Anant Srivastava** — `ai-engineer-talks/stop-fine-tuning-retrieval.md`
- **Talk Notes: "Stop Renting Your AI's Memory" — Dylan Couzon, Qdrant** — `ai-engineer-talks/stop-renting-memory.md`
- **Talk Notes: "How VS Code Went from Monthly to Weekly Releases with AI" — Harald Kirschner** — `ai-engineer-talks/vscode-weekly-releases.md`
- **Talk Notes: "What It Actually Takes to Build a Software Factory" — Tereza Tížková, Factory** — `ai-engineer-talks/what-it-takes-software-factory.md`
- **Talk Notes: "Why AI Didn't Actually Make You Ship Faster" — Gabriel Spencer-Harper, Meticulous** — `ai-engineer-talks/why-ai-didnt-ship-faster.md`
- **Talk Notes: "YOLO Mode, Safely: MicroVM Sandboxes for Any Agent" — Rowan Christmas, Docker** — `ai-engineer-talks/yolo-mode-microvm-sandboxes.md`

## Deep dives (12)

- **Anthropic: Reducing cost and improving performance with Claude Platform** — `deep-dives/claude-cost-optimization.md`
- **Deep Dive: "Dashboards Are Dead" — Sarah Simionescu, Composio** — `deep-dives/dashboards-are-dead.md`
- **GitHub: How we make AI coding more cost efficient** — `deep-dives/github-cost-efficiency.md`
- **Jev model router for Claude Code** — `deep-dives/jev-model-router.md`
- **The Jev thesis — TypeSafe's System One Models** — `deep-dives/jev-thesis.md`
- **jevgrep — Jev-powered code research CLI** — `deep-dives/jevgrep.md`
- **show-me — the visual-explanation skill** — `deep-dives/show-me-skill.md`
- **Spotify's shunt — routing agent I/O to cheap models** — `deep-dives/spotify-shunt.md`
- **Tangle — Shopify's open-source experimentation platform** — `deep-dives/tangleml.md`
- **Tokenomics Deep Dive: what AI-assisted engineering actually costs, and how to cut it** — `deep-dives/tokenomics-deep-dive.md`
- **Uber: Running a Software Factory Efficiently at Uber Scale** — `deep-dives/uber-software-factory.md`
- **Unreal Agent — async-first agent harness** — `deep-dives/unreal-agent.md`

## Cross-cutting

- **COMBINED.md** — recurring patterns across all reels + highest-leverage moves for tokenomics/context-management
- **tokenomics-playbook.md** — 5 ranked cost levers + open-source toolstack + Copilot billing reality + local CLI complements
- **setups/** — reusable project setups
- **templates/** — skill-card, skill-compare, project-setup templates

_Total indexed: 137 distilled items + 37 talk notes + 12 deep dives + patterns + playbooks._