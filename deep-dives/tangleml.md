# Tangle — Shopify's open-source experimentation platform

**What it is.** Tangle (tangleml.com) is Shopify's open-source, platform-agnostic ML experimentation platform: a drag-and-drop visual pipeline editor where you wire components into graphs and run them locally or in the cloud. It's the substrate behind the "self-improving loops" story — Tobi Lütke's post about open-sourcing "the core infra piece that makes these self improving loops possible."

**How it works.** Components are **containerized CLI programs in any language**; they exchange data as files (CSV, Parquet, JSON). You compose them the way shell scripts and pipes compose. Three properties make it loop-friendly:

1. **Content-based execution caching** — intermediate results are cached, including steps still in flight, so iteration is fast and cheap; rerunning a pipeline skips everything already computed.
2. **Everything persisted forever** — every run stores its graph, components, and logs. Teammates can inspect, copy, and modify a pipeline in seconds with no environment-parity pain (the "works on my machine" problem disappears because the run *is* the environment).
3. **Visual, shareable, reproducible** — closer to Kubeflow/Airflow in purpose, differentiated by the caching model and the editor.

**The self-improving loop it enables.** The pattern (Karpathy's AutoResearch, which Tobi adapted as pi-autoresearch): an agent proposes experiments → runs them in containerized isolation → keeps what improves a metric → iterates. The famous demo: PR #2056 against Shopify's Liquid templating engine — **93 commits from ~120 automated experiments**, parse+render time **7,469 → 3,534μs (53% faster)**, allocations **62,620 → 24,530**, all 974 unit tests passing. Caveats Tobi himself published: the PR was **never merged** and is **"probably somewhat overfit"** — the agent optimized hard against one benchmark, and real-world gains may be smaller.

**Why it matters for tokenomics / context management.** Two lessons. First, the *outer loop* (improving the system from execution traces — Uber's "continuous skill optimization" is the same idea) is where compounding returns live, but it must be **metered**: every experiment burns tokens, so loops need budgets and held-out metrics, or you get overfit theater. Second, Tangle's caching is the cost-control primitive for loops — content-based dedup means the 50th experiment doesn't repay the compute of the first 49. If you're building the "skill-improvement loop" from the factory talk, this is the reference architecture: containerized steps + content cache + full run persistence = auditable, cheap iteration.

**Links.** https://tangleml.com · Background: https://www.linux.com/news/shopifys-tangle-and-tangent/ · The Liquid PR story: https://www.techtimes.com/articles/316804/20260519/karpathys-autoresearch-loop-spreading-fast-shopifys-53-speed-claim-still-unmerged-flagged.htm.
