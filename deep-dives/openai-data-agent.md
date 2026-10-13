# Inside OpenAI's In-House Data Agent: Six Layers of Context

**What this is:** OpenAI's engineering blog post "Inside OpenAI's in-house data agent" (January 29, 2026 — Bonnie Xu, Aravind Suresh, and Emma Tang, Head of Data Platform Engineering), surfaced via @askdatadawn's Oct 12, 2026 reel. It's the clearest public account of how a frontier lab grounds an analytics agent in enterprise context: not a better model, but six layers of pre-computed context underneath a single model. Distilled here in my own words; the article is the primary source throughout.

**Related:** [WikiSkill](../03-agent-memory/README.md) (Google's skill-evolution memory) · [Unblocked relational context engine](../ai-engineer-talks/) (deterministic context assembly) · 02's context-engineering entries (the retrieve → select → filter → build pipeline)

**Thesis:** at 70,000 datasets, the hardest problem isn't writing SQL — it's finding the right table. An agent with perfect SQL and no table knowledge fails; an agent with imperfect SQL and rich context succeeds.

## The setup

OpenAI's data platform serves 3,500+ internal users across engineering, product, and research, spanning 600+ petabytes across 70,000 datasets. Their answer was a bespoke internal-only agent (not a product) that takes employees from question to insight in minutes instead of days. It runs on GPT-5.2 with a small toolset, built with Codex, the Evals API, and the Embeddings API — and it's available wherever employees already work: Slack, a web interface, IDEs, Codex CLI via MCP, and their internal ChatGPT app.

The agent handles analysis end-to-end and reasons in a closed loop: if an intermediate result looks wrong (zero rows from a bad join, say), it investigates, adjusts, and retries on its own — carrying learnings forward between steps instead of pushing the iteration back onto the user. Recurring analyses get packaged into reusable workflow instruction sets (weekly business reports, table validations) so the context is encoded once and reused.

## The six layers of context

The article's core claim: high-quality answers depend on rich, accurate context, and schema metadata alone doesn't cut it. Six layers, paraphrased:

1. **Table usage.** Schema metadata (columns, types) plus lineage (upstream/downstream relationships) plus *query inference* — ingesting historical queries to learn which tables get joined together and how people actually write against them.
2. **Human annotations.** Curated descriptions from domain experts capturing intent, business meaning, and known caveats that can't be inferred from schemas or past queries.
3. **Codex enrichment.** The distinctive one: Codex reads the pipeline code that *created* each table — Spark jobs, Python transforms — to learn what the data actually contains: how values are derived, uniqueness, update cadence, granularity, scope. This lets the agent distinguish tables that look identical in schema but differ critically (e.g., whether a table covers only first-party traffic), and it's refreshed automatically so it never goes stale.
4. **Institutional knowledge.** Slack, Google Docs, and Notion — launches, incidents, internal codenames, canonical metric definitions — ingested, embedded, and stored with metadata and permissions, served through a retrieval layer that enforces access control at runtime.
5. **Memory.** Corrections and discovered nuances get saved for next time — global and personal scope, user-editable. The point is retaining the non-obvious filters and constraints that matter for correctness but can't be inferred from the other layers (their example: an experiment-gate filter keyed on a specific string the agent could never have guessed).
6. **Runtime context.** When no prior context exists or it's stale, the agent issues live probing queries against the warehouse to inspect the table directly, and can talk to other platform systems (metadata service, Airflow, Spark) as needed.

The cost architecture matters as much as the layers: a **daily offline pipeline** aggregates the first three layers (table usage, human annotations, Codex enrichment) into one normalized representation, converts it to embeddings, and stores it for retrieval. At query time the agent pulls only the relevant embedded slice via RAG instead of scanning raw metadata — so table understanding stays fast across tens of thousands of tables and runtime latency stays predictable. Context is pre-computed offline; only the last mile is live.

## Evaluation and trust

Because an always-on, evolving agent can drift as easily as it improves, the team built evaluation in from the start: curated question-answer pairs, each targeting an important metric or analytical pattern, paired with a manually authored "golden" SQL query. Each eval sends the natural-language question to the agent, executes the generated SQL, and compares both the SQL and the result data against the golden query via an Evals grader — deliberately not naive string matching, since syntactically different SQL can be equally correct. The evals run continuously like unit tests, catching regressions as canaries.

Security is pass-through: the agent inherits the user's existing data permissions and can only query tables that user could already access.

One early lesson the article names: **less is more** — they started by exposing the full tool set and hit overlapping-functionality confusion, so they restricted and consolidated tool calls to reduce ambiguity for the agent.

## Tokenomics / enterprise angle

Four things worth stealing, in cost order:

1. **Pre-compute context offline; retrieve at query time.** The daily pipeline is the economic insight: the expensive work (reading pipeline code, aggregating query history, embedding everything) happens once per day as batch compute, and each query pays only for retrieving a relevant slice. This is the same shape as prompt caching and the Jev routing ladder — move cost out of the hot path.
2. **Memory is a cost lever, not just a quality lever.** The reel's headline demo (22:47 without memory → 1:22 with it) is the creator's illustration, but the mechanism is the article's: a saved correction means the agent starts from the right table and the right filter instead of re-deriving them at full price every time. Memory amortizes reasoning.
3. **Finding beats writing.** The article is explicit that table discovery is the time sink, not SQL generation. For enterprise agent budgets, that reframes where to spend: invest in the retrieval and enrichment layers (cheap, offline, shared across all users) rather than in a bigger model for the generation step.
4. **Evals are the trust budget.** Continuous golden-SQL evals are what let the agent evolve without silent regressions — the same "score, don't gate" pattern as the dark-factory entry, applied to a data agent. The eval suite is the fixed cost that makes the variable spend safe.

## Honest scoring

This is OpenAI describing its own system — the numbers (3,500 users, 600 PB, 70k datasets) and the architecture are first-party claims without independent verification. No cost figures are published, so the tokenomics above is inferred from the architecture, not measured. The 22:47 → 1:22 memory demo comes from the reel creator's retelling, not the article text. Secondary coverage (VentureBeat) adds color — two engineers, three months, Codex generating most of the agent's code — but that's reporting, not the source. The six layers themselves are the durable artifact: a concrete, replicable pattern regardless of whose numbers you trust.

**Source article:** https://openai.com/index/inside-our-in-house-data-agent · **Reel:** https://www.instagram.com/reel/DeZT_uahXdM/ (@askdatadawn, Oct 12, 2026)
