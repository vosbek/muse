# Unreal Agent — async-first agent harness

**What it is.** An open-source agent harness from Unreal Labs, written in Go. The launch post claimed "state-of-the-art cost efficiency" at "39% cheaper"; the repo itself (~2,060 stars, created Sep 21 2026) presents as an async-first, durable-execution harness with an explicit benchmark adapter. (Note: I could not locate the exact 39% benchmark comparison inside the repo — treat that figure as the launch claim, not a verified measurement.)

**How it works.** The architecture separates *deciding* from *doing*, which is where the cost story lives:

| Component | Responsibility |
|---|---|
| Session inbox | Session-scoped, in-memory dedup of external, control, and crash inputs |
| Coordinator | Persists accepted inputs, runs LLM turns, resolves tool translators, dispatches committed operations |
| Session store | Append-only persisted history, forkable; atomically records tool-call status with operations |
| Context builder | **Statefully assembles model input in memory** and returns a record of anything omitted, truncated, or compacted. Performs no I/O, takes no persistence dependencies |
| LLM adapter | Sends prepared input to a provider, returns a normalized response; owns auth, cancellation, provider errors |
| Tool translator | Validates a tool call and translates it into operations. Runs synchronously on the coordinator loop — **must not perform I/O or suspend the loop** |
| Operation manager | Actor runtime for durable operations; operations are serializable and versioned, so a proxy manager can ship them to a remote sandbox for execution |

The key move: tool execution happens as *operations* outside the model's turn. The model never sits in a turn polling a long-running command — the harness does that deterministically and hands back the result. Sessions are serializable and versioned, so runs are resumable and auditable.

**Run it / evaluate it.** The repo ships a Harbor 0.22.0 evaluation adapter (`benchmarks/harbor/`): build with `make -C benchmarks/harbor build REVISION=HEAD`, then run via `harbor run` against OpenAI, OpenRouter, or Fireworks models with `thinking_level` low→max. There's a Terminal-Bench 4.0 config for Modal. This is the honest way to check the "39% cheaper" claim on your own workload before believing it.

**Why it matters for tokenomics / context management.** Unreal Agent is the architectural embodiment of GitHub's lesson "optimize orchestration, not just model output": every turn the harness completes deterministically is a turn you didn't pay a frontier model for. The context builder's explicit record of what was omitted/truncated/compacted is also a governance primitive — it makes context decisions *auditable*, which is exactly what an enterprise context layer needs. If you're evaluating harnesses, this is the one to benchmark against your current setup on cost-per-completed-task.

**Links.** Repo: https://github.com/unreallabsai/unreal-agent · Launch post: https://x.com/unreallabsai/status/2102435462065385775 · Benchmarks: `benchmarks/harbor/` in the repo.
