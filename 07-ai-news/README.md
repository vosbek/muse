# 07 — AI News

**Thesis:** Two data points, one argument between them. @edhonour's take — the model (Opus 4.5) is excellent, the coding tool (Claude Code) is the bottleneck, and the open Qwen-based alternative won on a real task — reinforces the collection's harness-first theme: evaluate the full stack, not the model in isolation. @leon.petrou's Gemini news shows the other axis that matters: proprietary data access (250M real-world locations) as a moat no parameter count can replicate. Read together: the tooling layer and the data layer are where differentiation now lives, not raw model quality.

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
