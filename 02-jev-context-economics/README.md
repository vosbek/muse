# 02 — Jev Context Economics

**Thesis:** The cheapest token is the one you never spend. These three reels form a coherent economic argument: small models should make the decisions, retrieval should happen before reasoning, and the whole LLM-centric cost structure is transitional. The Jev pattern (a tiny model deciding, a big model executing) and jevgrep's measured 30% cost cut are the deployable present; the SLM prediction is the direction of travel.

### jevgrep: cut coding-agent cost ~30% with better file retrieval
- **Creator:** @gittrend.io · **Date:** 2026-09-29
- **What it suggests:** jevgrep is an open-source tool that converts a plain-English repository question into targeted searches, returning the exact lines an AI coding agent needs — instead of the agent dumping whole files or directory trees into context to find them. The reel walks through the GitHub README (install via `npm install -g @dshng/jevgrep`, requires Node.js 22+, macOS/Linux, a Vercel AI Gateway key; usage like `jg auth` and `jg "How are telemetry events recorded and sent?"`, plus an installable agent skill). The money slide is the benchmark: on a ten-task SWE-bench test, jevgrep solved the same 8 of 10 tasks as the baseline but cut the bill from $7.62 to $5.44 — a 28.6% reduction. The principle generalizes beyond code: every agent workflow has a "finding" step and a "thinking" step, and most teams overpay on the first. Fix retrieval before you touch the model.
- **Repos/tools:** [dshng/jevgrep](https://github.com/dshng/jevgrep) (npm: `@dshng/jevgrep`)
- **Extractable skill:** Retrieval-first cost control — instrument $/task, then optimize the finding step (targeted search returning exact lines) before upgrading models.
- **Source:** https://www.instagram.com/reel/Dd5Z0k1FLO6/

### Jev: choose MCP tools without polluting the main context
- **Creator:** @superlinear_fm · **Date:** 2026-09-29
- **What it suggests:** An emerging practice for coding agents: instead of handing the main session every available MCP tool (plus skills and other tools) — which bloats context with tool schemas and selection chatter — you spin up a separate decision model called "Jev" with its own context. Jev gets the project context, the current step, and the full tool menu; it picks the right tool in isolation; only the chosen answer is injected back into the main prompt. The main context window never sees the deliberation. This is the architectural version of "don't think out loud in the expensive room" — a cheap, narrow model absorbs the selection cost, and the frontier model only ever receives decisions. It applies anywhere a powerful agent faces a large action space: tool routing, model routing, triage.
- **Repos/tools:** MCP servers (pattern-level; no single repo)
- **Extractable skill:** Decision-model isolation — route every selection problem (tools, models, next actions) through a small model in its own context; inject only outcomes into the main session.
- **Source:** https://www.instagram.com/reel/Dd4DznsjPmW/

### SLMs will replace LLMs — because the economics demand it
- **Creator:** @gojutechtalk · **Date:** 2026-08-23
- **What it suggests:** Justin Goju Gottschlich (Stanford CS adjunct) states he's never been more confident about a technology prediction: small language models will replace large ones, and the biggest reason is economic — running AI systems in LLM form is "not fiscally reasonable." The argument isn't that SLMs are smarter; it's that most deployed AI work (classification, routing, extraction, simple agents, on-device assistance) doesn't need frontier intelligence, and the cost gap makes the current LLM-default architecture unsustainable at scale. For anyone planning infrastructure, the implication is to design for a two-tier world now: route the long tail of narrow tasks to small/cheap/local models, and reserve frontier calls for the shrinking set of problems that measurably need them.
- **Repos/tools:** None (prediction/thesis)
- **Extractable skill:** Two-tier model strategy — default narrow work to SLMs; require evidence (not habit) before spending frontier tokens.
- **Source:** https://www.instagram.com/reel/DcY6Er0iuwy/

### 9 ways to cut the LLM bill — it's an architecture problem, not a model problem
- **Creator:** @hackproduct · **Date:** 2026-10-01
- **What it suggests:** A merged checklist of 9 cost tactics (from 15): route by difficulty (tools first, small model next, big model only when needed); trim context (summarize old turns, drop irrelevant history); retrieve don't stuff (RAG sends a few chunks, not every document); prompt caching (pay a fraction for a long fixed prefix); semantic answer caching (skip the call entirely on near-duplicate questions); lean outputs (cap max_tokens, ask for JSON not essays); batch APIs (~half price for non-urgent work); agent guardrails (cap iterations, tool calls, tokens so one runaway loop can't burn the budget); track cost per request and per feature daily. The two lines most people miss: output tokens usually cost several times input tokens, and agents multiply every call — the cheapest token is the one you never generate. Every tactic maps onto this folder's existing entries (Jev routing, jevgrep retrieval-first, two-tier model strategy) and onto the tokenomics playbook's levers.
- **Repos/tools:** None (checklist; batch APIs and caching are provider features).
- **Extractable skill:** Bill-first architecture review — measure the biggest line on the bill (cost per request/feature), then apply routing, caching, and guardrails before touching model choice.
- **Source:** https://www.instagram.com/p/Dd-Y4rZOSn3/

## From X bookmarks (Sep 2026)
Distilled from Matt's X bookmarks, newest first. Full post text at each permalink (X truncates long posts in timelines).

### Open-source adapter that decouples your agent from any single LLM provider
- **Creator:** @EGafni · **Date:** 2026-09-27
- **What it suggests:** TypeSafe AI released an open-source adapter that lets GPT, Claude, and Gemini slot into the same agent pipeline interchangeably — the reply notes many teams would otherwise rebuild the same glue code repeatedly. This is a provider-swap layer: one interface, multiple frontier models underneath. For context economics, the point is that the routing/decision layer should be decoupled from the generation provider, so you can chase the cheapest or best model per call without rewriting integration code. The post text is short and complete; technical details live in the repo and attached images — full text at permalink.
- **Repos/tools:** None linked in post text (TypeSafe AI / @typesafeai mentioned).
- **Extractable skill:** Decouple your routing layer from your generation provider so models become swappable commodities.
- **Source:** https://x.com/EGafni/status/2104356000237228139

### A research-agent CLI claiming 40% lower coding-agent cost on SWE-bench
- **Creator:** @dzhng · **Date:** 2026-09-26
- **What it suggests:** Introduces jevgrep, a research agent CLI built on Jev from TypeSafe AI (@typesafeai). The headline claim: it reduces coding agent cost by 40%, verified on SWE-bench — a standardized coding benchmark, not a vibes-based number. The visible text cuts off mid-sentence, so the setup instructions and what the built-in shortcut refers to are only at the permalink. What can be verified: this is a concrete Jev-powered tool aimed at the research-loop pattern (search, investigate, act), and its value proposition is cost-per-task reduction on a recognized benchmark. For anyone building coding agents, the pattern is to put a cheap decision model in front of expensive generation and measure on SWE-bench rather than eyeballing savings.
- **Repos/tools:** jevgrep — github.com/dzhng/jevgrep
- **Extractable skill:** Put a cheap decision model in front of your coding agent's research loop and measure cost-per-task on SWE-bench.
- **Source:** https://x.com/dzhng/status/2103920741481848861

### The Jev founder's 12-page guide to pairing Jev with LLMs
- **Creator:** @hanakoxbt · **Date:** 2026-09-25
- **What it suggests:** Diogo Almeida, Jev's founder, released a 12-page PDF on using Jev alongside LLMs — positioned as a practical complement to the poster's own Jev Engineering course on not overpaying for yes-or-no decisions with frontier models. The visible text truncates early, so the PDF's actual techniques aren't visible in the timeline; what is verifiable is the framing: Jev is a decision-model layer you pair with general LLMs, and the founder's own guide is the authoritative reference for that pairing pattern. The core idea running through this whole collection is that binary and classification decisions should never be routed through an expensive autoregressive model. Full techniques at the permalink.
- **Repos/tools:** None linked in post text (PDF location not in visible text).
- **Extractable skill:** Route binary and classification decisions to a cheap decision model, never to a frontier autoregressive model.
- **Source:** https://x.com/hanakoxbt/status/2103492182053199992

### System One models: the ultra-fast decision-model wave
- **Creator:** @omarsar0 · **Date:** 2026-09-24
- **What it suggests:** Flags a new wave of System One models for anyone building custom agent harnesses, spotlighting CLM (Contrastive Language Model) — described as an ultra-fast System One model trained with a contrastive objective (text truncates). The System One framing is the key concept: fast, cheap, intuitive decision-making models as opposed to slow deliberative generation. For harness builders, the takeaway is to watch this model class for the routing, classification, and gating layers of agents, where latency and cost dominate. The quoted video presumably explains CLM's training; details beyond the teaser are at the permalink.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Use System One–style fast decision models for harness routing and gating layers where latency dominates.
- **Source:** https://x.com/omarsar0/status/2103139055013646646

### Pairing Jev with Opus 5.5 in a builder's agentic harness
- **Creator:** @Av1dlive · **Date:** 2026-09-24
- **What it suggests:** Expresses strong enthusiasm for combining Jev with Opus 5.5 in a personal workflow, quoting the author's own builder's guide to agentic harnesses with Jev plus a demo video. The visible text truncates, so the specific architecture isn't visible in the timeline. Verifiable: the pattern pairs a cheap decision model (Jev) with a strong frontier model (Opus 5.5) as a division of labor — Jev decides, the frontier model executes. This is the canonical Jev harness pattern echoed across this collection: keep the expensive model off the decision loop. Full setup at the permalink.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Split your harness: cheap decision model decides, frontier model executes.
- **Source:** https://x.com/Av1dlive/status/2103190313624039620

### The Jev setup guide for maximum quality at minimum cost
- **Creator:** @0x_rody · **Date:** 2026-09-22
- **What it suggests:** Notes Jev's exploding popularity and points at a Sep 19 setup guide promising maximum quality for minimum cost with the exact config inside. The visible text truncates, so the config itself is only at the permalink. Verifiable: the cost-quality frontier is the active conversation — people aren't just adopting Jev, they're tuning configs to hold quality while pushing cost down. For a tokenomics lens, the interesting bit is that the community is already treating model configuration as an optimization problem with shared, exact configs rather than defaults.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Treat your model config as a cost-quality optimization problem and share exact configs, not vibes.
- **Source:** https://x.com/0x_rody/status/2102403963865759871

### Using Jev at ticket creation to prompt for missing follow-up questions
- **Creator:** @peterramsing · **Date:** 2026-09-22
- **What it suggests:** Describes a concrete production pattern: when people create tickets, Jev is used to prompt for the follow-up questions the reporter should have answered in the ticket body. The visible text truncates, so the exact prompt mechanics are at the permalink. Verifiable: this is a real workflow deployment of a cheap decision/classification model at an intake funnel — structured-data extraction and gap detection, not generation. It's one of the clearest System One use cases in the collection: fast, cheap, and run on every single ticket without worrying about per-call cost.
- **Repos/tools:** None linked in post text (@typesafeai mentioned).
- **Extractable skill:** Deploy cheap decision models at intake funnels to detect missing information before humans touch the ticket.
- **Source:** https://x.com/peterramsing/status/2102413095037808667

### 20 must-use Jev skills for agent setups
- **Creator:** @FareaNFts · **Date:** 2026-09-22
- **What it suggests:** Lists 20 must-use Jev skills for agent setups; the visible portion names three: a browser-agent skill, a fast context-compaction skill, and a generative-UI skill (json-render). The post quotes the author's own article claiming to cut agent bills 400x with Jev across 20 real use cases; the full list and article are at the permalink since the timeline text truncates after the third skill. Verifiable: skills are emerging as the packaging format for Jev capabilities — reusable, composable decision-model behaviors (browse, compact, render UI) that drop into agent setups. The two visible skill repos are the concrete artifacts to inspect.
- **Repos/tools:** jev-ultrafast (browser agent) — github.com/browser-use/je… (display truncated in source); fast-jev-compaction (context compression) — github.com/tamaratran/fas… (display truncated in source)
- **Extractable skill:** Package decision-model capabilities as reusable skills (browse, compact, render) instead of one-off prompts.
- **Source:** https://x.com/FareaNFts/status/2102386737192607894

### A PDF on building a Jev harness for coding agents
- **Creator:** @zodchiii · **Date:** 2026-09-22
- **What it suggests:** Announces that Jev's founder released a PDF on building a Jev harness specifically for coding agents, quoting the author's own Sep 19 setup guide on maximum quality for minimum cost. The visible text truncates, so the harness architecture details live at the permalink. Verifiable: the founder is publishing first-party harness-building guidance aimed at the coding-agent use case — the highest-spend agent workload — which signals where the cost-reduction story is sharpest. Combined with the jevgrep post above, the pattern is converging: Jev as the decision layer in front of expensive coding models.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Build your coding-agent harness with a cheap decision layer in front of the expensive generation model.
- **Source:** https://x.com/zodchiii/status/2102377493705740417

### Jev makes agent evals dramatically cheaper
- **Creator:** @_avichawla · **Date:** 2026-09-21
- **What it suggests:** Highlights an under-appreciated Jev use case: evaluation. Jev makes it dramatically cheaper to evaluate what actually happened in agent runs, and the post quotes the author's own article on building a fully local Jev. The text truncates, so the eval methodology is at the permalink. Verifiable: eval is a huge hidden token cost — every trajectory judged by a frontier model multiplies spend — and a cheap local decision model turns eval from a luxury into something you run continuously. For tokenomics, this is a first-order move: make the measurement loop cheap and local.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Run your agent evals on a cheap local decision model so measurement costs approach zero.
- **Source:** https://x.com/_avichawla/status/2101966536798040332

### Jev as an industry-scale moment, with a 10-step setup roadmap
- **Creator:** @0xCodila · **Date:** 2026-09-18
- **What it suggests:** Frames Jev as an industry-scale moment — it tells agents and LLMs what to do next (text truncates) — and links a full 10-step roadmap article for setting up a new AI control layer from scratch. Verifiable: the "what to do next" framing positions Jev as the control plane for agents rather than a chat model: the thing that decides the next action. The 10-step roadmap is the practical artifact; the article is at the permalink. The moment-analogy is hype, but the control-plane framing is the useful mental model for harness design.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Treat the decision model as your agent's control plane: its job is choosing the next action.
- **Source:** https://x.com/0xCodila/status/2100984487802708306

### SimpleJev: open-weights decision models with vision, classifying 1,697 events
- **Creator:** @LLMJunky · **Date:** 2026-09-19
- **What it suggests:** Spotlights Richelle's SimpleJev, which turns any open-weight model into a structured classifier — now with open weights plus vision. The concrete proof point: 1,697 SF Tech Week events classified with Gemma 4 26B-A4B. This matters because it shows the Jev pattern (cheap structured decision-making) doesn't require the proprietary Jev API — open-weight models can be shaped into the same role, which is exactly the local-first direction that matters here. The post also quotes a reply anticipating other dev teams will copy and open-source Jev, underscoring how fast this space is commoditizing.
- **Repos/tools:** None linked in post text (SimpleJev by @Richelle_Ji).
- **Extractable skill:** Shape open-weight models into structured classifiers instead of renting the decision layer from an API.
- **Source:** https://x.com/LLMJunky/status/2101209063602155974

### Third-party demo: instant generative UI from json-render plus Jev
- **Creator:** @rauchg · **Date:** 2026-09-18
- **What it suggests:** Announces that Jev-driven generative UI has been achieved by a third party, quoting an experiment combining json-render with Jev: generative UI that feels instant, using the developer's own components and actions, with a demo video. Verifiable: someone got Jev driving UI rendering decisions fast enough to feel instant — the decision model picks components and actions, and structured JSON output becomes the interface between model and frontend. This is a concrete instance of the skill-packaging trend (json-render appears in the 20-skills post too): decision models emitting structured UI specs at near-zero latency.
- **Repos/tools:** json-render (generative UI skill mentioned; no URL in post text)
- **Extractable skill:** Have decision models emit structured UI specs (JSON) instead of rendered text for instant generative interfaces.
- **Source:** https://x.com/rauchg/status/2101032024635249069

### Jev cloned 3 days after launch: the model is not the moat
- **Creator:** @ziwenxu_ · **Date:** 2026-09-19
- **What it suggests:** Notes that Jev was built quietly for years, then cloned and open-sourced 3 days after launch — the product alone is no longer the moat (text truncates). The post quotes the CUA-S1 announcement: a family of small, specialized System One models for computer use, with a repo link. Verifiable: the decision-model category is commoditizing at extreme speed; defensibility is shifting from the model artifact to distribution, harness integration, and data. For enterprise planning, the lesson is to build on the pattern (cheap decision layers), not on any single vendor's model.
- **Repos/tools:** CUA-S1 — github.com/trycua/cua
- **Extractable skill:** Build on the cheap-decision-layer pattern, not on any single vendor's model, because clones arrive in days.
- **Source:** https://x.com/ziwenxu_/status/2101331645974655216

### Jev's pricing hook: cents per million input tokens
- **Creator:** @typesafeai · **Date:** 2026-09-19
- **What it suggests:** The official TypeSafe AI account amplifies a user's price comparison: a short phrase's worth of tokens at $0.042 per million input tokens — i.e., the Jev decision layer costs a few cents per million tokens, orders of magnitude below frontier generation pricing. This is the sharpest tokenomics data point in the collection: it quantifies exactly why the decision/generation split pays. The post is short and complete. Caveat: the quoted figure is a user's claim amplified by the vendor, not an independent benchmark — treat it as a directional pricing signal and verify against current Jev pricing before budgeting.
- **Repos/tools:** None (pricing signal, not a tool).
- **Extractable skill:** Price your decision layer separately from your generation layer; cents-per-million changes what you can afford to run on every call.
- **Source:** https://x.com/typesafeai/status/2101445845212365129

### Three-layer agent architecture: deterministic filters first
- **Creator:** @CD65594 · **Date:** 2026-09-19
- **What it suggests:** A reply proposing a 3-layer agent architecture, starting with a deterministic programmatic layer that filters for jurisdiction (the visible text truncates there). What can be verified: the architectural stance is that the first layer should be deterministic code, not a model — programmatic filters handle the crisp, rule-based gates, with model layers above only seeing what survives. This is a cost and reliability principle: never pay a model to enforce a rule you can express in code. The remaining layers are at the permalink.
- **Repos/tools:** None (architecture take).
- **Extractable skill:** Put deterministic programmatic filters first; only spend model calls on what survives the rules.
- **Source:** https://x.com/CD65594/status/2101355348946792930

### A Jev model router mod for Claude Code via AI Gateway
- **Creator:** @dani_avila7 · **Date:** 2026-09-19
- **What it suggests:** Introduces a Jev model router mod for Claude Code that lets the tool use Jev through a direct connection (text truncates), mentioning Vercel's AI Gateway. Verifiable: this is a routing layer that brings Jev's cheap decision-making into the Claude Code workflow via a gateway, so the harness can split traffic between decision calls and generation calls. The demo video shows it working; exact wiring is at the permalink. The strategic point: routers are where the tokenomics get implemented — the mod is the mechanism that decides which call goes to the cents-per-million model.
- **Repos/tools:** None linked in post text (@typesafeai and @vercel AI Gateway mentioned).
- **Extractable skill:** Implement your cost split in the router: route decision calls to the cheap model, generation calls to the frontier model.
- **Source:** https://x.com/dani_avila7/status/2101176629745561686

### LLMs vs. Jev, clearly explained
- **Creator:** @akshay_pachaar · **Date:** 2026-09-19
- **What it suggests:** An explainer post with the TL;DR that the key difference is not that Jev generates faster — the sentence truncates there. The post quotes the author's own clearly-explained article with a demo video. What can be verified: the framing pushes back on the speed narrative; the real distinction is architectural (decision vs. generation), not throughput. That distinction matters for how you design harnesses: you don't adopt Jev to make the same calls faster, you adopt it to make different, cheaper calls for the decision-shaped parts of the workload. Full explanation at the permalink.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Adopt decision models for decision-shaped work, not as a faster drop-in for generation.
- **Source:** https://x.com/akshay_pachaar/status/2101309966156712025

### An open-source Jev clone that already outperforms it
- **Creator:** @jun_song · **Date:** 2026-09-19
- **What it suggests:** Reports that an OpenAI co-founder spent 3 years quietly building Jev, only for an open-source clone to arrive that already performs better — quoting a translated post about "Laya," an open-source Jev rival, with a Hugging Face link and an image. The text truncates, so benchmark details are at the permalink. Verifiable: the Jev category is being replicated in the open within days of launch, with community builds claiming superiority. For local-first strategy, this is the post to watch — an open clone that beats the original removes the last reason to rent the decision layer.
- **Repos/tools:** Laya (open-source Jev-class model) — huggingface.co/convaiinnovati… (display truncated in source)
- **Extractable skill:** Track open clones of decision models; the best local-first option may already beat the API version.
- **Source:** https://x.com/jun_song/status/2101246204143366425

### If you're confused about Jev, study this harness article
- **Creator:** @AIGuide_ · **Date:** 2026-09-18
- **What it suggests:** A straightforward pointer: anyone confused about Jev should study a Sep 17 article on building a harness with Jev — described as fully worth the time. The post is short and complete; the substance is in the linked article at the permalink. Verifiable: within days of Jev's launch, the community converged on this article as the canonical explainer for harness builders. For the playbook, the action is to read the primary source (the article) rather than the commentary — it's the reference the practitioners themselves point to.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** When a new model class lands, find the practitioner's canonical explainer and study it before the commentary.
- **Source:** https://x.com/AIGuide_/status/2101119480361361685

### Bespoke Nimble: fully open 9B decision model with open data and recipe
- **Creator:** @AlexGDimakis · **Date:** 2026-09-18
- **What it suggests:** Announces Bespoke Nimble via a conference post: a fully open Jev-class model — open data, open weights, open training recipe — with the GitHub repo and Hugging Face links, framed with the joke that the CEO disappeared for two days and came back with a 9B model. Verifiable: this is a completely open decision model (data, weights, recipe), which is the strongest possible artifact for local-first deployment — you can inspect, reproduce, and run the decision layer yourself. The 9B size suggests it fits on serious local hardware. This is the open alternative to renting a decision-model API.
- **Repos/tools:** Bespoke Nimble — github.com/bespokelabsai/… (display truncated in source); huggingface.co/bespokelabs/Be… (display truncated in source)
- **Extractable skill:** Prefer open-data, open-recipe decision models when you need to audit, reproduce, or self-host the decision layer.
- **Source:** https://x.com/AlexGDimakis/status/2101129473794175138

### CUA's 2.8MB model: System One models go tiny
- **Creator:** @Layton_Gott · **Date:** 2026-09-18
- **What it suggests:** Marvels that a day after predicting Jev would open many doors, CUA shipped a 2.8MB model — quoting the CUA-S1 announcement of small, specialized System One models for computer use. The text truncates, so architecture details are at the permalink. Verifiable: 2.8MB is the striking number — a decision model small enough to embed anywhere, which reframes what's possible: classification and routing decisions running on-device, in the browser, or at the edge with negligible cost. This is the extreme end of the tokenomics curve: when the decision model is megabytes, per-decision cost effectively vanishes.
- **Repos/tools:** CUA-S1 — github.com/trycua/cua
- **Extractable skill:** Push tiny decision models to the edge; at megabyte scale, per-decision cost effectively vanishes.
- **Source:** https://x.com/Layton_Gott/status/2101031818413650111

### The one-line definition: decisions, not generation
- **Creator:** @matthewcanham · **Date:** 2026-09-18
- **What it suggests:** States the core definitional claim — Jev is a new model type built for making decisions rather than generating text — quoting the canonical harness article. The text truncates, so the elaboration is at the permalink. Verifiable: this is the cleanest one-line mental model in the collection — decision-optimized vs. generation-optimized — and it determines everything downstream: training objectives, eval metrics, pricing, and where the model sits in a harness. If you internalize one sentence about Jev, it's this one.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Classify every model call in your harness as decision-shaped or generation-shaped, then match the model to the shape.
- **Source:** https://x.com/matthewcanham/status/2101098949205713304

### Jev as a literal if statement
- **Creator:** @southpolesteve · **Date:** 2026-09-17
- **What it suggests:** Plays on the popular description of Jev as an "AI if statement" and takes it literally — with a link to a live demo on Cloudflare Workers and an image. The post text is complete. Verifiable: the provocation is that decision models collapse the distance between natural-language intent and programmatic control flow — a Jev call starts to look like a conditional branch in code rather than a chat completion. The linked demo presumably shows this concretely. For harness design, the mental model is powerful: treat decision-model calls as control flow, with the same expectations of speed, cheapness, and reliability as an if statement.
- **Repos/tools:** Demo — bably-lang.southpolesteve.workers.dev
- **Extractable skill:** Treat decision-model calls as control flow (if statements), not as chat completions.
- **Source:** https://x.com/southpolesteve/status/2100767781868150938

### The 45-second Jev explainer practitioners converged on
- **Creator:** @hot_town · **Date:** 2026-09-17
- **What it suggests:** Endorses a 45-second TL;DR video as the clearest Jev explainer available. The post is short and complete; the substance is the quoted video at the permalink. Verifiable: in a week flooded with Jev explainers, practitioners converged on this 45-second video as the clearest articulation — which itself says something about the idea's simplicity. For onboarding a team to the decision-model pattern, this is the recommended starting artifact: 45 seconds before the 12-page PDFs.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Onboard teams to a new model pattern with the shortest clear explainer first, depth later.
- **Source:** https://x.com/hot_town/status/2100459012315639944

### A skeptic's take: the simple question behind the Jev launch
- **Creator:** @manthanguptaa · **Date:** 2026-09-17
- **What it suggests:** Calls Jev one of the more interesting recent model launches because it asks a very simple question (text truncates), quoting a 2:56 video. Verifiable: the framing here is that Jev's power comes from asking a simple, well-posed question rather than from scale — the interesting launches reframe the problem. The video presumably contains the founder's argument; details at the permalink. The meta-lesson for the playbook: the most valuable model advances may come from better problem decomposition (decisions vs. generation) rather than bigger models.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Look for model advances that come from better problem decomposition, not just bigger models.
- **Source:** https://x.com/manthanguptaa/status/2100466984605417923

### Jev for PR review: ~200x cheaper than Claude, half a second
- **Creator:** @isaac_ts_way · **Date:** 2026-09-17
- **What it suggests:** Endorses targeted, fast, cheap code review as the best Jev use case for most developers, quoting a demo where Jev reviewed PRs at roughly 200x lower cost than Claude and answered in half a second. The post text is complete. Verifiable: PR review is decision-shaped work (approve, flag, comment) with clear economics — 200x cheaper and sub-second latency means you can run it on every PR, every push, without budget anxiety. This is the concrete ROI story: not a benchmark, but a deployed workflow with a measured cost multiple.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Run decision-shaped checks (like PR review) on every event once the cost multiple makes it free in practice.
- **Source:** https://x.com/isaac_ts_way/status/2100640617923555754

### jev(): a PostgreSQL extension for natural-language database search
- **Creator:** @iam_zachi · **Date:** 2026-09-17
- **What it suggests:** Shows off a PostgreSQL extension, jev(), that searches an entire database in natural language — with no index and no embeddings (text truncates mid-word). Verifiable: this pushes the decision model down into the database layer itself — a SQL-callable function that turns natural language into structured search over your data without a vector index or embedding pipeline. That's a striking simplification of the RAG-adjacent stack: if the decision model can map language to data directly, the embedding infrastructure becomes optional. Full demo at the permalink.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Consider decision models as a direct natural-language interface to structured data, bypassing embedding pipelines where possible.
- **Source:** https://x.com/iam_zachi/status/2100679300756435135

### A visual explanation of Jev built on Qwen2.5-RLCD
- **Creator:** @NielsRogge · **Date:** 2026-09-16
- **What it suggests:** Shares a visual explanation of how Jev works, built with Claude's help, based on the Qwen2.5-RLCD model released on Hugging Face. The core technical claim visible: replace autoregressive LLM generation with a single Transformer decoder of a pre-trained model (text truncates). Verifiable: this is the most architectural of the explainers — it grounds Jev in a concrete mechanism (single-decoder, non-autoregressive) rather than analogy, and ties it to an actual open model you can inspect. For understanding why Jev is fast and cheap, this is the mechanism-level reference; the full visual is at the permalink.
- **Repos/tools:** Qwen2.5-RLCD (open model on Hugging Face; no URL in post text)
- **Extractable skill:** Ground new model claims in their mechanism (single-decoder, non-autoregressive) before adopting the hype framing.
- **Source:** https://x.com/NielsRogge/status/2100239244501430438

### A 45-second TL;DR that makes Jev's simple core idea click
- **Creator:** @MatijaSosic · **Date:** 2026-09-16
- **What it suggests:** Shares a 45-second TL;DR video on Jev, noting the core idea is beautifully simple but the video made it land (text truncates). The post quotes the founder's 2:56 video as source material. Verifiable: this is the explainer other practitioners converged on as the clearest. The substance is the embedded video at the permalink. The playbook note: when an idea is genuinely simple, the best teaching artifact is short — length here would signal the explainer doesn't understand it yet.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** If an idea is truly simple, teach it in under a minute; length signals the teacher doesn't get it yet.
- **Source:** https://x.com/MatijaSosic/status/2100190746389135772

### The founder's question: why haven't superhuman chat models led to AGI?
- **Creator:** @CompleteSkeptic · **Date:** 2026-09-15
- **What it suggests:** Shares a 2:56 video of Diogo Almeida — described as having co-invented ChatGPT and now founder of Jev — asking why superhuman chat models have not led to AGI. The text truncates, so the argument unfolds in the video at the permalink. Verifiable: this is the philosophical origin story of the whole Jev wave — the claim that scaling chat and generation was the wrong ladder, and that decision-making models are the missing piece. Whether or not you buy the AGI framing, the practical consequence is the same: the industry spent years optimizing generation while the decision layer sat expensive and underexploited.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Question whether you're climbing the right ladder: generation scale vs. decision quality are different games.
- **Source:** https://x.com/CompleteSkeptic/status/2099925682726002904

### Second batch (Aug 24 – Sep 12)

> **Tokenomics callout — the two most cost-relevant posts in this batch.** GitHub and Anthropic both published their cost-efficiency playbooks within days of each other. If you read nothing else here, read these two.

### GitHub: "Using more tokens doesn't always mean better results"
- **Creator:** @github · **Date:** 2026-09-08
- **What it suggests:** GitHub's own post reframes the efficiency metric: the real measure of AI coding efficiency is whether an agent has the context it needs to move work f[orward, truncated] — not token volume. It links the github.blog piece "How we make AI coding more cost efficient without sacrificing task quality." This is the tokenomics thesis stated by the largest code host on earth: context sufficiency per dollar, not tokens per task. The blog presumably details their techniques (the visible text cuts off), but the framing alone is the takeaway for a tokenomics remit — it legitimizes measuring efficiency as outcome-per-token-spend and gives the enterprise program a vendor-published reference point. Read the full blog via the permalink.
- **Repos/tools:** github.blog (How we make AI coding more cost efficient without sacrificing task quality)
- **Extractable skill:** Define efficiency as context-sufficiency per dollar; use GitHub's published framing to anchor the enterprise tokenomics program.
- **Source:** https://x.com/github/status/2097388268237045883

### Claude Platform: cutting cost without cutting quality
- **Creator:** @ClaudeDevs · **Date:** 2026-09-08
- **What it suggests:** Anthropic's article "Reducing cost and improving performance with Claude Platform" — tuning prompt caching, instructions, and effort can reduce Claude's cost without sacrificing applica[tion quality, truncated]. 168 replies, 377 reposts, 4,026 likes — practitioners care about this enormously. The three levers named are the whole enterprise tokenomics playbook in one line: prompt caching (don't pay twice for the same prefix), instructions (shorter, sharper system prompts cost less on every call), and effort (match reasoning effort to task difficulty — the routing thesis). Vendor-published, so it's citable in enterprise docs; the full techniques are at the permalink.
- **Repos/tools:** Claude Platform docs (article link at permalink)
- **Extractable skill:** The big three cost levers — prompt caching, instruction hygiene, effort routing — applied systematically.
- **Source:** https://x.com/ClaudeDevs/status/2097369738968195513

**Deep dives:** [jevgrep](../deep-dives/jevgrep.md) (28.6% measured cut) · [jev-thesis](../deep-dives/jev-thesis.md) (System One Models) · [jev-model-router](../deep-dives/jev-model-router.md) (routing Claude Code with Jev) · [github-cost-efficiency](../deep-dives/github-cost-efficiency.md) (Copilot harness) · [claude-cost-optimization](../deep-dives/claude-cost-optimization.md) (Anthropic's ranked levers) · [context-language-models](../deep-dives/context-language-models.md) (the model edits its own memory).

### Context Language Models: the model edits its own memory
![CLM infographic](context-language-models-infographic.jpg)
- **Creator:** @rakeshgohel01 (infographic) · underlying paper: Rulin Shao et al., UW / Meta Superintelligence Labs / MIT / Trillium Labs · **Date:** 2026-09-29 (paper)
- **What it suggests:** The infographic distills the Sep 2026 "Context Language Models" paper (arXiv:2609.37725): stop treating context as an append-only transcript — mirror it into a file the model can edit directly (rewrite, delete, reorder, compact), synced into the next turn. Four learned behaviors emerge: delete stale results, track live state, rewrite history compactly, and write reusable helper functions for context management. The paper's numbers: +11.4% accuracy with 21.5% fewer FLOPs on BrowseComp-Plus, +5% score with 59% fewer FLOPs on 12-hour EdgeBench-10, and a co-designed Suffix Cache Reuse serving layer (editing breaks prefix caching; SCR reuses the unaffected suffix, −35% server compute vs SGLang). Context management becomes learned model behavior instead of hand-engineered harness rules — and it keeps improving with RL (Qwen3.5-9B: 28.8% → 42.5%).
- **Repos/tools:** https://github.com/facebookresearch/context-language-models (CC BY-NC 4.0) · paper: https://arxiv.org/html/2609.37725v1
- **Extractable skill:** Move context management inside the model: give the agent file-edit tools over its own context plus an evolved (not hand-written) skill doc, and pair it with suffix-aware caching on the serving side.
- **Source:** infographic by @rakeshgohel01 (image above) · paper arXiv:2609.37725

### Stop using an essay-writing AI for yes/no questions: Jev, the "System One" decision model
- **Creator:** @brijkishorepandey (Brij Kishore Pandey) · **Date:** 2026-09-23
- **What it suggests:** The cleanest public explainer of the Jev thesis in this collection. Most AI apps ask a general LLM small questions all day ("is this urgent?", "which team handles this?", "is this command safe?") — the LLM writes a full paragraph and code has to dig the answer out. Slow, expensive, compounding at scale. Jev (TypeSafe AI), named after Kahneman's fast intuitive thinking, doesn't write text — it only makes decisions. The interface: send the text (the "state") plus typed questions; it answers Noul (yes/no), Choice (pick an option), or Score (place on a scale), each with probabilities so your code decides when to act, when to ask a human, and when to escalate to a bigger model. The economics: ~60 questions cost roughly what one LLM call costs; the same input always gives the same answer (deterministic). The honest catch: Jev can't answer outside your options, and a valid answer isn't always a correct one. Best fit: routing, triage, guardrails, ranking, labeling — simple questions, fixed answers, asked thousands of times. The framing line: it's not LLM vs Jev, it's LLM + Jev — the LLM does the thinking, Jev handles the quick checks around it.
- **Repos/tools:** Jev by TypeSafe AI.
- **Extractable skill:** Decision offload — route every fixed-answer, high-volume question to a typed decision model; reserve the LLM for open-ended thinking; use returned probabilities to set act/human/escalate thresholds.
- **Source:** https://www.instagram.com/p/DdofDHvjh94/
