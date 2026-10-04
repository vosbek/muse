# Talk Notes: "What It Actually Takes to Build a Software Factory" — Tereza Tížková, Factory

**Video:** [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](https://www.youtube.com/watch?v=vGCJ7diEtrw) · AI Engineer channel · Sep 27, 2026 · 22:49 · Recorded at AI Engineer World's Fair 2026

**Note:** distilled from the full spoken transcript (read via usetranscribe.io); supplementary secondary sources are marked where used.

## Thesis

A software factory isn't a coding agent or even a swarm of agents — it's the whole autonomous software lifecycle (signals → feedback/logs → prioritization → orchestration → execution → validation → production testing → iteration + continuous learning). Building one takes three things — be agnostic, be truly autonomous, always improve — and requires rebuilding the organization from the ground up, not bolting on a consultancy. (In production for enterprises like EY and Adobe.)

## Key points

- **Definition.** The whole loop of developing software with autonomy: collecting signals, reacting to user feedback and logs, prioritizing, orchestrating, executing, validating, testing in production, iterating, continuously improving and gaining knowledge/skills.
- **Why now.** 2023-era attempts (AutoGPT, BabyAGI) failed — hallucinating LLMs, context length, reasoning quality, no good isolated environments. The tech has caught up.
- **What it's not.** Not a coding agent, "not even a swarm of coding agents, even thousands of agents" — "generating code... that's the easy part"; engineers don't spend most time writing code. Not a consultancy or abstract strategy — "you should really rebuild your organization from ground up."
- **Three pillars.** (a) Agnostic — independent of LLM choices and existing workflows (Slack, GitHub, BYO subscriptions); (b) autonomous — give agents trust/permissions/governance and let them run long (their "missions" already run for weeks; predictions of year-plus runs); (c) always improving — onboard agents like humans (codebase understanding, docs) and let them gain/share knowledge.
- **Model agnosticism.** Cites a Coinbase CEO chart: the org kept growing token usage ("token maxing") while flattening spend via different default models per role (stop pushing frontier as default), caching, no spend limits but requiring visible results, and smart routing.
- **Factory's "automatic model routing."** Assign task (org-level permissions/default models per role) → classify difficulty ("the magic": prompt structure, codebase, task difficulty, tools used) → threshold ("cheapest model that is predicted to accomplish your task") → go, with automatic failover mid-task. Benefits beyond cost: reliability and speed (open models often faster; automatic provider failover). Conservative benchmark: **~25%+ savings**.
- **Caching.** "Just a pricing decision, not a technical challenge" — labs save by skipping context prefill; self-hosted open models on dedicated compute get the same advantage.
- **Autonomy's hard problem** isn't loops (Ralph loops etc.) but defining "done" for open-ended, nondeterministic tasks; cheating risk (agents passing tests without accomplishing the task). "Scary chart": autonomous run durations keep growing, but production reliability isn't solved.
- **Factory "missions."** Long-running agent sessions (weeks). Orchestrator writes the conditions/validation contract *before* code → workers execute in sequence (not a parallel swarm — "more fresh context," like human code review; each worker may still use parallel sub-agents) → validators review and send back. Real customer mission: **16 hours, with validation taking 40% of the whole process**.
- **Validators judge code they didn't write.** Two types: scrutiny validator (rigorous code check: linters, types, tests) and user-testing validator ("in the arena" — a virtual computer that clicks through the app and checks it actually works; needed for a codebase migration where other tools produced non-interactive dummies). Enabled by computer-use progress + persistent VMs.
- **Context: "deferred context engine."** Progressive disclosure of tools — short list + short descriptions; fully load only when needed; nothing removed, just hidden. "Saves 50% of tokens or more" at scale.
- **Power law of adoption.** Succeed big or fail big; unready codebases degrade. Cites Stanford data: without structured codebases and docs, AI makes code worse. "Agent readiness" hygiene framework (reproducible dev env, tests, docs, code style, linters) — bigger customers go through checks + recommended fixes.
- **Continuous learning.** Plugins = packaged reusable skills/context; auto-updating documentation.
- **Humans.** Won't be obsoleted — we keep moving up abstraction levels (human computers → programming languages → coding agents → software factories). "We should be as humans deciding what to build in the software, not how to build it." AI takes the annoying stuff (alignment meetings, status syncs); humans keep the cool stuff. Close: "go touch some grass and let your agents build for you."

## Notable quotes & data

- "Software factory is not just coding agent and it's not even a swarm of coding agents even thousands of agents because generating code... that's the easy part."
- "You can save for example 25% but even more probably" (model routing); "you can save 50% of tokens or more" (deferred context engine)
- "Go touch some grass and let your agents build for you."
- Real mission: 16 hours, 40% of it validation; missions already run for weeks

## Tokenomics / efficiency angle

- **Automatic model routing.** Classify task difficulty → cheapest model above the capability threshold; ~25%+ cost savings plus reliability/speed (open models often faster, provider failover). The Coinbase "token maxing with flat spend" example is the enterprise playbook: per-role defaults, caching, visible results, smart routing.
- **Deferred context engine.** Progressive tool disclosure saves 50%+ tokens at scale — the same retrieval-before-inclusion principle as the playbook's context-management stack, applied to tool definitions.
- **Caching as pricing, not tech.** Open models on dedicated compute capture the same prefill savings the labs do — a cost-structure argument for self-hosting.
- **Validation is a first-class budget line.** 40% of a 16-hour mission went to validation — factory economics must price eval cost, not just generation cost.

## Local-deploy takeaways

- Self-hosted open models on dedicated compute unlock the same caching/prefill savings API providers price in — a concrete cost case for local inference infra.
- The deferred context engine pattern (short tool list + lazy load) is directly implementable in a local harness to cut per-task token overhead.
- The "agent readiness" hygiene checklist (reproducible dev env, tests, docs, linters) is a prerequisite any local factory deployment should audit first.

## Sources

- Video: https://www.youtube.com/watch?v=vGCJ7diEtrw
