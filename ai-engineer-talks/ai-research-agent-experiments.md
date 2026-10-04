# Talk Notes: "An AI Research Agent That Runs Your Experiments" — Tim Sweeney, Weights & Biases

**Video:** [An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases](https://www.youtube.com/watch?v=hd7TOvmyAxU) · AI Engineer channel · Sep 26, 2026 · 21:15 · Recorded at AI Engineer World's Fair 2026

**Note:** distilled from the full spoken transcript (read via usetranscribe.io); secondary sources are marked where used.

## Thesis

W&B's ARIA ("AI research and iteration agent") is a research agent that runs your experiments for you: on stage it autonomously ran 200+ experiment batches in a Karpathy autoresearch loop (downloading code, provisioning GPUs via W&B Launch on CoreWeave, iterating on code and hyperparameters), while also serving as a data-science companion (summarizing runs, finding patterns, writing W&B reports/workspaces) — and the same Weave-based loop the team uses to build ARIA itself (production traces → tasks-as-unit-tests → nightly evals → improvement loop → registry promotion) is the blueprint it offers agent builders.

## Key points

- **Three-part agenda** for three personas (ML researchers, applied engineers, AI managers): (1) ARIA itself + live autoresearch demo; (2) how W&B + CoreWeave built ARIA; (3) tips for productionizing agents.
- **W&B context:** 9 years in business, joined the CoreWeave family ~a year ago; known for the models/training/inference + Weave stack — collecting data about AI/ML workflows and making it actionable.
- **Demo setup:** a W&B workspace with 200+ training jobs and a scatter plot of declining loss; grounded on Karpathy's autoresearch project (a simple LLM-training codebase ideal for iterative improvement).
- **Live on stage:** "please conduct another batch of experiments… we're hoping to find the best model live." ARIA reasoned "I don't want to make a big architecture swing, that feels too risky," chose hyperparameter modifications, and kicked off shell calls running the experimentation loop — with a live Kubernetes terminal showing real GPU execution ("this is not a fake demo"), then polling for completion.
- **ARIA as data-science companion:** "summarize the highest-performing runs" (onboarding/PTO catch-up); "find patterns in this research" — it identified a newly emerged model family, batch size as a high-leverage parameter, and a promising architectural recipe ("insights that would have taken me hours or days"); emits W&B reports ("markdown on steroids" with embedded plots — it chose the esoteric parameter-importance chart) and builds workspaces/plots with W&B's proprietary charts.
- **Launch announcements:** ARIA went GA the Monday before the talk and shipped in the **W&B iOS app** — steer hyperparameter tuning from your phone ("go touch grass at Yerba Buena gardens").
- **Vision:** a fully automated end-to-end research platform that complements rather than replaces researchers — ARIA orchestrates jobs, understands GPU workloads, responds to W&B-ecosystem events, looks up arXiv papers, and collaborates on hypotheses. "Let ARIA drive the mechanics you don't want to deal with while you focus on new ideas."
- **Backend (archetypal agent stack):** web + iOS clients → API server → trace DB → worker harness ("magic box") wired to: (a) sandbox for arbitrary shell/Python (recommends the CoreWeave×W&B sandbox); (b) an LLM provider (e.g., GLM 5.2 or fine-tuned models via W&B Inference); (c) W&B Launch for long-running workloads (days-long training) on CoreWeave GPUs; (d) Weave observability — 100% of traces logged.
- **Building ARIA itself:** Weave traces → insights → "tasks" (unit tests for models) → nightly eval loops; model registry via W&B artifacts; eval results in Weave on a shared dashboard for go/no-go on prompt/architecture changes → the **"improvement loop"** (hypothesize → implement candidates → analyze evals). Two complementary-yet-adversarial offline research loops feed Weave data until the best model is promoted to production — closing the data flywheel.
- **Weave agent dashboard:** span volume, conversation volume, token tracking (bird's-eye view); live conversations feed (filtered to internal employees in the demo); spans view showing trace topology (tool calls, LLM calls, thinking blocks as colors/shapes); per-conversation detail (system prompt, user message, shell calls, reasoning blocks) where the research lead, PM, and Tim annotate with notes/feedback/emojis to discover behavioral nuances → new tasks.
- **ARIA analyzing ARIA:** "summarize" buttons throughout the W&B app open contextual chats — ARIA analyzes ARIA's own conversations to recommend ARIA improvements, all in-UI.
- **Weave "signals":** integrated LLM judges on live traffic — user-frustration, low-quality-response, ask-user signals — clustering behaviors to fix next iteration, with the judge's live reasoning visible (e.g., "I'm not satisfied with the loss curve, it looks bad" → frustration flag).
- **Tasks = YAML files = unit tests for models:** example prompt ("check this run and that run… what's the difference?") + metadata + an LLM judge defining correctness + a second LLM judge scoring "are the insights actually interesting" + a rule-based judge (result within 6 tool calls — expediency). ~200 tasks in a nightly suite tracked in Weave; two nights before the talk the candidate scored **73% vs prod 72%** → "definitely going to push that forward this Friday."
- **Weave workflow recap:** (a) collect ALL production traffic; (b) generate insights (humans + ARIA + LLM judges); (c) enrich tasks; implement; evaluate on the shared dashboard; promote the best model with confidence.
- **Tips for managers:** (1) invest in agent-oriented observability — log sessions, turns, tools, feedback — to catch "behavioral bugs" (not exceptions or perf, but behavioral); (2) tasks and evals are the new CI — researchers on the same scrum team writing tasks, metrics as go/no-go — BUT keep humans as necessary judges (LLMs miss behavioral nuances; the team reviews best/worst traces weekly); (3) add value through context and tools — don't overengineer the harness with memory tricks; low-hanging fruit is giving the agent business-domain context, primitives, and data.
- **Live result:** previous best loss 5.831 (lunchtime) vs 5.833 from the on-stage batch — "right on the edge of having a live improvement, pretty darn close"; 12 experiments ran in that batch, "more all night."

## Notable quotes & data

- "Tasks and evals are the new world of CI."
- "Behavioral bugs — not exceptions, not performance, but behavioral bugs."
- "Let ARIA drive the mechanics that you don't want to deal with while you focus on new ideas."
- Candidate 73% vs prod 72% on nightly evals → ship Friday; 200+ training jobs; 12 experiments in the live batch.

## Tokenomics / efficiency angle

- Token tracking is a first-class dashboard metric (span volume, conversation volume, token tracking).
- Expediency is an eval criterion: a rule-based judge requires results within 6 tool calls.
- W&B Launch + CoreWeave GPUs back long-running workloads; the efficiency story overall is eval-driven iteration (nightly evals, 200 tasks, go/no-go promotion).

## Local-deploy takeaways

- Make token usage and tool-call counts first-class dashboard metrics and eval criteria — an expediency judge ("solved within N tool calls") forces the agent to stay cheap, not just correct.
- The tasks-as-YAML pattern needs no Weave: prompt + metadata + judge + tool-call budget is a local nightly eval suite.
- Biggest local leverage: don't overengineer the harness with memory tricks — give the agent domain context, primitives, and data instead.

## Sources

- Video page: https://www.youtube.com/watch?v=hd7TOvmyAxU
- Full transcript: https://www.usetranscribe.io/yt/hd7TOvmyAxU/arya-ai-research-agent
