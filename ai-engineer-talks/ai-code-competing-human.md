# Talk Notes: "AI-Generated Code Is Already Competing With Human Code" — Daksh Gupta, Greptile

**Video:** [AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile](https://www.youtube.com/watch?v=474j-n1Ltxc) · AI Engineer channel · Sep 27, 2026 · 12:40 · Recorded at AI Engineer World's Fair 2026

**Note:** YouTube's transcript was unreadable in our environment, so this is distilled from the video's own description/chapters plus biggo.com's AI-generated talk summary — treat secondary-derived points as the speaker's arguments per those summaries, not verbatim transcript.

## Thesis

Fully autonomous coding agents crossed the enterprise-usability threshold around **December 2025**. Greptile — reviewing **1M+ PRs/month** for NVIDIA, Coinbase, Scale, Datadog, American Express — finds roughly **a quarter of reviewed PRs are now completely or largely AI-generated** (up from <1% in early 2025), and on three independent quality tests (revert rates, P0/P1/P2 bug severity, review iterations to merge) agent-authored PRs perform roughly on par with human-authored ones. Since validation can't scale with agent output, Greptile reframed validation around three questions answered by sandboxed browser agents rather than human review.

## Key points

- **The arc:** 2022–23 tab-completion era (Copilot, Cursor TabComplete); 2024 multi-file editing (Cursor first mover); 2025 autonomous agents producing whole PRs. **December 2025 is the watershed** — "coding agents became literally completely autonomous" (100-PRs-a-day developers, polyphasic-sleep anecdotes). Gupta moved to SF ~2023 specifically for AI coding after GPT-3.5.
- **Detection was the hard first problem; three signals combined:** GitHub author field (Codex/Claude/Cursor as committer — under 1% alone), "Co-authored by Claude/Cursor" PR footers, and branch-name prefixes agents give themselves. Combined: **~25% of PRs in the prior month** completely/largely AI-generated vs **<1% in early 2025**. "The progress is very continuous" — no step-jumps visible at model release dates.
- **Test 1 — revert rates** (GitHub's `revert-` branch prefixes enable tracking): **Codex ~1 per 1,000; Devin ~3.5 per 1,000; humans in the middle at ~2.5 per 1,000.** "Very little correlation, if any" between PR size and revert rates — undercutting the objection that humans keep the hard work for themselves.
- **Test 2 — Greptile bug-severity comments:** three of four agents tested produced **fewer P0s than humans**; the pattern held for P1s and P2s. "Human-generated PRs were about equal in quality to agent-generated PRs based on this data."
- **Test 3 — review iterations to merge** (Greptile's modal workflow is review → agent addresses comments → new commit): **Devin averaged 2.1 cycles, Codex 2.45, humans in the middle** — agent PRs needed no extra rounds.
- **Failure modes differ qualitatively.** From a corpus of ~4 comments/PR (several million comments), normalized to human = 1x — **Claude was ~1.5x more likely** than humans to produce a SQL injection; **Devin ~0.5x as likely** to produce an off-by-one. Distinct per-agent failure signatures imply agent review tooling needs **error-class-specific tuning**, not one generic bar.
- **The scaling crisis.** Greptile used weekly by tens of thousands of engineers; PRs per user per month — median **50** (~2/workday), P90 **500** (~25/workday), P99 **in the thousands**. "The people on the margins are actually producing pull requests at the rate at which they're coming up with new ideas." Manual review, testing, and external QA cannot scale to this.
- **Greptile's three-question merge framework** (instead of "automate QA"):
  - **Q1** — does the change violate the user contract? (block merge)
  - **Q2** — does it increase propensity of a future violation?
  - **Q3** — does it fulfill the author's stated intent? (high-confidence merge)
  - **Mechanism:** spin code up in a sandbox, install dependencies, mock inputs, run browser agents that click around trying to break things, inspect every changed file plus related files.
- **Adoption signal:** nearly **one-fifth of all PRs** Greptile reviews are already merged with **no human review or human testing** — a number Gupta explicitly wants to increase "within the guardrails of producing really high-quality code."
- **Caveats** (per the secondary summary's own synthesis): the 25% estimate rests on self-reported/tool-emitted signals (true rate may be higher or sample-skewed); revert is a coarse proxy that misses subtle correctness/maintainability regressions.

## Notable quotes & data

- ~25% of PRs largely AI-generated (from <1% a year earlier); revert rates Codex 1 / Devin 3.5 / humans 2.5 per 1,000.
- "Three out of the four agents that we tested performed better than humans in terms of the rate at which they were producing P0s."
- "The P99 is in the thousands of pull requests. That means that the people on the margins are actually producing pull requests at the rate at which they're coming up with new ideas."
- "In spite of my initial skepticism around the enterprise usability of end-to-end coding agents, the evidence seems to suggest that they're here."

## Tokenomics / efficiency angle

- **~20% of PRs merged with zero human review/testing** via sandboxed agent validation — direct labor-cost efficiency; the explicit goal is pushing that share higher inside quality guardrails.

### Local-deploy takeaways

- **Tune review tooling per agent's failure signature, not one generic bar** — distinct agents produce distinct error classes (SQL injection vs off-by-one); error-class-specific review configs get more signal per review-token spent.
- **Shift review from "automate QA" to the three-question framework** (violates user contract? increases future-violation propensity? fulfills stated intent?) — executed by sandboxed agents that exercise the code, which scales where human review queues can't.

## Sources

- YouTube description/chapters: https://www.youtube.com/watch?v=474j-n1Ltxc
- BigGo AI talk summary: https://finance.biggo.com/podcast/e0c502d3f5b75332
