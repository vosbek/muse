# AI Engineer Talks — World's Fair 2026 (Sep 25 – Oct 3)

37 talks from the AI Engineer channel's World's Fair 2026 run, each distilled into thesis, key points, notable quotes/data, and a tokenomics/efficiency angle with local-deploy takeaways where relevant. Three more videos from the same window were already covered elsewhere in the repo (see bottom).

Provenance: 21 notes are transcript-based (full spoken transcripts via usetranscribe.io); the rest are distilled from video descriptions/chapters plus biggo.com's AI-generated talk summaries — each file carries an exact provenance note at the top. Treat secondary-derived points as the speaker's arguments per those summaries, not verbatim transcript.

## The talks

| Talk | Speaker | Date | Sharpest takeaway |
|---|---|---|---|
| [Stop Fine-Tuning to Fix Retrieval Problems](stop-fine-tuning-retrieval.md) | Anant Srivastava | Oct 3 | Fine-tune only what has stopped changing; the rest belongs in retrieval or the prompt. |
| [What Makes Open Models Fast in Production](open-models-fast-production.md) | Sujee Maniyam, Nebius | Oct 3 | KV-cache prefix reuse → up to 10x speedup; custom draft models → 30%+ on speculative decoding. |
| [GPU Died. Training Didn't: Self-Healing Training at Scale](self-healing-training.md) | Connor Guerrero & Young Jeong, Crusoe | Oct 3 | XID 79 → drain, replace, resume from checkpoint in under 15 min, no human action. |
| [An Interaction Is All You Need](interaction-is-all-you-need.md) | Ivan Leo, Google DeepMind | Oct 3 | Server-side interaction state + persistent sandboxes + credential-injecting proxy so agents never see tokens. |
| [I Built a Personal AI Agent on a Raspberry Pi](raspberry-pi-agent.md) | Jeremy Adams, Neo4j | Oct 3 | Old Pi 4B + NanoClaw + WhatsApp + Neo4j POLE graph: cloud brain over the wire, local graph on device. |
| [How VS Code Went from Monthly to Weekly Releases with AI](vscode-weekly-releases.md) | Harald Kirschner | Oct 3 | 70x token spread between models on an identical 5-char-file eval — token efficiency is a selection criterion. |
| [Your LLM App Returned 200 OK. It Was Still Wrong.](llm-app-200-ok-wrong.md) | Marina Petzel, Datadog | Oct 2 | Golden signals say the app is up; you need cost, safety, and quality pillars to know it's right. |
| [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent](yolo-mode-microvm-sandboxes.md) | Rowan Christmas, Docker | Oct 2 | 5 prompts took Claude Code from browser history to real bank accounts — protection belongs at the microVM boundary. |
| [The 5 Levels of Self-Driving Production](self-driving-production.md) | Eric Schwartz, Traversal | Oct 2 | RCA is a causal-ML problem, not an observability problem (Amex: 3-min dispatch vs 60-min war rooms). |
| [Lessons from Generating 12 Trillion Synthetic Tokens](12-trillion-synthetic-tokens.md) | Bogdan Gaza, DatologyAI | Oct 2 | 12T tokens was won on plumbing, not recipe: metadata 11 days → 2 hrs, vLLM flag tuning → +40%. |
| [Why AI Didn't Actually Make You Ship Faster](why-ai-didnt-ship-faster.md) | Gabriel Spencer-Harper, Meticulous | Oct 2 | Generation is solved; verification is the bottleneck — invert testing to record-replay-diff. |
| [Why 99% Accurate Browser Agents Still Fail](browser-agents-99-percent.md) | Derek Meegan, Browserbase | Oct 2 | "Cost accumulation is continuous, while value realization is terminal" — measure per transaction, not per run. |
| [Stop Rationing Tokens: Let the Harness Pick the Model](harness-picks-model.md) | Žilvinas Urbonas & Laurent Gil, Cast AI | Oct 2 | Cost-per-task routing saved 2.5x vs Claude while token volume grew 1.5x; autonomous re-benchmarking catches model drift in weeks. |
| [Your Coding Agent Is 6 Months Out of Date](coding-agent-out-of-date.md) | Jakub Hojsan, Exa | Oct 2 | Instruct the agent *when* to search; feed ~500-char computed highlights, not 100k-char pages (~200x token cut, zero latency). |
| [MCP Doesn't Suck. Your Agent Does.](mcp-doesnt-suck.md) | Jan Čurn, Apify | Oct 2 | Context bloat is a harness bug, not a protocol bug: "MCP plus CLI is the best." |
| [Stop Renting Your AI's Memory](stop-renting-memory.md) | Dylan Couzon, Qdrant | Oct 2 | Owning inference buys autonomy; owning memory buys continuity — 92 objects, 300+ vectors, 15MB, <1ms, fully offline. |
| [The State of AI in Software Development: Data from 400+ Orgs](state-of-ai-dev-400-orgs.md) | Justin Reock, DX | Sep 30 | Median +7.7% PR throughput, nobody hit 2x; "an hour saved on something that isn't the bottleneck is worthless." |
| [The Chief AI Officer: Scientist, Architect, Coach](chief-ai-officer.md) | Rania Khalaf, WSO2 | Sep 30 | The role is three sliders; she refused to track tokens: "it's so easily hackable." |
| [The Death of the Code Review: What the Data Actually Says](death-of-code-review.md) | Laurie Voss, Arize AI | Sep 30 | 741% more code written, 30% more shipped — stop reviewing PRs; design the review harness instead. |
| [Your Agents Are in Solitary Confinement](agents-solitary-confinement.md) | Vlad Luzin, Band | Sep 30 | Parallel sessions make you a human router; coordination needs conversation-level primitives, not more plumbing. |
| [AI-Generated Code Is Already Competing With Human Code](ai-code-competing-human.md) | Daksh Gupta, Greptile | Sep 27 | ~25% of 1M+ monthly PRs largely AI-generated (from <1%), at or above human quality on reverts/P0s/review cycles. |
| [Get Out of the Model's Way](get-out-of-models-way.md) | Kevin Hou, Google Antigravity | Sep 27 | "Scaling with intelligence": ship primitives that get better as models do — dynamic subagents, sidecars, generative UI. |
| [GLM-5.2: Open Weights, Near-Frontier Intelligence](glm-5-2-open-weights.md) | Zixuan Li, Z.ai | Sep 27 | Between Opus 4.7 and 4.8 on long-horizon coding; MIT-licensed, 1M context, vLLM/SGLang. |
| [Orchestras, Not Factories: How the Fastest Builders Work](orchestras-not-factories.md) | Charlie Holtz, Conductor | Sep 27 | "Don't beat the market": invest only where you hold proprietary alpha; vendors commoditize the rest. |
| [Scale the Judgment, Not the Model](scale-the-judgment.md) | Andrew Orobator, Reddit | Sep 27 | $1.26/PR flag-cleanup agent vs $26k+/yr by hand — "The model wrote the code and I wrote the judgment." |
| [No, That's Not a Software Factory](not-a-software-factory.md) | Ryan Cooke, WorkOS | Sep 27 | Sandbox + agent + prompt ≈ Claude Code on laptops; the real factory encodes processes and measures outcomes. |
| [What It Actually Takes to Build a Software Factory](what-it-takes-software-factory.md) | Tereza Tížková, Factory | Sep 27 | Model routing saves ~25%+; deferred context engine (progressive tool disclosure) saves 50%+ of tokens. |
| [I Turned Coding Agents Into a Strategy Game](coding-agents-strategy-game.md) | Ido Salomon, AgentCraft | Sep 27 | The bottleneck is human supervisory bandwidth — and the skills already exist, from RTS games. |
| [Building Self-Improving Agent Software Factories](self-improving-factories.md) | Suraj Gupta, Warp | Sep 27 | Best-at-k "eval sidecar": "UI tasks are really well done with GLM. We don't really need to run those with Opus." |
| [We Let Claude Code and Codex Race Human Researchers](claude-code-codex-race.md) | Elie Bakouch, Prime Intellect | Sep 26 | Per-output-token flips the winner (Kimi most efficient); zero novel optimizers emerged — a telling ceiling on recursive self-improvement claims. |
| [Beating RL With Reflection: GEPA and Optimize Anything](gepa-optimize-anything.md) | Lakshya A. Agrawal, GEPA | Sep 26 | One reflection round on 3 examples beat GRPO's 25,000 rollouts 2x; Databricks: GPT-OSS 120B > Claude Opus at 90x lower cost. |
| [Long-Horizon Agents Need Experiments, Not Just Prompts](long-horizon-agents-experiments.md) | Erina Karati, Supercell | Sep 26 | RAG alone can't fix social decay — optimize the agent *protocol* via autoresearch meta-loop with ratchet semantics. |
| [How We Built an Agent That Improves Itself](agent-that-improves-itself.md) | Zubin Aysola, Weights & Biases | Sep 26 | Bit-wise identical agent in prod and sim; every production trace becomes an offline YAML eval task. |
| [Autoresearch Made Our Models 3x Faster](autoresearch-3x-faster.md) | Tejas Bhakta, Morph | Sep 26 | Human ideas + autoresearch verification + billions of tokens; ~80% of attempts are bad — reward hacking is the real problem. |
| [An AI Research Agent That Runs Your Experiments](ai-research-agent-experiments.md) | Tim Sweeney, Weights & Biases | Sep 26 | Expediency as an eval (results within 6 tool calls) makes cost control a correctness criterion. |
| [The Loop Is the Product](loop-is-the-product.md) | Roland Gavrilescu, Introspection | Sep 26 | System distillation is the moat — failure patterns→evals, behaviors→skills, frustrations→harness — baked into versioned git "agent recipes"; "valued work per watt" is the unit economics. |
| [Fixing the PR Bottleneck](fixing-pr-bottleneck.md) | Matt Pocock, AIHero | Sep 25 | Coding standards belong in the *reviewer* subagent, never in AGENTS.md — red-green-refactor across two context windows; a "retro" skill compounds every review into new checks. |

## Already covered elsewhere

- [Dashboards Are Dead](../deep-dives/dashboards-are-dead.md) — Sarah Simionescu, Composio (Oct 3) — deep dive with screenshots.
- [Software Engineering Is Becoming Factory Engineering](https://www.youtube.com/watch?v=tUPPVhBBcoM) — Zach Lloyd, Warp (Sep 27) — covered as an enterprise HTML distillation (`factory-engineering-zach-lloyd.html`).
- [Teaching LLMs to Speak Spotify](../deep-dives/spotify-shunt.md) — Yves Raimond & Jacqueline Wood, Spotify — deep dive (routing agent I/O to cheap models via hooks).
