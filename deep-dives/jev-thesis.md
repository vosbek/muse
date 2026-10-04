# The Jev thesis — TypeSafe's System One Models

**What it is.** The founding document of the Jev wave: TypeSafe AI's launch post by founder Diogo Almeida (ex-OpenAI, where he helped build the methods behind ChatGPT). After four years asking "where is all the automation?", his answer is a new model class — **System One Models** — with **Jev** as the first public model. (I could not locate the 12-page "how to use Jev with LLMs" PDF mentioned in the bookmarks; this dossier is built from the official launch post, which states the full thesis.)

**How it works — the core mechanism.** Existing LLMs are trained with RLHF/RLVR to produce *strings humans prefer*; Jev is trained with **Reinforcement Learning for Calibrated Decisions (RLCD)** to produce *typed, probabilistic decisions software can use directly*. The differences that matter:

- **Inputs:** unstructured state (emphasis on structured program state, not chat messages).
- **Outputs:** type-safe structured values, never strings. Possible outputs are defined in advance — no type errors, mathematically impossible to hallucinate.
- **Sampling:** parallel, not autoregressive. All outputs in a single query — this is where the speed comes from.
- **Confidence:** every answer ships with calibrated probabilities. Higher confidence actually means higher accuracy — the property that makes automation possible without a human in the loop.
- **Question types:** Choice (pick among options), Score (rate), Noul (yes/no) — the vocabulary of "smart if-statements": classify, route, score, extract, branch.

**Key numbers (TypeSafe's claims, with their own caveats).** Input tokens **$0.042/MTok** ($42 per billion); **output tokens free** ("too cheap to meter"). Latency **70–500ms** (claimed 40–200x faster than frontier models at the same intelligence on decision tasks). Workflow evals claim up to **193.6x faster / 444.6x cheaper** — TypeSafe themselves flag these as the high end of real-world gains, measured against GPT-6 Astra and Fable 5.1 as reference. The name is a double homage: Kahneman's System 1 thinking, and William Stanley Jevons — of the **Jevons paradox**: every order-of-magnitude drop in the cost of intelligence unlocks orders of magnitude more use cases.

**Why it matters for tokenomics / context management.** This is the foundational bet behind half the playbook: *stop paying frontier models to make yes-or-no decisions.* Every classify/route/score/verify/guardrail step in an agent loop currently burns frontier tokens (and frontier latency) on work a $42/B-token decision model does as well or better, with calibrated confidence the LLM never had. The deployable pattern: keep the frontier model for generation and judgment, route every structured decision through Jev (or an open clone), and watch the per-task cost collapse. The Jevons-paradox framing is also the strategic warning — savings get reinvested as volume, so budget on cost-per-outcome, not cost-per-token.

**Links.** Launch post: https://typesafe.ai/blog/introducing-system-one-models-and-jev · Workflow evals: evals.typesafe.ai (linked from the post) · API docs: docs.typesafe.ai (linked from the post).
