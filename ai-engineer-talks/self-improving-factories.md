# Talk Notes: "Building Self-Improving Agent Software Factories" — Suraj Gupta, Warp

**Video:** [Building Self-Improving Agent Software Factories — Suraj Gupta, Warp](https://www.youtube.com/watch?v=TN3mj92oZ8I) · AI Engineer channel · Sep 27, 2026 · 12:52 · Recorded at AI Engineer World's Fair 2026

**Note:** distilled from the full spoken transcript (read via usetranscribe.io); supplementary secondary sources are marked where used.

## Thesis

Software factories should self-improve — getting better, more efficient, faster over time — via three concrete mechanisms: (1) skills that improve through an outer-loop agent observing the inner loop, (2) persistent memory as an agent-scoped fact store, and (3) eval-driven model routing. This is becoming a core software-engineering job as we shift from building products to building and maintaining factories. (Warp context: ~1M active users of its agentic dev environment; now building the "Oz" cloud agent platform for software factories.)

## Key points

- **Framing.** Self-improvement = agents/models improving over time with humans phased out of the improvement loop; software factories = automations from triage to production. Factories themselves must get better/more efficient/faster.
- **Mechanism 1 — Skills: procedural memory.** E.g., how a triage agent reproduces issues. Skills go stale: humans give feedback, agents learn in their trajectories. Fix: an outer-loop agent observes the inner loop's runs, spots mistakes and human feedback, and synthesizes skill updates. Warp's internal example: a triage agent on their open-sourced client repo — GitHub issue arrives → agent determines what's missing / whether to dedupe; feedback signals are thumbs up/down, user comments, Warp employee comments.
- **Skill updates land as a pull request.** Full git observability of how the skill evolves over time, and a human reviews the update so the outer loop can't make the triage agent worse.
- **Mechanism 2 — Persistent memory: an agent-scoped fact store.** Without it, a Sentry agent re-gathers context on every repeat issue (wasted tokens, no guarantee of the same root cause). An outer-loop agent extracts facts/learnings/outcomes from inner-loop runs. Demo: a Sentry agent's memory store of past root-cause analyses — on a new run it used 5 stored memories to speed up triage. Memories are versioned, human-editable/deletable, and source-traceable (open the run a memory came from; drop "local maxima").
- **Memory works across all harnesses on Oz** (Warp's own, Claude Code, Codex — names as transcribed): auto-created, fully traceable, human-reviewable.
- **Mechanism 3 — Model routing.** "Prohibitively expensive to run all of your agents that are doing simple things like triage or fixing simple CI failures with Opus." Warp's "auto models": out-of-the-box routers continuously evaluated for Pareto efficiency as new models arrive — better than pinning to Opus or Haiku. Users can also define custom routing rules in config: task classes → models (his example: database migrations → GLM, runbooks/API docs → Qwen).
- **Eval-driven routing.** Task-class routing is "more art than science" today; next step is customer-facing evals (define what you care about, which knobs to turn). Internally, an "eval sidecar" uses a best-at-k approach — run agents across models on Oz for a prompt; finding: "UI tasks are really well done with GLM. We don't really need to run those with Opus." Workflow-specific evals, not generic benchmarks. Being productized for customers.

## Notable quotes & data

- "It can become prohibitively expensive to run all of your agents that are doing simple things like triage or fixing simple CI failures with Opus."
- "UI tasks are really well done with GLM. We don't really need to run those with Opus."
- ~1M active Warp users; skill improvements tracked through git PRs with human review
- Sentry agent used 5 stored memories to speed up triage on a repeat issue

## Tokenomics / efficiency angle

- **Model routing for Pareto efficiency.** Auto models re-evaluated as new models land; best-at-k eval sidecar; task-class routing (GLM for UI work, Qwen for docs) instead of defaulting to Opus — the direct answer to "everything runs on the frontier model."
- **Persistent memory avoids re-gathering context on repeat issues** — direct token savings, plus consistency (same root cause, not a re-derived guess).
- **The skill-improvement loop** (outer-loop agent → git PR → human review) is eval-driven iteration on the factory itself — improvement compounds instead of being re-paid per session.

## Local-deploy takeaways

- The persistent-memory pattern (versioned, human-editable, source-traceable fact store) is implementable locally — e.g., a sqlite-backed store — without Warp's Oz platform.
- Task-class routing config (migrations → GLM, docs → Qwen) maps directly onto a local Ollama/multi-model setup: cheap local models for routine agent chores, frontier only where evals justify it.
- The best-at-k eval sidecar is a repeatable local pattern: run the same agent prompt across models, measure, pin the cheapest that clears the bar.

## Sources

- Video: https://www.youtube.com/watch?v=TN3mj92oZ8I
