# Tokenomics Deep Dive: what AI-assisted engineering actually costs, and how to cut it

**What it is.** A synthesis of 12 recent tokenomics articles/posts, the open-source cost-cutting toolstack, and Copilot-specific + local-CLI levers — researched October 2026 — combined with this repo's own distilled evidence (37 AI Engineer talks, vendor cost writeups, storage/memory maps). Written for a team standardized on VS Code + GitHub Copilot that wants Copilot as the main tool and cheaper paths everywhere else.

**Status.** Advisory. Vendor percentages are marketing-adjacent even when the math checks out; Copilot's credit allowances shift (a promo "credit cliff" just stepped down Sep 1, 2026). Verify plan specifics against docs.github.com before contracting. Unverified items are flagged inline.

## The core equation

**Cost per successful task** = (tokens in × input rate + tokens out × output rate + tool calls) ÷ tasks actually completed. Everything else is a vanity metric. The evidence:

- Agentic coding tasks average **~3,500× the tokens** of single-round reasoning; same-task runs vary up to **30×** in tokens (theagentloop, DEV Sep 2026).
- TheAgentCompany benchmark: $4.20/task at 30.3% success = **~$13.90 per successful task**. A cheap model that fails and retries costs more than a capable one that succeeds first try.
- Anthropic's own finding: inference is **>85% of enterprise AI budgets**; agent tasks run 50K–500K tokens vs 2–4K for chat (via Requesty).

## The ranked levers (with numbers)

**1. Prompt caching — the highest-ROI single change.** Provider-native KV-cache on stable prefixes:
- Anthropic: 90% off cached input reads (writes cost 1.25× — a mutating prefix costs *more* than no cache). PwC's measurement study: **78.5% cost savings on Sonnet 4.5**, 79.6% on GPT-5.2 across 500+ long-horizon sessions. ⚠️ secondary-source figures; paper not fetched directly.
- OpenAI: 50% off (90% on GPT-5.4/5.5), automatic prefix matching. Gemini: ~75% via explicit CachedContent API.
- The discipline that decides everything: **static prefix first, dynamic content last.** A timestamp at the top of a system prompt produced 0% cache hits on OpenAI and *+25% cost* on Anthropic in a 2026 reproducible benchmark; moving volatile content to the end cut input cost 82% / 68–73% respectively. Manus calls KV-cache hit rate "the single most important metric for a production-stage AI agent" (input:output ≈ 100:1; Sonnet cached $0.30 vs $3/MTok — via secondary source).
- Worked example: 10-turn agent session on 128K context — resend $3.93 vs cache $0.95 vs RAG $0.33 (DigitalOcean). Caching ~4× cheaper than resending; retrieval ~12×.

**2. Model routing — the 70/20/10 rule.** Route 70% of traffic to nano/flash tier, 20% mid, 10% frontier. Requesty's worked math: moving off Claude Opus 4.8 to 70% Flash ($0.30/M) + 20% Sonnet ($3/M) drops average cost **$15 → ~$2.10/M tokens (86%)**. This repo's own evidence: Kimchi's cost-per-task routing saved **2.5x vs Claude**; a 70x token spread between models on one identical eval (Kirschner, VS Code talk); GEPA served GPT-OSS 120B above Claude Opus at **90x lower cost**. Re-benchmark quarterly — cheapest today isn't cheapest next quarter.

**3. Context hygiene — the free lever.** From this repo: `.github/copilot-instructions.md` (highest-ROI single file), standards in the reviewer not the implementer (Pocock), content exclusions, and Exa's 200x (500-char computed highlights vs 100k-char raw pages). From Anthropic's cost post: prompt-audit at model migration — removing "verify twice" (two words) cut per-ticket cost **by a third** on Opus 5 with zero accuracy change; full audit cut 14.6% and *raised* accuracy 5.3%.

**4. Effort calibration.** Anthropic's dial: Fable 5 at low effort 11.5% @ $5.35/task vs 30.9% at max @ $19.00/task — and "a stronger model at low effort can be cheaper than a weaker model working hard" (Fable 5.1 low-effort matched Fable 5 high-effort at a third of the cost).

**5. Deferred/progressive context.** Factory's deferred context engine: **50%+ token savings** via progressive tool disclosure. Don't load context speculatively.

**6. Semantic caching + compression.** GPTCache (semantic cache, Zilliz): 40–70% fewer LLM calls on repetitive workloads (community-reported). LLMLingua (Microsoft Research, MIT): up to 20x prompt compression. leanctx: drop-in SDK claiming 40–60% bill cuts (newer project, smaller community).

## The 2026 Copilot billing reality (for your team)

GitHub moved to **AI Credits** (1 credit = $0.01) on June 1, 2026 — metered on actual tokens at per-model API rates. What matters for a Copilot-standardized team (corroborated across 4+ Sep–Oct 2026 sources; re-verify at docs.github.com):

- **Completions are free and unlimited** on all paid plans — zero credits. Agents, chat, code review, CLI, and Spark are what draw the balance. Business ($19/seat): 1,900 credits/user pooled; Enterprise ($39/seat): 3,900 pooled. A promo that inflated these just stepped down Sep 1, 2026 ("credit cliff").
- **Model spread is ~50x on input.** Documented per-1M rates run from MAI-Code-1.1-Flash ($0.20/$1.20) to Claude Fable 5 ($10/$50). The model picker is a cost lever most teams leave on default. Auto model selection earns 10%; cached tokens bill ~10%; don't switch models mid-session (invalidates cache); run subagents on cheaper models.
- **Budgets are the only hard stop.** Four levels (user / cost-center / org / enterprise); overage is on by default. Set the user-level budget first.
- **Output is the expensive token class** (~5x input): "Code only, no explanation" in copilot-instructions.md is guide-claimed at 40–70% output cuts per code task (anecdotal percentage, sound mechanism).
- **Hooks kill the most expensive failure mode**: PreToolUse/Stop hooks block redundant tool calls and runaway agent loops under credit billing.
- **`/chronicle`** (Copilot CLI) surfaces recurring patterns — encode them into copilot-instructions.md once instead of re-paying per session.

## The open-source toolstack (router → observe → compress)

| Layer | Pick | Why | Repo |
|---|---|---|---|
| Router/gateway | **LiteLLM** | 100+ providers, cost-based routing, per-team budgets; the default OSS pick | github.com/BerriAI/litellm |
| Router (fast) | **Bifrost** | Go gateway, <100µs overhead, when Python proxy is the bottleneck | github.com/maximhq/bifrost |
| Observability | **Langfuse** | Per-request token+cost tracing, self-hostable (MIT) | github.com/langfuse/langfuse |
| Observability | **Opik** | Tracing + agent optimizer that compounds into lower per-task spend (Apache-2.0) | github.com/comet-ml/opik |
| Dev spend visibility | **ccusage** | CLI reporting per-dev coding-agent spend from on-disk data | github.com/ryoppippi/ccusage |
| Pre-call estimating | **tokencost** | Dollar cost before you call, for routing logic | github.com/AgentOps-AI/tokencost |
| Compression | **LLMLingua** | Up to 20x prompt compression (Microsoft Research, MIT) | github.com/microsoft/LLMLingua |
| Semantic cache | **GPTCache** | Near-duplicate queries never hit the model (Zilliz) | github.com/zilliztech/GPTCache |

Acquisition notes: Portkey (gateway) → Palo Alto Networks; Langfuse → ClickHouse; Helicone → Mintlify (maintenance mode — use for the logging pattern, not as a forward bet). Continue (coding assistant) → Cursor, repo archived — do not standardize on it.

## Local CLI complements (the Copilot-adjacent stack)

Keep engineers in VS Code; move metered agentic burn off Copilot credits where it makes sense:

- **Ollama** (ollama.com) — local model runner, OpenAI-compatible API, zero marginal token cost. Best local coding models in 2026 guides: Qwen2.5-Coder 7B/14B/32B (Apache 2.0), DeepSeek-Coder-V2-Lite, Codestral 22B. Honest scope: great for completions, test scaffolds, docstrings, lint fixes, eval judges — weak at multi-file refactors and agentic loops vs frontier.
- **Aider** (github.com/Aider-AI/aider) — git-native pair programming, BYOK, local-capable. Its **Architect mode** is the canonical cheap/expensive split: strong model plans, cheap model writes the edits.
- **Cline / Roo Code / Kilo Code / Goose / Crush** — VS Code-native or terminal agents with BYOK and local-model support; Goose is Apache-2.0 and local-first with MCP + hooks.
- **The pattern teams run:** Copilot completions (unlimited/free) + Aider/Cline pointed at a cheap API or local model for agent work. Same UI, metered burn moved.
- **vLLM for team serving:** breakeven ≈150–200 req/hr; ~70% cheaper than hosted volume at 500+/hr — but idle GPU time destroys the economics, and GPU ops is real work.

## Reading list (the 12)

1. Anthropic, "Reducing cost and improving performance with Claude Platform" (2026-09-08) — claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform
2. GitHub, "How we make AI coding more cost efficient without sacrificing task quality" (Sep 2026) — github.blog (already a deep dive in this repo)
3. PwC AI Research, "Don't Break the Cache" (arXiv 2601.06007, Jan 2026) — arxiv.org/abs/2601.06007 ⚠️ secondary-source figures
4. Manus on KV-cache hit rate as the production SLO (2025, canonical) — via tokenbill research notes ⚠️ secondary source
5. theagentloop, "What one agent run actually costs" (DEV, ~Sep 2026) — dev.to/theagentloop/what-one-agent-run-actually-costs-28i8
6. Requesty, "AI Agent Cost Optimization: cut LLM spend 80% with routing" (~Jun 2026) — requesty.ai/blog/...
7. CloudZero, "LLM cost optimization: 7 strategies" (Jul 2026, upd. Sep 2026) — cloudzero.com/blog/llm-cost-optimization/
8. DigitalOcean, "What it actually costs to serve a 1M-token model" (DEV, ~Sep 2026) — dev.to/digitalocean/...
9. Manveer Banxal, "AI Agent Cost per Month: the token maths, worked out" (DEV, Oct 2026) — dev.to/manveer-banxal/...
10. Brinvik, "A better model, a 36% bigger bill, an unread prompt" (Sep 2026) — brinvik.com/en/journal/claude-ai-costs-prompt-audit
11. ravoid.com, "Stop asking RAG vs fine-tuning. Ask this." (~Sep 2026) — ravoid.com/blog/rag-vs-fine-tuning-cost/
12. sedai77/tokenbill — open-source agent cost profiler with graded evidence — github.com/sedai77/tokenbill-llm-agent-cost-profiler

## What to do Monday morning (sequenced for a Copilot team)

1. **Set user-level budgets** in Copilot (the only hard stop) and check where the Sep 1 credit step-down left you.
2. **Write the team `copilot-instructions.md`** — output discipline ("code only" defaults), path-scoped sections, landmines only. One afternoon.
3. **Measure cost per successful task** for two weeks on one repo (ccusage for dev-level visibility; Langfuse/Opik if you want team dashboards).
4. **Run the model-routing eval**: same tasks across Copilot's model picker, score quality vs tokens. Expect a wide spread; set per-surface defaults (cheap for completions, frontier for hard agents).
5. **Pilot the local complement**: Ollama + Aider on one project for the mechanical tier (scaffolds, docstrings, lint fixes) before spending on anything else.
6. **Calendar the re-benchmark**: quarterly model-routing re-run + prompt-audit at every model migration. The Brinvik rule: prompts written for older models carry hidden taxes on newer ones.

## Verification flags

- PwC cache figures (78–80%) and Manus numbers are via secondary sources, not the primaries.
- Requesty/CloudZero percentages are vendor-authored; the arithmetic is explicit but the headlines are marketing-adjacent.
- Copilot credit allowances and per-model rates corroborated across multiple Sep–Oct 2026 sources, but GitHub adjusts flex allotments — re-verify at docs.github.com before quoting internally.
- "40–70% output cut", "70% cheaper self-hosting", local-model benchmark scores: single-source or guide-claimed; mechanisms sound, magnitudes anecdotal.
- tokenbill is the single most useful open-source find for the "open source repo tool" ask: a cost profiler *plus* a graded-evidence research corpus.
