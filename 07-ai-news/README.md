# 07 — AI News

**Thesis:** Two data points, one argument between them. @edhonour's take — the model (Opus 4.5) is excellent, the coding tool (Claude Code) is the bottleneck, and the open Qwen-based alternative won on a real task — reinforces the collection's harness-first theme: evaluate the full stack, not the model in isolation. @leon.petrou's Gemini news shows the other axis that matters: proprietary data access (250M real-world locations) as a moat no parameter count can replicate. Read together: the tooling layer and the data layer are where differentiation now lives, not raw model quality.

## Oct 2026

### Kolibri: 78B of capacity at 3.46B active per token — sparsity as a serving-economics play
- **Creator:** Aleph Alpha · **Date:** 2026-10-03 (announced on German Unity Day; full weights on Hugging Face)
- **What it suggests:** Aleph Alpha released Kolibri-1, an open-weight English–German MoE transformer — 78.1B total parameters, but the router activates only 3.46B per token (6 of 384 experts per token, plus one shared expert; 50 layers, sliding-window attention on 40 of them). The pitch is the serving-economics frontier: 78B-scale capacity at the compute cost of a ~3B model — Aleph Alpha claims Pareto-front quality-vs-operating-cost in both languages (71% on German benchmarks, decoding faster than GPT OSS A5B / Qwen 3.6 A3B / Gemma 4 A4B). The catch that matters for tokenomics: sparsity cuts compute, not memory — the full 78B still has to live somewhere (~78 GB in FP8/BF16), so Aleph Alpha's minimums are datacenter-class (2× A100 80 GB, 2× H100 SXM5, 1× H200, or 1× B200/B300); one report of ~170 tok/s on a single RTX Pro 6000 in FP8 is unverified. Supports up to 1,048,576 tokens of context, though Aleph Alpha recommends ≤262,144 for serving efficiency — long context is a KV-cache problem before it's an accuracy problem. License is Apache 2.0 (with patent grant), weights downloadable, runs on your own hardware — the "sovereign ops" profile: data stays local, no third-party inference service. Trained on 768 B200 GPUs in Germany and Finland, signed to the EU GPAI code of practice. Also ships a "Merlin-Arthur" behavior: refuses to answer when the provided context is insufficient to verify — a context-grounding discipline worth stealing for enterprise agents.
- **Repos/tools:** Aleph Alpha Kolibri (Hugging Face, Apache 2.0; BF16 + FP8 weights), `aleph-alpha-inference` package for vLLM support
- **Extractable skill:** When evaluating sparse models, separate the two cost axes — active-params-per-token sets compute cost per token, total params set the memory floor. And size long-context plans by KV-cache cost, not parameter count. Concrete fit note: at ~78 GB (FP8) this lands inside the 128 GB unified-memory envelope of the RTX Spark-class machines debuting at the Oct 7 Microsoft/NVIDIA keynote — a candidate for the local-vs-Copilot cost-per-task analysis.
- **Source:** https://the-decoder.com/aleph-alpha-releases-kolibri-an-open-weight-model-that-makes-the-case-for-european-ai-sovereignty/

### Opus 4.5 is amazing — Claude Code is the problem
- **Creator:** @edhonour · **Date:** 2025-11-30
- **What it suggests:** Jay R. Asher's argument, from direct experience: Anthropic's Opus 4.5 is an excellent model, but Claude Code as a coding tool underperformed on a complex task — while Qwen-Agents, an open-source alternative running the Qwen Code 3.0 model, succeeded on the same work. The takeaway isn't "switch tools"; it's the evaluation discipline. Judge the model and the harness separately, test alternatives on your actual workload instead of your assumptions, and don't let brand loyalty override measured results. It also quietly reinforces the open-model story running through this collection: the gap between frontier-proprietary and open weights keeps narrowing to the point where the harness decides the winner.
- **Repos/tools:** Qwen-Agents / Qwen Code 3.0 (open source, Qwen), Claude Code, Opus 4.5 (Anthropic)
- **Extractable skill:** Stack-separated evaluation — benchmark model vs. harness independently on your real tasks; re-test open alternatives regularly.
- **Source:** https://www.instagram.com/reel/DRs5CHVDsoU/

### Gemini grounding with Google Maps: 250M real-world locations
- **Creator:** @leon.petrou · **Date:** 2025-11-11
- **What it suggests:** Google gave Gemini "Grounding with Google Maps" — live access to 250M+ real-world locations with hours, ratings, and reviews inside the Gemini app. The pitch is accuracy: grounded answers about places beat generic or hallucinated ones from competitors. But the strategic read matters more than the feature: proprietary, continuously-updated data access is a durable moat that model weights alone can't cross. For builders, it's also a signal about where to invest — the post explicitly frames it as an opportunity to build travel planners, digital tour guides, and local apps on top of grounded location data. The general principle: when evaluating AI platforms, weight exclusive data access alongside model quality; the best model with stale data loses to a good model with live data.
- **Repos/tools:** Gemini app (Google), Google Maps Platform
- **Extractable skill:** Data-moat evaluation — when choosing platforms, score proprietary live-data access as heavily as model benchmarks.
- **Source:** https://www.instagram.com/reel/DQ65_PejKYJ/

## From X bookmarks (Sep 2026)
Distilled from Matt's X bookmarks, newest first. Full post text at each permalink (X truncates long posts in timelines).

### Six lessons on getting the most out of bots, from Grok Bot's leads
- **Creator:** @peteryang · **Date:** 2026-09-28
- **What it suggests:** Shares six things learned from Grok Bot's engineering and design leads on getting the most out of bots — the visible portion begins mid-list (text truncates) — quoting the author's own Sep 27 post about delegating everything touched by keyboard and mouse to bots. A short video and an image accompany it. Verifiable: the operating principle is aggressive delegation — keyboard-and-mouse work routed to bots by default — with six concrete lessons from the team that builds Grok Bot. The full list is at the permalink.
- **Repos/tools:** None (news).
- **Extractable skill:** Default to delegating keyboard-and-mouse work to bots; learn the delegation playbook from teams that ship them.
- **Source:** https://x.com/peteryang/status/2104575614263144794

### The week in agents: xAI, Meta, OpenAI, Anthropic roundup
- **Creator:** @ParkerRex · **Date:** 2026-09-21
- **What it suggests:** A Monday roundup video covering everything that changed in agents last week across the major labs (text truncates). The substance is the short video at the permalink. Verifiable: this is a news digest, not a technical post — useful as a weekly catch-up surface for the pace of agent releases. For the playbook, the durable lesson is the habit: a weekly agent-news scan beats sporadic deep dives when the landscape moves this fast.
- **Repos/tools:** None (news).
- **Extractable skill:** Run a weekly scan of agent releases across labs instead of relying on sporadic deep dives.
- **Source:** https://x.com/ParkerRex/status/2102078834409340962

### GitHub Copilot models deprecated Oct 19, 2026 — don't hard-tie to one model
- **Creator:** @OrenMe · **Date:** 2026-09-20
- **What it suggests:** Warns builders of agentic workflows, prompts, skills, and custom agents: if your work is tied to a specific model, pay attention — quoting the GitHub changelog notice that selected GitHub Copilot models will be deprecated on October 19, 2026, with a link to the changelog (text truncates). Verifiable: the news is the deprecation date; the lesson is architectural — model deprecations are now a routine operational event, so prompts, skills, and evals must be portable across models. This is the strongest argument in the collection for the abstraction layers (routers, adapters, skills) that insulate you from any single model's lifecycle.
- **Repos/tools:** None (news). Changelog — github.blog/changelog/2026… (display truncated in source)
- **Extractable skill:** Keep prompts, skills, and evals portable; treat model deprecation as a routine operational event.
- **Source:** https://x.com/OrenMe/status/2101685249633587623

### New Jira canvas in the GitHub Copilot app
- **Creator:** @pierceboggan · **Date:** 2026-09-14
- **What it suggests:** Announces a Jira canvas in the GitHub Copilot app that turns Jira tasks into action, with a short demo video. The post is complete. Verifiable: this is Copilot extending from code into task management — Jira tickets becoming actionable work items inside the agent surface. News value: the agent IDE is absorbing the project-management layer, which shortens the path from ticket to working code and is worth evaluating for teams living in Jira.
- **Repos/tools:** None (news).
- **Extractable skill:** Evaluate agent surfaces that turn tickets directly into action to shorten the ticket-to-code path.
- **Source:** https://x.com/pierceboggan/status/2099572243240276466

### Claude now writes 80% of Anthropic's code; engineers ship 8x more
- **Creator:** @addyosmani · **Date:** 2026-09-14
- **What it suggests:** Reports that at Anthropic, Claude now writes 80% of the company's code and engineers ship 8x more code per quarter — linking the Anthropic blog post on agentic coding, with an image (text truncates). Verifiable: this is a first-party productivity claim from the lab building the model — 80% machine-written code, 8x throughput. Treat vendor self-reports as directional; the full analysis is at the permalink and the linked blog.
- **Repos/tools:** None (news). Blog — claude.com/blog/agentic-c… (display truncated in source)
- **Extractable skill:** Measure your own agent-written code share and throughput; don't manage by vendor benchmarks alone.
- **Source:** https://x.com/addyosmani/status/2099577600159158765

### Second batch (Aug 24 – Sep 12)

### GitHub's HydraFusion: frontier-level coding from the orchestrator
- **Creator:** @pierceboggan · **Date:** 2026-09-10
- **What it suggests:** "The best model may not be a model after all. @Jujujuliakasper walks us through our early learnings with Project Hydrafusion and how we're delivering frontier-leve[l results, truncated]" — linking gh.io/githubcopilotd. GitHub's thesis: the orchestrator — the system that routes, decomposes, and verifies — matters more than any single model. "Frontier-level" results from orchestration rather than weights is the decision-model economics argument wearing an enterprise product hat. For buyers: evaluate the harness, not the model card.
- **Repos/tools:** gh.io/githubcopilotd (Project HydraFusion)
- **Extractable skill:** Evaluate coding assistants on orchestration quality; the router is the product.
- **Source:** https://x.com/pierceboggan/status/2098080315562733795

### Hands-on with HydraFusion: "exactly how you'd want a teammate to work"
- **Creator:** @OrenMe · **Date:** 2026-09-10
- **What it suggests:** "I recently got to play with HydraFusion. It's exactly how you would want your employee or team mate t[o work, truncated]" (gh.io/GitHubCopilotD). An independent hands-on corroborating GitHub's claims: the experience feels like working with a competent teammate, not an autocomplete tool. The bar being set is behavioral — does it work like a colleague? — a harder eval than benchmark scores and a more useful one for adoption decisions.
- **Repos/tools:** gh.io/GitHubCopilotD
- **Extractable skill:** Eval agent tools on teammate-behavior, not just benchmarks.
- **Source:** https://x.com/OrenMe/status/2097920445081165850

### HydraFusion in plain English
- **Creator:** @acolombiadev · **Date:** 2026-09-08
- **What it suggests:** "Learn about @github HydraFusion in plain English." A pointer post — the accessible explainer for this HydraFusion cluster. When a product generates its own plain-English explainers within days of launch, it's a signal the category is moving fast enough to need translation layers.
- **Repos/tools:** None.
- **Extractable skill:** When a launch spawns instant explainers, treat the category as fast-moving and track it closely.
- **Source:** https://x.com/acolombiadev/status/2097455710023876655

### Lerna: use HydraFusion in the Copilot CLI, watch subagents live
- **Creator:** @unixterminal (Hayden Barnes) · **Date:** 2026-09-07
- **What it suggests:** "Lerna - Use GitHub's new AI orchestrator, HydraFusion, in GitHub Copilot CLI - Monitor subagent acti[vity, truncated]" — github.com/sirredbeard/Lerna. A third-party tool that puts HydraFusion orchestration in the terminal and, crucially, lets you watch subagent activity. Observability is the missing piece in most agent setups: when the orchestrator fans out to subagents, you need to see what each one is doing. Lerna's angle — monitoring as the feature — is the right instinct for anyone operating multi-agent systems.
- **Repos/tools:** github.com/sirredbeard/Lerna
- **Extractable skill:** Demand subagent observability in any orchestrator; fan-out without visibility is undebuggable.
- **Source:** https://x.com/unixterminal/status/2097033608481082663

### "Hydrafusion is here!" (brief)
- **Creator:** @burkeholland · **Date:** 2026-09-04
- **What it suggests:** Launch-day pointer for HydraFusion. Filed with the cluster above; details at the permalink.
- **Repos/tools:** None.
- **Extractable skill:** None — pointer.
- **Source:** https://x.com/burkeholland/status/2095965855297220835

### "I've got some bad news…" (brief)
- **Creator:** @burkeholland · **Date:** 2026-09-12
- **What it suggests:** Text is just "I've got some bad news…" (4 replies, 53 likes) — the substance is presumably in attached media or replies. Filed as a stub; the take is at the permalink.
- **Repos/tools:** None.
- **Extractable skill:** None — stub.
- **Source:** https://x.com/burkeholland/status/2098622630425416023
