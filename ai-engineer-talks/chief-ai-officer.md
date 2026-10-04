# Talk Notes: "The Chief AI Officer: Scientist, Architect, Coach" — Rania Khalaf, WSO2

**Video:** [The Chief AI Officer: Scientist, Architect, Coach — Rania Khalaf, WSO2](https://www.youtube.com/watch?v=9cJrbj23fOA) · AI Engineer channel · Sep 30, 2026 · 22:21 · Recorded at AI Engineer World's Fair 2026

**Note:** YouTube's transcript was unreadable in our environment, so this is distilled from the video's own description/chapters plus biggo.com's AI-generated talk summary — treat secondary-derived points as the speaker's arguments per those summaries, not verbatim transcript.

## Thesis

The CAIO role barely existed five years ago and is proliferating faster than anyone can define it (IBM: **11%** of orgs in 2024 → **26%** in 2025 → **76%**); it isn't one job but a spectrum — **Scientist** (explore/experiment/build), **Architect** (strategy/product/budget/board), **Coach** (evangelize/educate) — whose mix is set by company type, workforce technicality, and AI maturity. Because "there's AI in everything," the role is structurally prone to overload; discipline in focus areas and refusing gameable metrics (she refused to track tokens: "it's so easily hackable") separate a functioning AI function from an overwhelmed one.

## Key points

- The title "means drastically different things based on two criteria": **company type and AI maturity** — plus a third, **the skill set of the person in the seat**. Recruiters show unusual open-mindedness, shaping the mandate around whoever they find; the role sometimes splits in two.
- "It's so great. OK, I have an AI officer. But there's AI in everything, right? It's kind of like saying digital or, I don't know, electricity. It's in everything, and it can be so many things, and it can be really overwhelming."
- **Credibility:** 20 years at IBM Research (ran ~a third of the global research AI org); then a CAIO-type role at a Cambridge-area ag biotech unicorn doing CRISPR on corn/soy/wheat (validating one gene edit took **10 years** and "a ton of land"); now WSO2 — ~20 years old, **~$150M ARR**, fully open source (not open core), API/integration/IAM/IDP portfolio across **90+ countries**.
- **The three sliders, each a range:**
  - **Scientist** — from exploring heavily (no PhD required) to creator/inventor of new algorithms; some part of the team must always be experimenting, "there's no way around it."
  - **Architect** — from business steward (holds budget, evaluates/prioritizes/project-manages; deep AI knowledge optional) to strategy shaper (reinvents productivity, product strategy, GTM; she reports to the board).
  - **Coach** — from inward enablement at non-AI-product companies to outward trusted-advisor work as maturity grows.
  - She validated the framework by running real CAIO resumes/postings through Claude and Gemini: "really it's the person."
- **Counterintuitive finding:** some companies deliberately staff a business steward who deeply understands the business rather than an AI expert (prompted by an "AI education for Chief AI Officers" marketing email she first balked at).
- **Coaching pedagogy:** "you can explain until you're blue in the face, but people don't believe it until they experience it" — hence letting employees discover hallucination themselves rather than lecturing.
- **Biotech war stories:** the mandate sprawled (handed IT, told to hire a CISO, zero data engineers; seed-seller → full AWS, Databricks, Box→Microsoft). The right answer was often not ML: a corn-embryo-size hypothesis needed only **blob detection** — basic computer vision from her master's, no ML — while gene discovery used BERT substantively.
- **WSO2 mix self-reported as ~20% Scientist / 60% Architect / 20% Coach:** small research team; strategy refocused on the "agentic enterprise fabric"; ~75% technical workforce that's "super, super curious," so inward coaching is minimal.
- **Measurement** (asked to track tokens, refused):
  - workforce AI fluency (builders across functions vs. a CoE everyone queues for — WSO2 runs a small central team plus an AI lead in every product);
  - adoption spectrum (email cleanup → full workflow rework → "agentic employees");
  - tool availability; **GEO visibility** (can LLMs find/know the company — "genuinely hard," industry-wide WIP);
  - product (what to build/extend/partner; every product agent-consumable — MCP server, skills, CLI);
  - **agent-proof consumption pricing** ("all SaaS is dead... if you price per seat... what happens when the agents come and blow it out of the water");
  - dogfooding with a closed feedback loop; earned media/analyst recognition/customer use cases; open-source signals (stars, forks); ARR from AI products.
  - "You really get what you measure... everyone's going to optimize for that" — so the list must evolve.
- **WSO2 product moves:** AI gateway added to the API platform; **agent identity** added to the identity platform (human IAM expertise extended to agents); agent-proof consumption pricing; agent builder in the integration platform; **Agent Manager** (newest) for full agent lifecycle.
- **Scientist-side pride:** three publications this year, two co-authored with Sri Lankan undergrads (their first ever; one won a best paper award).
- **Closing counsel:** no silver bullet; requires strong CEO backing and a close CEO relationship; find the intersection of what you're good at, love, the world needs, and can be paid for — and shape the fluid role around it. Structural sightings: CPO = CAIO at AI-forward firms; heads of HR becoming heads of AI at non-software companies ("I don't know how I feel about that" — the room shared her skepticism).

## Notable quotes & data

- "Someone asked me to measure tokens because to see how much AI we do. And I said no. Because it's so easily hackable."
- "Revenue is not the only number that matters, like tokens is not the only number that matters. What you measure should change over time."
- CAIO prevalence: 11% (2024) → 26% (2025) → 76% (IBM studies, one year apart).

## Tokenomics / efficiency angle

- **Explicitly rejects token counts as an efficiency metric** (gameable proxy); substitutes adoption depth, agent-readiness, and AI fluency spread.
- **Consumption-based (not per-seat) pricing** as the defensive response to agent-driven usage exploding consumption.

### Local-deploy takeaways

- **Never let raw token counts be the scoreboard** — Khalaf refused the metric because it's hackable; measure outcomes (adoption depth, fluency spread, review quality) instead, or teams will optimize the counter, not the value.
- **Design pricing and budgets for agent-driven consumption**, not seats: per-seat plans break when agents multiply usage; consumption-based budgets with explicit guardrails are the durable model.

## Sources

- YouTube description/chapters: https://www.youtube.com/watch?v=9cJrbj23fOA
- BigGo AI talk summary: https://finance.biggo.com/podcast/c7e768723256089a
- daily.dev summary post: https://daily.dev/posts/the-chief-ai-officer-scientist-architect-coach-rania-khalaf-wso2-uberqhgkq
