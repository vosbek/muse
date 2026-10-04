# 05 — Prompts & Evals

**Thesis:** A single reel, but it carries a discipline the whole collection depends on: prompts are not set-and-forget text — they're experimental surfaces with measurable ROI per rule. Everything else in this repo (skills, memory, routing) only compounds if someone is testing what actually improves output and deleting what doesn't.

### How to run experiments on prompts when output quality is critical
- **Creator:** @camillaintech · **Date:** 2026-07-24
- **What it suggests:** After 50 hours building an AI model workflow, the hard-won method for prompt iteration: decompose output quality into three pillars — the foundational LLM, the customization layer (knowledge base, user info), and the quality gates/rules governing output — then test changes to each pillar systematically and measure aggregate improvement. The counterintuitive finding that drives the whole method: adding more rules to force quality actually degrades it. Each rule is another check the model must run before generating, which slows responses and — worse — forces the model to prioritize across a long list, producing worse output. Unless a rule is deterministic and explicit, the model infers its meaning slightly differently each time, so you can't eyeball single outputs; you need repeated runs and aggregate measurement to know whether a rule earns its keep. The promised Part 2 (the actual system) isn't in this reel, but Part 1's frame is the valuable part: treat every prompt addition as a hypothesis with a measured payoff, and assume rules have costs until proven otherwise.
- **Repos/tools:** None (methodology)
- **Extractable skill:** Rule-ROI testing — for each prompt rule, run repeated trials, measure aggregate quality and latency, keep only rules that prove their worth; default to fewer, deterministic rules.
- **Source:** https://www.instagram.com/reel/DbL2Wd3tK_4/
