# Talk Notes: "How We Built an Agent That Improves Itself" — Zubin Aysola, Weights & Biases

**Video:** [How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases](https://www.youtube.com/watch?v=XyV6bSMyq-I) · AI Engineer channel · Sep 26, 2026 · 17:05 · Recorded at AI Engineer World's Fair 2026

**Note:** distilled from the full spoken transcript (read via usetranscribe.io); secondary sources are marked where used.

## Thesis

W&B's ARIA agent improves itself through a **production↔offline eval flywheel** built on Weave: production traces are logged in the exact same format as offline traces, so every production miss (or win) becomes an offline eval task (886 YAML tasks); a bit-wise identical agent runs in production and in a simulation environment; nightly CI compares prod vs candidate variants; and ARIA itself reviews traces, authors tasks, and proposes prompt/skill variants — "replication from production to simulation to agent-defined improvement." The governing worry: benchmarks, evals, agents, and configs are all covariant, so measurement must be identical across prod and offline.

## Key points

- **ARIA:** W&B's agent harness for doing research inside the W&B platform; went GA the Monday before the talk (~Sep 21, 2026). Companion talk by peer Tim Sweeney (see ai-research-agent-experiments.md).
- **Core problem** ("what I go to bed thinking about"): benchmarks, evaluations, agents, and configs are all covariant — principled evaluation of a changing system demands identical measurement in production and offline (the sim-to-real gap).
- **W&B Weave:** observability for production AND offline agent tracing. Half the team works production (deploy, log traces in the exact same format); half works offline (simulation envs, run ARIA, track metrics in Weave).
- **The flywheel:** rip production traces → convert to offline eval tasks → hill-climb on them (fix errors or reinforce wins) → deploy new agent versions.
- **Live demo "ARIA researches ARIA":** asked ARIA to do autoresearch on itself — it took the codebase (a W&B artifact), launched jobs against the offline eval framework, reviewed production traces, added hill-climb tasks, and wrote a new variant of itself.
- **Production trace → eval task, done live:** took a real Weave production trace, had ARIA log it into offline evals, ran candidate vs production agent on it with evals streaming into Weave. Nightly CI jobs (~7 weeks of traces) evaluate the prod-format agent plus candidate variants — ~66% on some tasks; "for a while the CI broke, we had ARIA fix itself last night."
- **Mostly prompt engineering + skills, not RL:** current models are good enough at W&B tasks; the work is building agent skills — but with RL-grade simulation rigor.
- **Bit-wise identical agent** in production and simulation; research and production code are exactly the same; a 4-hour prod→research sync job prevents drift as researchers cut new variants/skills.
- **Generate a TON of traces, then decide what to do with them:** measure emergent properties, align the agent. Improvement comes from manual task review or asking ARIA to review its own rollouts and reinforce behavior via prompting.
- **Model-agnostic harness:** tests many models (CoreWeave inference, foundation-model providers); agnostic stack for compaction, context prep, UI payloads; YAML-defined configs produce many parallel variants — "better to run more experiments than fewer."
- **Unconstrained sandbox:** the agent can do anything — ARIA built itself a sandbox to run parallel executions of its own research loop; unconstrained environments enable emergent behavior.
- **Simulation-env pattern (agnostic DAG):** YAML config → hydrate (load live data) → set up env (expensive: full ML training logs, possibly simulated GPU execution → parallelize) → rehydrate (hot-patch runtime configs not expressible in YAML) → run agent (bit-wise identical to prod) → score → tear down (don't clobber teammates).
- **Scoring is two-mode:** normative (pass/fail per task) and relative (e.g., variant that asks the user questions vs one that doesn't — which behaves better), a traditional RL formulation.
- **886 tasks as YAML** (start state + user configs + end state), leveled and exposed to the product team for validation; three simulation styles: plain text instruction, simulated user persona (an LLM role-plays a user asking questions in order for multi-turn), and production-trace-derived tasks.
- **Demo payoff:** ARIA turned a real agent trace into a WBAF (W&B Agent Factory) regression task, diagnosed the root cause — `weave.log` SDK call not invoked properly in the sandbox — replicated the trace, ran agent variants, and the winning candidate got a tight prompt injected into the system prompt/skills fixing that exact SDK error. Prod vs candidate compared in Weave.
- **Human stays in the loop:** "I haven't written a line of code in maybe eight months because I just tell Claude to write all my code" — but that doesn't remove the thinking about how to improve; time goes to guardrails and making the system reinforce itself better. Also demoed: ARIA training ML models on H200s on CoreWeave infra and autoresearch on Karpathy's nanochat.

## Notable quotes & data

- "Benchmarks, evaluations, the agents, and how you configure them are all covariant."
- "For a while the CI broke, we had ARIA fix itself last night."
- "I haven't written a line of code in maybe eight months because I just tell Claude to write all my code for me."
- 886 tasks; ~66% on some tasks; 7 weeks of nightly CI traces; 4-hour prod→research sync.

## Tokenomics / efficiency angle

- Offline sim envs are "relatively expensive" (full training logs, simulated GPU execution), so they're parallelized and torn down after scoring.
- YAML-defined configs make it cheap to spin up many parallel agent variants — "better to run more experiments than fewer."
- The automated trace→task→hill-climb flywheel replaces manual offline-benchmark authoring.

## Local-deploy takeaways

- The core pattern — production traces → YAML eval tasks → nightly candidate comparison — is implementable locally: tasks are just files (start state + user config + end state), and the "CI" is a script.
- Keep research and production agent code identical with a sync step; otherwise your offline improvements silently diverge from what's deployed.
- Generating a large volume of traces and deciding what to do with them later (emergent-property measurement, self-review) is cheap relative to hand-authoring evals — volume is the strategy.

## Sources

- Video page: https://www.youtube.com/watch?v=XyV6bSMyq-I
- Full transcript: https://www.usetranscribe.io/yt/XyV6bSMyq-I/arya-agent-self
