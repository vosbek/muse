# Combined Patterns — what all 39 reels teach together

Each reel below was distilled on its own. This page is the synthesis: the ideas that show up again and again, and what they mean for someone running tokenomics and context management.

## Recurring patterns

**1. Small decision models keep the main context clean.**
The Jev pattern (@superlinear_fm) — a separate small model picks MCP tools in isolation, and only the chosen answer enters the main prompt — recurs everywhere: the Explorer subagent that locates code so the main agent doesn't burn context (@agentic.james), GSD orchestrating work so the operator doesn't (@jens.heitmann), the Historian snapshotting checkpoints to markdown (@agentic.james). The principle: never let bookkeeping tokens touch the expensive context window. Route decisions through cheap, narrow models; reserve the frontier model for execution.

**2. Retrieval quality is token economics.**
@gittrend.io's jevgrep demo makes it numeric: same 8/10 SWE-bench tasks solved, bill cut from $7.62 to $5.44 (~30%), purely by converting a plain-English repo question into targeted search that returns exact lines. @bryrobbie's MarkItDown → Obsidian pipeline is the same idea for documents: agents can't use what they can't parse, so convert everything to clean markdown first. Every token spent re-reading files the agent already should have found is waste — retrieval is a cost control.

**3. Skills beat prompts.**
A prompt is a hope; a skill is a packaged, reusable, versionable unit of behavior. The collection keeps returning to this: Anthropic's skill-creator turning late-night sessions into saved skills, obra/superpowers as a skill library, the frontend-design skill that made 18 months of vibe-coding obsolete (@sourcetms), the six design skills that survived testing 70+ (@omgluka). Skills are how individual wins become institutional capability.

**4. Memory that compounds beats context that resets.**
Three independent designs converge: lessons.md read at session start and applied before code (@keshavsuki), the /memory + /recall + /rem-sleep trio with a hierarchical folder store (@agentic.james), and the nested memory tree managed by background subagents (@agentic.james). @lostandlucky's Second Brain is the same idea at company scale: stop treating the model as memory; store past work as structured knowledge and retrieve it. Memory is context you don't have to re-pay for.

**5. The harness is the product.**
@brooke.bytes' summary of the Strands Agents paper is the most important technical idea in the collection: most coding-agent failures are an intent-execution gap in the harness (the layer translating model intent into edits), not model stupidity — a one-line change gets applied to three classes, the model blames itself, and everything compounds from there. Fixes are harness-level: expand context until matches are unique, require whole-line matches, show a diff after every edit, reject bad edits upfront. Model-agnostic, and improvements compound across models. @rajistics' dynamic workflows point the same way: let the agent write its own orchestration instead of hand-rolling node-edge-state configs.

**6. Local-first is becoming economically forced.**
@gojutechtalk (Stanford CS adjunct): running AI in LLM form is "not fiscally reasonable" — SLMs will replace LLMs, economics being the biggest reason. @ai.christianson's 44-line agent (smolagents + Qwen3 30B, two tools: shell + file write) proves the floor has collapsed: capable agents now run on commodity hardware. @sabrina_ramonov's SuperWhisper pick is the same instinct for voice: local processing, no cloud round-trip, private by construction.

**7. Evals are a discipline, not a tool.**
@camillaintech's prompt-testing method (three pillars: base model, customization layer, quality gates; rules have measurable ROI — too many rules slow the model and degrade output) pairs with @rajistics inspecting 84 Langfuse traces and the Strands paper's Terminal Bench 2 numbers across 21 models. The pattern: instrument first, keep what measures better, delete what doesn't.

**8. Design is a system, not taste.**
Generic AI output has a look (purple gradients, random emojis) because models regress to the mean of their training data (@janustiu). The fixes are all systems: reference skins (@kem_glitch), locked style-guide prompts, the 4-level de-genericizing ladder (references → specific prompts → style guide → Figma MCP), curated skill sets. "Humans set the quality standard" (@jens.heitmann) — the system just enforces it.

**9. Automation is glue between tools.**
Power Automate scheduled flows (@metric_maven), Playwright MCP browser automation (@agentic.james), NotebookLM as a free offloaded analysis engine (@chase.h.ai, @jens.heitmann), N8N/Make/Voiceflow tutorials (@sabrina_ramonov), and the Gmail agent-builder-vs-Zapier verdict (@digitalsamaritan): the winning move is rarely one tool — it's the cheapest reliable pipe between the tools you already have.

## Highest leverage for a tokenomics + context-management remit

If you own token cost and context layers, these are the patterns to deploy first:

1. **Retrieval-first cost control.** jevgrep's 30% is the template: measure $/task, then attack the finding step before the thinking step. Better retrieval is the cheapest token you'll ever save.
2. **Decision-model routing.** Put a small, cheap model in front of every expensive decision — tool selection, model selection, triage. The main context window should only ever see answers, never deliberation.
3. **Memory as context compression.** lessons.md, hierarchical memory stores, checkpoint snapshots: everything the agent re-learns every session is a recurring token tax. Store it once, retrieve it cheap.
4. **Rule ROI on prompts.** Every instruction you add to a system prompt is paid on every call and can degrade output. Test additions like @camillaintech does; delete rules that don't measure better.
5. **Local-first for the long tail.** Classification, routing, transcription, simple agents — the SLM economics argument says this work migrates local. Reserve metered frontier calls for where they measurably win.
6. **Invest in the harness, not just the model.** When agents fail, check the edit/verify loop before blaming the model. Whole-line matches, diffs after every edit, reject-bad-edits-upfront — these are cheap, model-agnostic, and compound.

## New patterns from the X bookmarks (Sep 2026)

The 55 X posts (Sep 12–28, 2026) add four patterns the original 39 reels didn't have — all of them about speed of commoditization:

**10. Decision models commoditize in days, not years.**
Jev launched; three days later CUA-S1 open-sourced a competing System One family, and within two weeks there were open clones claiming superiority (Laya), a fully open 9B model with open data and recipe (Bespoke Nimble), a 2.8MB edge model, an open-weights classifier toolkit (SimpleJev), a PostgreSQL extension (jev()), a research CLI (jevgrep), and a provider-swap adapter. The moat evaporated before most teams finished evaluating the original. The playbook consequence: never build on a single decision-model vendor — build on the pattern (cheap classification/routing/gating), keep the provider swappable, and track open clones because the best local-first option may already beat the API.

**11. The economics are now quoted in multiples, and they're extreme.**
$0.042 per million input tokens for the decision layer. PR review at ~200x cheaper than Claude, answering in half a second. Agent bills cut 400x. jevgrep at 40% lower cost on SWE-bench. Unreal Agent 39% cheaper at the harness level. Even discounting vendor-amplified claims, the direction is unambiguous: decision-shaped work is becoming effectively free. That changes what's worth automating — when review costs 1/200th, you run it on every PR, every push, every ticket. The tokenomics move is to re-audit which workflows become viable at each new cost multiple.

**12. Skill-driven development is the emerging practice.**
@rauchg named it: a full CRM dashboard in two days, driven by composed skills from skills.sh. An ex-Google Anthropic engineer distilled 14 years into 24 reusable skills. shadcn shipped a linter whose primary user is an agent. NVIDIA shipped a multi-tier framework for evaluating agent skills. The unit of agent engineering is converging on the skill — versioned, reusable, evaluable — not the prompt, not the single agent. For the playbook: the skill library is the asset; evals (SkillEvaluator) are what keep it trustworthy as it grows.

**13. Model deprecation is now routine operations.**
GitHub Copilot deprecating selected models on Oct 19, 2026 is the forcing function: prompts, skills, evals, and workflows hard-tied to one model break on someone else's schedule. The X bookmarks' answer is the same abstraction stack the reels described — routers, provider-swap adapters, portable skills — now justified as operational resilience, not just cost control. Design every layer for model turnover.
