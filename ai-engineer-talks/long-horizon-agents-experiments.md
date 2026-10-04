# Talk Notes: "Long-Horizon Agents Need Experiments, Not Just Prompts" — Erina Karati, Supercell

**Video:** [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](https://www.youtube.com/watch?v=x4e5O9zN0TE) · AI Engineer channel · Sep 26, 2026 · 21:26 · Recorded at AI Engineer World's Fair 2026

**Note:** distilled from the full spoken transcript (read via usetranscribe.io); secondary sources are marked where used.

## Thesis

Agents that carry state over long horizons can't be fixed with prompt tuning or a good demo — they need **controlled experiments**: define scenario suites, run simulations, collect structured traces, score behavior with a balanced scorecard, and let an autoresearch meta-loop search a small frozen "policy surface," keeping only changes that survive measurement (a ratchet). Memory (RAG) alone is insufficient; what matters is the **agent protocol** — how memories get written, uncertainty communicated, trust updated, sources attributed, and replanning triggered.

## Key points

- **Project Paradox:** a modular framework from Supercell's AI innovation lab (Karati, ex-Microsoft, ex-Supercell; teammate Arunachalam Manikandan) letting developers plug intelligent autonomous agents into video games as dynamic companions that interact, compete, or cooperate with players and each other.
- **Agent capabilities:** move with intent (guided by memory, emotion, curiosity); interact with the world (pick up/drop objects, context-aware); react to events (beliefs and emotions update on the fly); initiate conversations with agents or players — all stored in memory and feeding back into emotions, beliefs, and goals.
- **Deliberately stateful architecture:** (a) per-agent RAG memory namespaces (no bleed between agents); (b) emotion as a small vector (joy, sadness, fear, anger, disgust) updated after events; (c) belief/trust scores toward other agents and the player — a trust matrix where the LM moves trust up/down/unchanged; (d) an importance score per memory, with above-threshold memories in a separate cache (remembers a murder, forgets Tuesday's dinner).
- It worked short-horizon (demo: "Blossom" plans a picnic — grabs a pastry, goes to the picnic area, answers in context afterward) but **social consistency decayed over long horizons**.
- **Failure modes (the mango-rumor demo):** a rumor about a mango sale spreads agent→agent→agent; later the agent remembers the rough topic but loses the source; rumors harden into facts ("might leave" becomes "is leaving"); agents know facts but fail to use them in plans. The question: how to improve a multi-agent system over long-running social behavior, not one response.
- **Autoresearch (Karpathy's concept):** make the system run experiments on itself — define a scenario suite, run the agents, collect traces, score behavior, change a small policy surface, keep only what improves the score. Project Paradox becomes the lab bench; autoresearch the experimental loop. It's not about RAG retrieval — it's optimizing the **agent protocol** (memory writing/retrieval, uncertainty communication, trust updates, source attribution, replanning).
- **Autoresearch is a meta-system OUTSIDE the village** (villagers have only local perspectives; no shared memory DB). It reads full traces, compares against scenario ground truth, scores, proposes a constrained protocol change, reruns, and asks "did society-level behavior get better?" — evaluating an entire run, not one answer.
- **The loop:** control scenario (e.g., an agent learns a public fact / hears a rumor) → simulate → collect structured traces (observations, conversations, memory writes, retrievals, belief updates) → score (did information spread correctly? did source attribution survive? did uncertainty stay uncertain? did agents act on what they knew?) → propose a small policy change (never rewrite the app; edit the controlled surface) → rerun → keep iff score improves and guardrails hold, else revert.
- **Scenario design matters:** free-wandering agents look cool but can't be evaluated. Example scenarios: public-fact diffusion (bakery closes tomorrow — who learns it? do they remember who said it? do plans change?); rumor uncertainty (does "might leave" survive as a rumor?); replanning (blocked route — do agents update and tell each other?).
- After one autoresearch loop, the mango-rumor agent answered in context — the fix worked.
- **Scorecard shape matters more than formulas:** no single vague "agent quality" metric (hides failures); instead a **balanced scorecard** — diffusion→reach, provenance→source retention, rumors→uncertainty preservation + false-assertion rate, planning→action consistency + time-to-replan, privacy→containment. Single-metric optimization misbehaves (diffusion-only → oversharing; recall-only → noisy/stale memories); the scorecard prevents gaming.
- **Keep the editable surface small:** freeze harness, scenarios, metrics; expose only memory-writing policy, retrieval policy, communication prompt, belief/trust rules, source attribution, replanning triggers. That's the difference between "LM writing random patches" and "searching a controlled policy space."
- **Example fixes:** lost attribution → preserve sources in memory writes/summaries; hardening rumors → store confidence, mark firsthand vs secondhand, require hedging on retelling; local-only facts → classify public facts and proactively share sourced evidence.
- **Two hard lessons:** memory is not enough — you need provenance (firsthand/secondhand/verified/uncertain), separation of raw episodic memories from current beliefs, and scenario-based testing ("not just vibes"); and **rollback is not optional** — the loop must be a ratchet, since a change can help one metric and hurt another (faster spreading → privacy leaks; more recall → stale memories). Claims stay modest without repeated controlled-loop results.
- **Beyond games:** support agents (which policy update supersedes?), personal assistants (commitments, corrections), research agents (provenance, citations, contradiction handling), coding agents (long-running context across issues/files/teammates), workflow agents (access controls, handoffs, replanning) — all share the same problem: state persists and shapes future action.
- **Recipe:** freeze the harness, define scenarios, log traces, score behavior, expose a small policy surface, keep only what survives measurement.

## Notable quotes & data

- "We were no longer evaluating one answer. We were evaluating an entire run."
- "You can add a RAG memory to an agent and still not get the long-term horizon behavior… You need to test behavior through scenarios, not just through vibes."
- "The loop should basically be like a ratchet. Try a change, score it, keep it only if the scorecard improves and guardrails hold."

## Tokenomics / efficiency angle

- The autoresearch loop automates what would otherwise be endless manual prompt tuning and demo-watching.
- A small editable surface plus ratchet semantics (revert anything that doesn't measurably improve) constrains the search and avoids wasted iteration.
- No direct cost/token figures given.

## Local-deploy takeaways

- The pattern is local-first friendly: freeze everything, edit only a small protocol surface, rerun scenarios — cheap to run on local infrastructure with no frontier dependency.
- For any stateful assistant (personal assistant, coding agent): add **provenance to every memory** (firsthand/secondhand/verified/uncertain) and keep raw episodic memories separate from current beliefs — this is a data-model change, not a model upgrade.
- Use a balanced scorecard, not a single quality metric — it prevents the agent from gaming optimization (oversharing, noisy recall) and wasting iteration on regressions.

## Sources

- Video page: https://www.youtube.com/watch?v=x4e5O9zN0TE
- Full transcript: https://www.usetranscribe.io/yt/x4e5O9zN0TE/long-horizon-agents
