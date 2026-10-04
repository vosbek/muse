# Talk Notes: "We Let Claude Code and Codex Race Human Researchers" — Elie Bakouch, Prime Intellect

**Video:** [We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect](https://www.youtube.com/watch?v=oVsEddfhdxc) · AI Engineer channel · Sep 26, 2026 · 19:38 · Recorded at AI Engineer World's Fair 2026

**Note:** distilled from the full spoken transcript (read via usetranscribe.io); secondary sources are marked where used.

## Thesis

Big labs claim recursive self-improvement — models training models without human intervention — is imminent, but no independent, third-party benchmark exists to verify it. So Prime Intellect is building open "speedrun" environments that measure whether AI agents can actually do ML research, arguing this work must happen in the open rather than locked inside big labs.

## Key points

- **Origin:** Andrej Karpathy's video training GPT-2 from scratch in ~90 minutes → the community repo **modded-nanogpt** (led by Keller Jordan) drove it 90 min → 45 min → under 2 minutes over ~2 years.
- **Speedrun = a game.** Reach the GPT-2 validation-loss target in the shortest time. The **nanoGPT speedrun** has almost no constraints (same train/val data); the **optimizer speedrun** (released ~2 months before the talk) allows changing only optimizer-related code (e.g., Adam → Muon/Shampoo).
- **Why speedruns:** they're good evaluations *and* good training environments — positive reward for beating the record, zero/negative otherwise; they're fast (runs take 15–20 min); clear verifiable rules make them good for discovery.
- **Setup:** a `goal.md` defines the rules; the agent proposes ideas and submits jobs via `sbatch` on a Slurm cluster using preemptible priority (a human can reclaim the node, cancelling the job). A record counts only after passing a statistical threshold, so it isn't seed luck.
- **The race:** two agents set loose on the cluster — **Codex** (GPT-5.5, xhigh) and **Claude Code** (Opus 4.8, xhigh). V1/V2/V3 were just stop/restart iterations; V3, launched 1–2 days before release, was fed the latest human records and improved on them. A separate **"novelty track"** required beating the record with only novel ideas — much harder for the models.
- **Behavioral contrast:** Claude Code gave up every 9–10 hours ("cannot improve the record") and sat idle ~1/3 of the time (no monitoring was in place); Codex worked continuously, almost never idle, and never asked questions.
- **Scratchpad/memory:** Codex wrote far more to its scratchpad (active memory) — plots were normalized by active hours, so it's a genuine behavioral difference, not just more uptime. Tone differed: Claude excitable with emojis; Codex robotic ("here is what I do, decisions, next steps"). Codex spawned many more subagents, burned ~1B tokens total (mostly cached input, not output), and compacted ~20x/hour vs Claude's ~1/hour (Codex had a 250k context window).
- **Results:** both agents beat the human record almost the entire time; Claude was extremely fast early. Human record ≈ 2,990 steps; Claude beat it by 50–60 steps, Codex finished ~20 steps better. Crucially, agents could fetch human records at any time — Claude did exactly that on restart and improved on them.
- **Next:** a proper benchmark with three tracks — (a) weights-only knowledge, no external access; (b) arXiv papers only; (c) full access including latest human records — across nanoGPT and optimizer speedruns (novelty-constrained), with multiple seeds and identical conditions.
- **Six-day follow-up run** (Codex, Claude, Kimi, GLM — GLM still running): Kimi was surprisingly competitive with a breakthrough on day 4 beating Codex; Claude improved progressively, Kimi in step functions. Replotted **per output token**, the story changes: Claude (max mode) is the most token-hungry, Kimi the most token-efficient. Claude did the most paper searching and found a paper no other model found — which led to the best record.
- **Key limitation:** **no novel optimizers emerged** — models combined papers into clever "+1 improvements" but produced no genuinely new optimizer or mechanism, which he finds telling for a problem accessible to human researchers spending days/weeks.
- **Future direction:** an AlphaEvolve-inspired multi-agent discovery loop — generators (closed models plus cost-effective open-source ones) propose ideas → speedrun gives reward → a judge with "taste" gives quality feedback → winners get scaled to more parameters/tokens; humans stay in the loop as judges; varying objectives/constraints across speedruns creates diversity. Prime Intellect is building GPU sandboxing, its own efficient agents (RLM framework: filesystem + programmatic tool use), training on open-source bases, and has released "Environments" plus verifier/RL-training products (can train models as large as GLM-class).

## Notable quotes & data

- "Recursive self-improvement is like model training models without human intervention… but we don't have any benchmark to basically quantify if this is true or not."
- "Claude Code kept stopping every 9 or 10 hours and basically said, 'yeah I cannot improve the record, it's too hard for me.'"
- "They did some clever trick where they combine different papers… but there was really no novel optimizer or mechanism coming from those models."
- Human record ≈ 2,990 steps; Claude beat it by 50–60 steps, Codex by ~20. Codex burned ~1B tokens total (mostly cached input).

## Tokenomics / efficiency angle

- Codex burned ~1B tokens total — mostly **cached input**, not output — while Claude in max mode consumes far more tokens **per output token** than Codex and Kimi; Kimi is the most token-efficient per unit of progress. Rankings flip depending on which token metric you use.
- Open-source models are "super effective for the cost" as idea generators in the proposed AlphaEvolve-style loop.
- Speedrun runs are cheap and fast (15–20 min), which is what makes them a practical RL/eval environment.

## Local-deploy takeaways

- When comparing agents, track cost **per output token**, not wall-clock progress — the winner flips (Claude max mode looks strong on progress, Kimi wins on token efficiency).
- Use cheap/open models as idea generators and reserve frontier spend for judged winners — the AlphaEvolve-style loop is designed around exactly that cost structure.
- 15–20 minute verifiable environments (speedruns) are a practical local RL/eval substrate: fast, cheap, and falsifiable, unlike long-horizon subjective tasks.

## Sources

- Video page: https://www.youtube.com/watch?v=oVsEddfhdxc
- Full transcript: https://www.usetranscribe.io/yt/oVsEddfhdxc/automated-eye-research
- Prime Intellect blog "Measuring Autonomous AI Research" (primeintellect.ai — secondary source)
- ai.engineer speaker page (secondary source)
