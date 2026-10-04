# Talk Notes: "The Loop Is the Product" — Roland Gavrilescu, Introspection

**Video:** [The Loop Is the Product — Roland Gavrilescu, Introspection](https://www.youtube.com/watch?v=7taOQBfjDyE) · AI Engineer channel · Sep 26, 2026 · 18:43 · Recorded at AI Engineer World's Fair 2026

**Note:** distilled from the full spoken transcript (read via usetranscribe.io); secondary sources are marked where used.

## Thesis

A blueprint for autoresearch in 2026+: three ideas — (1) **the loop is the product** (the progression went RL-for-models → harnesses with commodity models → loops you build instead of code you touch); (2) **system distillation is the moat** (distill each loop's learnings — failure patterns→judges/evals, repeated behaviors→skills/prompts, frustrations→harness extensions — into versioned, portable, provider-agnostic "agent recipes" in git that encode the maker's taste); (3) **valued work per watt is the score** (measure value per unit of compute; the Cursor/Cognition playbook of product→evals→models applies to every vertical).

## Key points

- **From xAI to Introspection:** he and his co-founder left xAI's agent-infra team a few months prior to work standalone on always-on, long-horizon tasks; the talk is about productizing autoresearch at customer scale.
- **Idea 1 — the loop is the product:** the field moved from RL for models (better reasoning) → harnesses (model is a commodity, harness is everything) → loops (build loops, stop touching code).
- **The first viral loop: Clawbot** (original name of OpenClaw) — "AJ" built a car-haggling loop: scrape Reddit for prices/inventory, talk to dealers, pit dealers head-to-head to outbid each other, a verifiable "price is right" check, then lock in the car. It worked — "probably should be a startup."
- **Why loops:** OODA loops (US Air Force, 1970s — fast decision cycles). Models calling tools and taking observations are already trained for this. Strong signals + verifiable work → worker/Claude Code agents; signal quality determines loop success rate, verifier quality calibrates whether success is real. Then "loop the loop": feed the first loop's artifacts into a second loop for continuous improvement.
- **Idea 2 — system distillation is the moat:** every loop emits useful information (harnesses, profiles, evals, models, resources, tools, environment). Keep it portable, versioned, evolving — like "data recipes" in RL (which is how RL got good: recipes against hallucinations and reward hacking → a final data recipe). No equivalent exists for harnesses/AI systems — that's the gap.
- **Agent recipes:** make frontier AI systems reproducible; a moat that compounds over time; not tied to any platform or provider; you own it; model-agnostic. Loops exist to distill systems into recipes. Mapping: failure patterns → judges and evals; repeated behavior → skills and prompts; user frustration → harness extensions and memories. Bundle it all in a git repo = your ongoing strategy for self-improving systems.
- **Introspection** = the tool that generates these recipes ("recipes for introspecting on your system"): built on the Pi harness + Harbor for evals, baked into git repos for versioning — owned by you, managed by your agents. The owner is the "higher taste personality"; agents calibrate to the maker's taste; using someone else's recipe means borrowing their taste.
- **Early release: "Pi recipes"** — a step beyond 2025-era skills: everything needed for a frontier agent (codifying taste into evals, running evals, loops that improve evals, signal processing, right tools per model, harness profiles per model).
- **Idea 3 — valued work per watt:** Cursor and Cognition's playbook — best product → best evals → best models, each artifact feeding the next. Code was first; customer support, legal research, everything follows. Two questions: how do I measure the value, and how do I know I'm getting a good deal on it? You only discover the frontier by running systems in prod — then the research problem is economic viability: don't spend more than the value warrants. Fine-tuning APIs and infra are already abstracted; the missing know-how is codifying taste into evals and validating it in experiments.
- **Taste, precisely:** evals aren't just tests — they're the creator's taste that agents should reproduce and self-improve around. Portability means "making my taste as an artist/developer downloadable — a one-to-one replica of me." RL today = turning tastemakers into environments and evals, then into weights. The worker is the inner loop generating artifacts; taste decides what to change (generating candidates); experiments self-calibrate that taste against production users (maker happy via offline evals AND end users agreeing).
- **Worked example — talent-sourcing agent:** baseline = tools (web search, LinkedIn), subagents (popularized by Codex/Claude Code harnesses), system instructions. Recruiting is taste-driven ("not what is good recruiting, but who considers it good").
- **Step 1 — understand signals:** mine traces for pattern clusters of behavior or user frustration. Example: the agent kept reaching out to big-tech employees; the recruiter wants hidden gems ("you don't want to try to hire John Carmack") — a behavior you'd never think to codify, discovered from traces.
- **Step 2 — calibrate judges/evals:** agents can build the evals (e.g., a trajectory judge: "did the agent contact Google employees instead of finding hidden gems on GitHub?"); the human's job is only to calibrate — "do you agree we should prefer hidden gems?" "You don't need the human to actually build the evals. You need them to calibrate the evals."
- **Step 3 — recipe candidates + prod validation:** offline evals are the easy part; the test is production — do end users agree with your taste? Validate with A/B tests (multi-armed bandit); when users confirm your taste, promote to the next recipe version. Repeat forever: continuously codify taste into an agent that reproduces your service, with users agreeing you have great taste and execution.
- **Takeaways:** (1) the loop is the product — automate yourself as the higher-level judge; second-loop agents apply the same judgment to prod agents; (2) system distillation is the moat — continuously inject taste into workers; the fastest to do it builds a defensible vertical AI company; (3) valued work per watt — is the work valuable, and do the economics make sense (the price delta vs Claude Code is what makes people switch).

## Notable quotes & data

- "The loop is the product… System distillation is the moat… Valued work per watt is the score."
- "Failure patterns should become judges and evals. Repeated behavior should become skills and prompts."
- "You don't need the human to actually build the evals. You need them to calibrate the evals."
- "How do I make my taste as an artist or as a software developer something that anyone can download… a one-to-one replica of me?"

## Tokenomics / efficiency angle

- "Valued work per watt" is the proposed unit economics: value generated per unit of compute/cost; don't spend more than the value warrants; the price delta vs Claude Code is what drives switching.
- Fine-tuning APIs and abstracted infra make the economics accessible — the missing piece is the know-how of codifying taste into evals.
- Multi-armed-bandit A/B testing validates taste in production before promotion.

## Local-deploy takeaways

- Agent recipes are git repos, not platforms: versioned, portable, provider-agnostic, model-agnostic — the most local-first moat in the eight talks. Distill your own failures→evals, repeated behaviors→skills, frustrations→harness extensions.
- "Valued work per watt" is a directly usable metric: for every agent deployment, measure value per unit of compute and cap spend at a fraction of value — this is the cost-control discipline for an enterprise tokenomics remit.
- Let agents build the evals and keep humans as calibrators ("do you agree we should prefer hidden gems?") — calibration is cheap; hand-authoring evals is the expensive part to eliminate.

## Sources

- Video page: https://www.youtube.com/watch?v=7taOQBfjDyE
- Full transcript: https://www.usetranscribe.io/yt/7taOQBfjDyE/ai-loops-and-feedback
