# The Tokenomics Playbook

**For:** a team standardized on VS Code + GitHub Copilot, trying to cut what AI-assisted engineering actually costs — tokens, context, and tooling spend.
**Status:** advisory. Every claim below points at a distilled source in this repo; verify plan-level specifics (Copilot accounting, current model prices) against your own contracts before acting on them.

## The one number that matters: cost per completed task

Don't track tokens. Don't track seats. Track **cost per completed task** — tokens in + tokens out + tool calls, divided by work actually merged. Cast AI's Kimchi harness proved the point on real traffic: cost-per-task routing saved **2.5x vs Claude** while token volume *grew* 1.5x, because cheaper models did more of the work ([source](ai-engineer-talks/harness-picks-model.md)). If you take one thing from this page: instrument cost-per-task before you change anything else.

## Lever 1 — Context hygiene (biggest lever, zero spend)

Most teams burn tokens on context they never needed. The fixes are configuration, not products:

- **`.github/copilot-instructions.md`** — repo-level instructions injected into every Copilot prompt by the client, read locally, costs nothing. This is the single highest-ROI file your team can write: coding standards, architectural constraints, "never do X" rules. The repo's skill system ([skill cards](templates/skill-card.md), [project setups](setups/README.md)) is the grown-up version of the same idea.
- **Put standards in the reviewer, not the implementer.** From Matt Pocock's AI Engineer talk: coding standards belong in a *reviewer* subagent with its own context window, never in AGENTS.md alongside the implementer — red-green-refactor across two context windows ([source](ai-engineer-talks/fixing-pr-bottleneck.md)). One crowded context window is the most expensive mistake in agent design.
- **Content exclusions** — paths Copilot must never read (`.env`, secrets, generated code). Enforced client-side before data leaves the machine. Caveat from the research: exclusions don't cover agent mode, and file names can leak — treat them as hygiene, not a security boundary ([source](01-claude-code-agents/github-copilot-storage-memory-map.md)).
- **Feed computed highlights, not raw pages.** Exa's finding, and it generalizes: ~500 characters of computed summary beat 100k-character raw pages — a **~200x token cut** with zero latency penalty ([source](ai-engineer-talks/coding-agent-out-of-date.md)). Anywhere your workflow pastes raw docs into context, summarize first.

## Lever 2 — Model routing (the 70x spread)

On one identical eval (five character files, one model), token consumption varied **70x between models** (Harald Kirschner's VS Code talk, [source](ai-engineer-talks/vscode-weekly-releases.md)). Model choice is a cost decision before it's a quality decision:

- Route **completions → cheap models**, **chat → mid-tier**, **hard reasoning/agents → frontier**. Copilot's model picker already allows per-surface selection — most teams leave it on default.
- **Re-benchmark on a schedule.** Kimchi's autonomous re-benchmarking caught model drift within weeks — a model that's cheapest today isn't cheapest next quarter.
- **Never hard-tie prompts to one model.** GitHub deprecated selected Copilot models on Oct 19, 2026 with routine notice ([source](07-ai-news/README.md)). Portable prompts, skills, and evals are cost infrastructure: they let you move to the cheapest capable model without rewriting anything.

## Lever 3 — Deferred and progressive context

Don't load context speculatively — disclose it as the task demands it. Factory's **deferred context engine** (progressive tool disclosure) cut token usage **50%+** ([source](ai-engineer-talks/what-it-takes-software-factory.md)). For a Copilot team, the practical translations:

- Skills over mega-prompts: load the skill for the task at hand, not the whole playbook.
- Summarize-then-expand: keep rolling summaries of long threads; rehydrate detail only when needed.
- The GEPA extreme: one round of text-space reflection on 3 examples beat 25,000 RL rollouts 2x — and Databricks served GPT-OSS 120B above Claude Opus at **90x lower cost** ([source](ai-engineer-talks/gepa-optimize-anything.md)). Optimization effort compounds harder than model spend.

## Lever 4 — Local complements (the local-first stack)

Your engineers are on VS Code; the machine under their fingers is free compute:

- **Local memory that never leaves the disk.** Qdrant's demo: 92 objects, 300+ vectors, 15MB, sub-millisecond, fully offline ([source](ai-engineer-talks/stop-renting-memory.md)). Project memory doesn't need a cloud vector DB.
- **Open weights for the cheap tier.** GLM-5.2 runs between Opus 4.7 and 4.8 on long-horizon coding, MIT-licensed, 1M context ([source](ai-engineer-talks/glm-5-2-open-weights.md)). The open tier keeps narrowing the gap — re-test it quarterly (Lever 2's discipline).
- **Local CLI agents for mechanical tasks.** The repo's own pattern: cheap local execution for the 80% of work that doesn't need frontier reasoning; reserve Copilot's best models for the 20% that does.

## Lever 5 — Memory that compounds (stop paying twice)

Every repeated failure your team pays tokens to rediscover is a tax. Two patterns from the talks:

- **The "retro" skill** (Pocock): after every human code review, compound the feedback into new automated checks and standards. Each review makes the next one cheaper.
- **Eval sidecars** (Warp): run a cheap model alongside the expensive one per task type; promote the cheap model wherever it matches quality ([source](ai-engineer-talks/self-improving-factories.md)).

## Lever 6 — Policy-driven governance (FinOps for tokens)

You can route models (Lever 2) and measure cost-per-task — but until policy enforces both, they stay engineer-by-engineer habits. The governance half arrived Oct 6, 2026:

**Stacklet Token Custodian** — launched Oct 6, 2026 — is the control plane that attributes every token across teams, agents, and projects, then governs spend with policies that *act* instead of blocking. When a team nears its limit, it automatically shifts to a lower-cost model or routes an approval, so work keeps moving and spend stays in check ([Business Wire launch release](https://www.businesswire.com/news/home/20261006377964/en/Stacklet-Launches-Token-Custodian-to-Turn-AI-Spend-into-More-Value)).

Why it maps to this playbook:

- **Routing as policy, not habit.** Lever 2's 70x model spread becomes an enforced default: budget exceeded → cheapest capable model, automatically. That's the Kimchi cost-per-task loop, productionized.
- **Attribution, not just reporting.** Every token and agent run traced to team, project, app, and cost center, one view across providers. You can't govern what you can't attribute — this is the instrument-before-you-change step (page top) made vendor-supported.
- **Trusted lineage.** Built by the creators of CNCF's Cloud Custodian — the policy engine enterprises have run for a decade against $10B+ in cloud spend. Stacklet is a Tokenomics Foundation member; their State of Tokenomics 2026 survey found 43% of respondents named *proving value* their biggest challenge, 5x those who named price.

Honest caveats, kept from the research:

- **Commercial, not open source.** Early preview now, GA planned Q4 2026; pricing undisclosed. Per the playbook's AI/tech-only + local-first lens: this is an enterprise control plane, cloud-hosted — it belongs in governance, not in your local stack.
- **Vendor claims.** The auto-shift behavior and cost-reduction figures come from launch materials. Treat as roadmap until preview feedback lands; Avalara's Director of Cloud & AI Optimization is quoted as an early trial customer.
- **Worth watching, not buying on day one.** The Token Governance Summit (Oct 27, 12–1:30 pm EDT) will demo it live — cheap reconnaissance before any pilot.

## What this repo already gives you

- [Storage/memory maps](08-tools-apis/vscode-storage-memory-map.md) for VS Code and [Copilot](01-claude-code-agents/github-copilot-storage-memory-map.md) — exactly what leaves each machine, so you can see the cost surface.
- [37 AI Engineer talk distillations](ai-engineer-talks/README.md), most with a tokenomics angle — the evidence base behind every lever above.
- [COMBINED.md](COMBINED.md) — cross-item patterns: the harness-not-model consensus, skills replacing prompts, vendors publishing real cost numbers.

## Suggested next steps for your team

1. Write the team `copilot-instructions.md` (Lever 1) — one afternoon, immediate token savings.
2. Stand up cost-per-task tracking for one repo for two weeks (the Kimchi metric) — you can't route what you don't measure.
3. Run the model-routing eval: same tasks across Copilot's available models, score quality vs. tokens — expect a wide spread.
4. Pilot a local memory sidecar (Qdrant pattern) on one project before buying any cloud memory product.
5. Watch the Token Governance Summit (Oct 27) demo — decide then whether a Token Custodian preview pilot is worth it; meanwhile pilot routing-as-policy manually with per-surface Copilot model defaults (Lever 2).
