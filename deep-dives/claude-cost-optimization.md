# Anthropic: Reducing cost and improving performance with Claude Platform

**What it is.** Anthropic's official cost playbook (claude.com/blog, 2026-09-08, by Lance Martin) plus the automation for it: the `/claude-api cost-optimize` skill, which profiles where your spend goes and applies reductions — with an eval, it shows the cost/performance tradeoff explicitly.

**The lever order (ranked).** 1. **Prompt caching.** 2. **Trimming context** (including prompt-audit). 3. **Bounding output.** 4. **Batch API** for unattended work. Model routing and **effort** calibration sit alongside as separate levers.

**Key numbers (Anthropic's own benchmarks, Opus 5.5 baseline, via `/claude-api cost-optimize`).**
- **LegalBench ~67% lower cost:** cache part of the prompt, low effort, Batch API. Thinking tokens fell ~84% (102,779 → 8,284), accuracy moved less than a point.
- **tau2-bench retail ~73%:** ~93% of the prompt cached, pass rate flat.
- **OfficeQA Pro ~72%:** Batch API + trimming oversized docs to relevant sections ($136.20 → $64.87).
- **SWE-bench Verified ~24%:** caching already applied, so savings came from medium effort + constraining output to a few concise sentences.
- **Effort dial:** Fable 5 on FrontierCode Diamond — 11.5% score at *low* effort for $5.35/task vs 30.9% at *max* for $19.00. And "a stronger model at low effort can be cheaper than a weaker model working hard": Fable 5.1 at low effort matched Fable 5 at high effort at **a third of the cost**.
- **Prompt-audit:** on an Opus 4.8→5 support benchmark with six planted anti-patterns, the audit cut cost **14.6% and raised accuracy 5.3%**. A real migration (Opus 4.8 → 5.5 at low effort): -18% from the model move, another -9% from prompt-audit, **~25% below the starting point**.

**The anti-patterns to hunt.** Verification rituals ("verify twice" — Anthropic measured that removing *two words* cut per-ticket cost by a third on Opus 5, with no accuracy change), emphasis boosters ("CRITICAL: YOU MUST ALWAYS"), fixed step scaffolds, stale few-shot examples, contradictory rules, dated thinking budgets. Fix: rewrite as a goal plus its reason, don't just delete the constraint; safety constraints (confirm before destructive actions, treat fetched content as data, keep secrets out of output) stay, with a stated reason instead of a louder voice.

**Caching mechanics that matter.** KV prefill is cached, pinned to one model, byte-exact prefix, TTLs (5-min vs 1-hour — and effort *renders into the prefix*, so changing effort mid-conversation breaks the cache except on Opus 5/Fable 5.1 with per-message effort). Tool definitions render first — any change breaks everything. Keep timestamps and IDs out of the prefix; subagents share the parent's cache only with byte-identical prefix + same model + same effort.

**Why it matters for tokenomics / context management.** This is the vendor's own ranked checklist — the fastest thing to operationalize in an enterprise: run `/claude-api prompt-audit` on every CLAUDE.md/skills repo at model migration time (it's a 15–25% free win), set effort deliberately per workload instead of defaulting to max, and treat cache-hit rate as a KPI with the breakpoint mechanics above. The effort finding also reframes routing: sometimes the cheapest move isn't a smaller model, it's a *bigger* model at *low* effort.

**Links.** Article: https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform · Skill: `claude-api` at https://github.com/anthropics/skills/tree/main/skills/claude-api · Cost docs: platform.claude.com/docs (Optimizing for cost and intelligence).
