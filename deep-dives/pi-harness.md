# Pi: The Minimal Agent Harness Coinbase and Shopify Are Betting On

**Trigger:** [@sourcerypod reel](https://www.instagram.com/reel/DeRBnnilHgX/) (Oct 9, 2026, 694 likes) — USV's Fred Wilson: Coinbase and Shopify "dumped Claude" and built their own coding-agent harness on the open-source **Pi**. "The CTO and engineering leaders look at it and say, we can't just build everything on top of Claude. We have to have something more flexible that we can evolve with our needs." Wilson identifies himself as an investor in the company behind Pi.

**Note:** this dossier assembles the Pi project (pi.dev, GitHub), the companies' own engineering writing (Coinbase's Mux and Forge posts, Shopify's Helix post), and contemporaneous reporting. Where claims conflict (notably "layers on Claude" vs "dumped Claude"), both are presented with dates.

## What Pi is

**Pi** ([pi.dev](https://pi.dev), [github.com/earendil-works/pi](https://github.com/earendil-works/pi)) is an open-source, MIT-licensed, terminal-first AI coding agent and agent harness — **114,000+ GitHub stars** as of Oct 2026, TypeScript monorepo, Windows/macOS/Linux.

- **Author:** Mario Zechner (`badlogic`), creator of the libGDX game framework. He wrote Pi out of frustration that every coding agent was an unexplainable black box; the repo was `badlogic/pi-mono` until ~April 2026.
- **Company:** **Earendil Works** (Earendil Inc., Vienna) — co-founded by Armin Ronacher (creator of Flask, ex-Sentry) — **acquired** the Pi open-source project in 2026; Zechner became a major stakeholder and team member. Early backers per the announcement: Accel, Balderton, and founders of n8n, OpenClaw, Revolut, Sentry, Slack. (Wilson's USV investment claim comes from the reel; USV is not named in Earendil's public backer list — treat as his claim.)
- **Not** Inflection's Pi chatbot, Google's robotics PI, or "Pieces."

## The design thesis: primitives, not features

Pi's tagline is "a minimal agent harness": **adapt Pi to your workflows, not the other way around.** The signature is what it deliberately leaves out:

- **Four built-in tools.** read, write, edit, bash. That's the whole default toolset. System prompt under 1,000 tokens — "the shortest system prompt of any major agent."
- **No subagents, no plan mode, no permission popups in core.** Everything else — sub-agents, plan mode, permission gates, path protection, SSH execution, sandboxing, MCP integrations — is a **TypeScript extension** you build or install. "The strength is in what they didn't build."
- **Model-agnostic by construction.** 15+ providers (Anthropic, OpenAI, Google, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, Hugging Face, Kimi, MiniMax, NVIDIA, OpenRouter, Ollama) plus custom providers via `models.json` or extensions. Mid-session model switching (`/model`, `Ctrl+L`). Pi is the harness; the model is a plug-in.
- **Context engineering as first-class surface.** `AGENTS.md` (project instructions from `~/.pi/agent/`, parent dirs, cwd), `SYSTEM.md` (replace/append the default system prompt per-project), **customizable compaction** (implement topic-based or code-aware summarization, or swap the summarization model, via extensions), **skills** (capability packages loaded on-demand — progressive disclosure without busting the prompt cache), prompt templates (`/name` expansion), and extensions that inject messages before each turn, filter history, or build long-term memory/RAG.
- **Tree-structured sessions.** `/tree` navigates to any previous point and continues from there; all branches in one file; `/export` to HTML, `/share` to a gist URL.
- **Four modes:** interactive TUI, print/JSON (`pi -p "query"`, `--mode json` event streams), **RPC** (JSON over stdin/stdout), and an **SDK** for embedding. **OpenClaw** — the 145k-star agent project — is built on Pi.
- **Packages:** bundle extensions + skills + prompts + themes, install from npm or git (`pi install npm:@foo/pi-tools`). 50+ examples in the repo.
- **Pi 1.0 / Pi Durable** (just shipped, Oct 2026): durable agents that survive a crashed process and resume exactly where they left off — the "effect sandwich" (record intent, run effect, persist result), idempotency keys for tool calls, versioned documents for agent state; runs on Node, Bun, Cloudflare Durable Objects, E2B, even a phone. Notably, Pi is also landing **Codemode, MCP, and the Jev classifier** (per Ronacher's Oct 2026 post) — the decision-model pattern from this playbook's Jev section, inside the harness.

## Why enterprises pick it: Wilson's argument

Wilson's claim, stripped of hype: a CTO cannot build the company's entire engineering future on a proprietary model endpoint. The reasons are the ones this playbook has been documenting all along — **model churn** (the model you tuned for gets replaced), **pricing power** (rate limits in 2025 taught enterprises this), **evolvability** (you can't change what you can't see). Pi inverts the dependency: the harness is yours (MIT, forkable, hackable), the model is a commodity you swap. When Claude 6 or GPT-7 or a local distilled model wins, you change one line in `models.json`, not your whole platform.

## The companies

### Coinbase: Forge and Mux

Coinbase's trajectory is the most documented enterprise agent build-out:

- **Forge** (previously Cloudbot, originally Claudebot): as of July 2026, **>95% of Coinbase's code is AI-generated** (up from 40% in February), the system accounts for **5% of all merged PRs**, PR cycle time fell from **~150 hours to ~15 hours**, and **1,200 AI agents** run at full-time-equivalent capacity — each engineer working with 5–10 simultaneously. Built from scratch: in-house sandboxes, MCPs + custom Skills, Slack-native invocation, **agent councils + auto-merge** as the validation pattern.
- **Mux** ([coinbase.com/blog](https://www.coinbase.com/blog/coding-had-a-concurrency-problem-how-mux-helped-solve-it), May 2026): the concurrency story. Agents made individuals faster, but engineers still worked "one branch, one terminal, one task" — while the agent worked, the engineer waited. Mux gives each agent its own git worktree, branch, and terminal. Started as one engineer's side project, grew to **600+ users, 5,068 merged PRs across 461 repos**, with users merging **3.5× more PRs** (39.6 vs 11.4 baseline). "The bottleneck had moved. It was no longer how fast we could write code. It was how many things one engineer could orchestrate at once."
- **The build-vs-buy lesson** (Coinbase's own words): "AI changed the build-vs-buy calculus for internal tooling… Internal tools that encode institutional knowledge are suddenly cheap to build and expensive to ignore." The substrate that made Mux possible: an **internal LLM Gateway**, a growing **MCP server ecosystem**, and a culture of experimentation. Their answer to "did we have to build this ourselves": the value isn't the multi-agent UI (that exists everywhere) — it's the institutional knowledge baked in (internal cloud agent dispatch, Codeflow deploys, team review flows, repo conventions as reusable commands).

### Shopify: Helix, River, Roast

Shopify's public work shows the same harness instinct in three places:

- **Helix** ([shopify.engineering/helix](https://shopify.engineering/helix)): the internal tool that rebuilt the Shop mobile app (React Native → native Swift/Kotlin) in 12 weeks and is now migrating the 300-screen Shopify app. The pattern: **checkpoints small enough to review at a glance** + **four gates strict enough to stop anything unproven** — (1) Behavior (CLI tests, no simulator needed), (2) UI review (Gemini as a "perfectionist design reviewer" comparing screenshots, listing every difference with severity and location), (3) adversarial review (two independent, context-isolated reviewer agents; loop until both approve), (4) engineer sign-off with feedback recorded to memory so later checkpoints need less oversight. "An attempt is allowed to be wrong. It is not allowed to ship until it isn't."
- **River**: a Slack-based coding/knowledge agent living under one deliberate constraint — **no direct messages; every conversation in a public channel**. Watching a colleague debug with River teaches the org faster than any training doc, and public visibility keeps quality honest. Underneath sits **Aquifer**, the infrastructure for durable, resumable agent sessions. Extended into autonomous security remediation (grouping vuln findings into threads, driving fixes to merge).
- **The platform underneath**: an **internal LLM proxy** (one billing relationship, one observability pipe) and a custom review harness called **Roast**; VP Engineering Farhan Thawar: "Shopify is not yet at the place where we allow AI to check in code automatically."

### The honest tension

August 2026 reporting (The Information, via webpronews/Medium): Coinbase and Shopify were building **custom layers on top of Claude Code** — "the model is not being replaced, it's being scaffolded" — with the wrappers adding memory, routing, and guardrails. Wilson's October reel says they **dumped Claude** for Pi. Both can be true in sequence (scaffold first, swap the harness later — which is exactly what a model-agnostic harness enables), or different teams may be at different stages. Don't present "dumped Claude" as settled fact; present it as Wilson's claim, directionally consistent with the documented trajectory.

## How to build your own: the Pi-based enterprise pattern

Distilled from what Coinbase and Shopify actually did, mapped onto Pi's surfaces:

1. **Start with the harness, not the model.** Deploy Pi (MIT) as the agent substrate. Four tools and a sub-1k system prompt mean the thing you own is small enough to audit. The model becomes a config line.
2. **Centralize the gateway.** One internal LLM proxy: one billing relationship, one credential store, one observability pipe, one policy enforcement point. This is the prerequisite for everything below (Coinbase's LLM Gateway, Shopify's proxy). Route models per task here — the cost lever.
3. **Encode institutional knowledge as packages.** `AGENTS.md` + `SYSTEM.md` per repo, skills for team workflows, prompt templates for repeated jobs. Bundle as Pi packages, distribute via npm/git or an internal registry. This is the Mux lesson: the plugins and skills *are* the moat — they encode how your company ships.
4. **Gates, not advice.** Copy Helix: checkpoints small enough to review at a glance; automated gates (behavior tests, visual review, adversarial review) that block; engineer sign-off that feeds memory. An attempt may be wrong; it may not ship until it isn't.
5. **Make agent work visible.** Shopify's River rule — public channels only — or the equivalent: shared session trees (`/share`), public dashboards. A private agent teaches one person; a public one teaches the org, and visibility is a quality control.
6. **Orchestrate, don't just chat.** The Mux pattern: one worktree/branch/terminal per agent, many agents per engineer. The engineer's job moves up the stack to scoping, review, and exception-handling.
7. **Instrument cost from day one.** Per-run budgets, per-team dashboards, P90-overrun investigation (the Palafox pattern from this playbook's talk notes). Model-agnosticism lets you A/B models per task and pick the cheapest that clears the gate.

## Best ways for a company to do it: the short playbook

- **Harness is the product; the model is the commodity.** Own the harness (open-source, forkable). Rent the model (routable, replaceable). This is the single decision everything else follows.
- **Centralize the narrow waist, distribute the edges.** One gateway, one package registry, one set of gates — but skills and workflows authored by the teams that own the repos.
- **Start where the evidence is.** Mux began as one engineer's side project solving their own problem; Helix began with one app migration. Grassroots tools that encode real workflows beat top-down platform mandates. Leadership's job is the substrate (gateway, MCP servers, permission to experiment), not the tool.
- **Measure the loop, not the demo.** PR cycle time (Coinbase: 150h → 15h), % AI-generated code, merged PRs per engineer (Mux: 3.5×), rework rate. Faros AI's warning stands: raw output speed ≠ developer productivity once rework is counted.
- **Treat agent definitions like cache keys.** Standardized, versioned, shared agents produce identical prompt prefixes → shared cache hits (see the Palafox talk page's deep dive: 96.22% hit rates are a property of the harness, and per-team customization fragments them).
- **Don't skip the security model.** Unattended agents with repo credentials need the gh-aw treatment: sandboxing, credential isolation, output scanning, declared writes only.

## Tokenomics angle

Pi is the local-first thesis compiled into a product: the harness is a fixed, ownable cost; the model is a metered, routable one. Three tokenomics consequences:

- **Model arbitrage becomes a config change.** 15+ providers and mid-session switching mean the routing ladder (this playbook's Lever 4) is a `models.json` edit, not a migration. When a cheaper model clears your gates, you capture the spread the same day.
- **The minimal core is a smaller bill.** A sub-1k-token system prompt and four default tools mean every turn's cached prefix is smaller; skills load on-demand with progressive disclosure instead of front-loading context. Less prefix → less cache-write cost → cheaper turns.
- **The gateway is the meter.** One proxy sees every token from every team — the precondition for chargeback, budgets, and the P90-overrun pattern. Without it, "AI spend" is a rumor; with it, it's a line item.

## Links

- Pi: [pi.dev](https://pi.dev) · repo: [github.com/earendil-works/pi](https://github.com/earendil-works/pi) (114k ⭐, MIT) · docs: [pi.dev/docs](https://pi.dev/docs)
- Earendil: [earendil.com](https://earendil.com) · Pi acquisition + Lefos announcement
- Pi 1.0 / Pi Durable: [earendil.com/posts/pi-durable](https://earendil.com/posts/pi-durable/)
- Trigger reel: [instagram.com/reel/DeRBnnilHgX](https://www.instagram.com/reel/DeRBnnilHgX/) (@sourcerypod, Oct 9, 2026)
- Coinbase Mux: [coinbase.com/blog/coding-had-a-concurrency-problem-how-mux-helped-solve-it](https://www.coinbase.com/blog/coding-had-a-concurrency-problem-how-mux-helped-solve-it)
- Coinbase Forge (95% AI code, 1,200 agents): via ainvest summary; original Coinbase engineering channels
- Shopify Helix: [shopify.engineering/helix](https://shopify.engineering/helix)
- The Information via [webpronews](https://www.webpronews.com/coinbase-shopify-bet-big-on-custom-ai-coding-agents-to-supercharge-claude/) (Aug 2026, paywalled original)
- Related in this playbook: [Palafox talk](scaling-custom-agents-copilot-palafox.md) (the GitHub-side mirror: marketplace → pipeline → cost observability)
