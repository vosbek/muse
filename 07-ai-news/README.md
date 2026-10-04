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
