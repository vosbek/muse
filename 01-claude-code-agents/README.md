# 01 — Claude Code & Agents

**Thesis:** Claude Code's power isn't the model — it's the scaffolding around it. Taken together, these eight reels describe a complete operating system for the tool: skills that package repeatable behavior, subagents that keep the main context clean, dynamic workflows that let the agent write its own orchestration, and pipelines that offload heavy analysis to free external engines. The through-line is leverage — a small amount of setup (a skill file, a subagent definition, a slash command) that pays off on every subsequent session.

### Turn Instagram Saves into a Notion content system
- **Creator:** @justyn.ai · **Date:** 2026-07-01
- **What it suggests:** The Save button is a graveyard — posts go there to be forgotten. The fix is an automation that treats saves as raw material: a Claude Code (or Codex) session builds two Notion databases ("Instagram Saves" with columns for Caption, Collection, URL, Status, Type, Saved date), connects via Instagram session cookies, and syncs twice daily at 9 AM and 9 PM. Saved posts land categorized under collections like "Claude Code" or "Content Ideas," and from there the system transforms them into original content ideas, blog posts, or articles. The deeper lesson is architectural: social saves are an unstructured intake queue, and a scheduled agent plus a structured store turns them into a content supply chain. The same pattern works for any intake — bookmarks, read-later lists, meeting notes — as long as there's a schema and a sync cadence.
- **Repos/tools:** Notion (database + API), Claude Code / Codex
- **Extractable skill:** Scheduled intake automation — define a schema, connect the source, sync on a cadence, then run a transform step that converts raw captures into usable output.
- **Source:** https://www.instagram.com/reel/DaQqNWnvEMs/

### Dynamic workflows: let the agent write its own orchestration
- **Creator:** @rajistics · **Date:** 2026-05-31
- **What it suggests:** Anthropic's dynamic workflows collapse multi-agent orchestration from ~25 lines of hand-written node-edge-state config to a couple of lines, by giving the agent itself a tool to write its own orchestration logic. The demo walks through a research-deepening example — specialized agents for web search and fact-checking — where the model generates async coordination code live in the terminal, adapting the plan as it goes instead of following a predefined workflow. The critical discipline he adds: inspect the traces afterward (84 interaction traces in Langfuse in his demo) to understand what the system actually did. The takeaway for agent builders is to stop pre-scripting every branch and instead give agents orchestration primitives plus observability — flexibility at runtime, auditability after.
- **Repos/tools:** Claude Code (dynamic workflows), Langfuse (trace observability)
- **Extractable skill:** Agent-written orchestration — provide coordination tools, not fixed graphs; always keep trace inspection as the verification step.
- **Source:** https://www.instagram.com/reel/DZBiUWhtEvj/

### The 6 design skills worth keeping (after testing 70+)
- **Creator:** @omgluka · **Date:** 2026-05-02
- **What it suggests:** After testing 70+ Claude Code design skills, only six survived — three for web (stitch-skill, taste-skill, impeccable) and three for motion (remotion, hyperframes, gsap) — and he deleted the rest. The value isn't the specific list, it's the method: skills accumulate silently and most of them are redundant or low-quality, so periodic culling against real output is mandatory. A skill earns its place by surviving contact with actual work; everything else is context-weight. Note he renders video with remotion itself — dogfooding as the selection filter.
- **Repos/tools:** stitch-skill, taste-skill, impeccable, remotion, hyperframes, gsap (skill names as presented)
- **Extractable skill:** Skill portfolio review — regularly test your installed skills against real tasks, keep the winners, delete the rest. A small set of proven skills beats a large set of maybe-skills.
- **Source:** https://www.instagram.com/reel/DX2oGBDN7M0/

### YouTube pipeline skill: offload analysis to free engines
- **Creator:** @chase.h.ai · **Date:** 2026-03-17
- **What it suggests:** A custom seven-step "YouTube pipeline" skill: search YouTube for any topic, push the links to NotebookLM, let Google's free analysis engine do the synthesis, and receive the results back. The key insight is economic — the heavy analytical work happens on Google's free tier instead of inside your metered coding session, so it costs nothing and consumes none of your main context. This is the Jev pattern applied to research: a narrow, purpose-built pipeline handles the expensive comprehension step, and only the distilled answer crosses back into the working session. Any workflow with a "read and summarize a pile of stuff" step is a candidate for this offload.
- **Repos/tools:** Claude Code (custom skills), NotebookLM (notebooklm.google.com)
- **Extractable skill:** Free-engine offload — identify the comprehension-heavy step in a workflow, route it to a free external engine, import only the synthesis.
- **Source:** https://www.instagram.com/reel/DWA8YqVNP-N/

### Three systems to unlock Claude Code's design power
- **Creator:** @jens.heitmann · **Date:** 2026-03-03
- **What it suggests:** Most people only install front-end skills and miss the bigger lever: three systems working together. First, Google's Stitch MCP plus Nano Banana 2 to generate strong mockups that Claude Code uses as visual reference — the agent designs better when it can see a target. Second, the "UI UX Pro Max" design-intelligence skill from a GitHub library, which encodes design judgment as reusable rules. Third, an asset library like 21st.dev for production-grade 3D and reactive components, so the agent assembles rather than invents. The demo contrast (basic vs. polished outputs like "Eclipse," "Golden Hour," "Ethereal Glow") makes the point that AI design quality is bounded by its references. His closing line is the thesis: while designing with AI, humans set the quality standard — these systems just raise the floor.
- **Repos/tools:** Google Stitch (MCP), Nano Banana 2, UI UX Pro Max (GitHub skill library), 21st.dev
- **Extractable skill:** Reference-driven generation — never ask an agent to design from nothing; feed it mockups, encoded taste, and real components first.
- **Source:** https://www.instagram.com/reel/DVbfcdTkZ7R/

### Three Claude Code skills: GSD, superpowers, skill-creator
- **Creator:** @jens.heitmann · **Date:** 2026-02-21
- **What it suggests:** The claim is that most people use maybe 20% of Claude Code, and the skills feature is the other 80%. Three to install immediately: GSD ("Get Shit Done" v1.9.6), a workflow skill that multiplies output by imposing execution discipline; obra/superpowers, a skill library that — paired with GSD — puts Claude Code "on steroids"; and Anthropic's official skill-creator, the meta-skill that turns repetitive late-night sessions into saved, reusable skills. The third is the most strategic: it's the mechanism by which individual workflows become institutional assets. Together they form a stack — discipline (GSD), capability library (superpowers), and capture mechanism (skill-creator) — that converts usage into compounding advantage.
- **Repos/tools:** [obra/superpowers](https://github.com/obra/superpowers), Anthropic skill-creator (official), GSD v1.9.6
- **Extractable skill:** Skill-stack thinking — install an execution-discipline skill, a capability library, and a capture tool; the last one is how the other two keep improving.
- **Source:** https://www.instagram.com/reel/DVB32zvj91u/

### One frontend-design skill replaces 18 months of vibe-coding
- **Creator:** @sourcetms · **Date:** 2025-12-30
- **What it suggests:** Thomas Schlossmacher, a founder building AI-centric products, says Claude's skills feature made his previous 18 months of frontend vibe-coding obsolete: a single frontend-design skill plus one prompt rebuilt his entire personal website — a clean, modern bento-modular layout with social links, partners, Telegram community access, and articles — in under 30 minutes. The striking detail is that the skill absorbed his fragmented, messy "workspace" and returned it standardized and beautiful. The lesson generalizes: a well-built skill encodes taste and structure that would otherwise take months of iteration to develop, and it works in Claude Code or OpenAI's Codex. Skills aren't shortcuts; they're compressed expertise.
- **Repos/tools:** Claude Code / Codex (skills feature)
- **Extractable skill:** Taste-encoding — when a workflow finally produces great output, capture it as a skill immediately; that's the moment 18 months of learning becomes a file.
- **Source:** https://www.instagram.com/reel/DS5KGfdjHvL/

### Top 3 subagents: Explorer, Research Documenter, Historian
- **Creator:** @agentic.james · **Date:** 2025-10-13
- **What it suggests:** Three subagent archetypes for efficient Claude Code work, each solving a context problem. The Explorer locates code across the codebase so the main agent doesn't burn its context window on discovery. The Research Documenter handles large integrations with parallel web searches — fan-out work that would serialize and bloat the main thread. The Historian is a context-orchestration system that stores checkpoint snapshots as markdown files, giving long sessions a rewindable memory. Together they're a division of labor: discovery, parallel research, and state persistence all happen outside the expensive main context, which stays focused on decisions and edits.
- **Repos/tools:** Claude Code (subagents)
- **Extractable skill:** Context-labor division — push discovery, parallel research, and checkpointing into subagents; keep the main thread for judgment and edits only.
- **Source:** https://www.instagram.com/reel/DPxE0FDAe71/

## From X bookmarks (Sep 2026)
Distilled from Matt's X bookmarks, newest first. Full post text at each permalink (X truncates long posts in timelines).

### AI Engineer Paris talk: /retro, /pr, and getting more from agents
- **Creator:** @mattpocockuk · **Date:** 2026-09-25
- **What it suggests:** Shares the talk given at AI Engineer Paris 2026, announcing /retro and /pr commands and covering how to get more from coding agents (text truncates). Verifiable: /retro and /pr are new workflow commands — a retrospective command and a PR-focused command — presented on a main-stage talk with a YouTube card. The pattern is agent workflow commands as the unit of leverage: named, repeatable loops (review your own work, prepare a PR) that compound agent output quality. The talk's full content is at the permalink and the linked video.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Encode repeatable agent workflows (retrospectives, PR prep) as named commands, not ad-hoc prompts.
- **Source:** https://x.com/mattpocockuk/status/2103501498361798983

### Getting the most out of Opus 5.5: hand over whole tasks, define "done"
- **Creator:** @ClaudeDevs · **Date:** 2026-09-22
- **What it suggests:** Tips for a first Opus 5.5 session: hand over a whole task, define what "done" means, and decide when to check in (text truncates), linking the official blog post on getting the most out of Opus 5.5 in Claude and Claude Code. Verifiable: the advice pushes toward larger delegation units — whole tasks with explicit completion criteria and check-in points — rather than step-by-step micromanagement. This matches the delegation theme across the collection: agent output quality scales with how completely you specify the goal and the verification step. Full tips at the permalink and the linked blog.
- **Repos/tools:** claude.dev (blog link card in post)
- **Extractable skill:** Delegate whole tasks with an explicit definition of done and scheduled check-ins instead of micromanaging steps.
- **Source:** https://x.com/ClaudeDevs/status/2102491840612380934

### A real-world Opus 5.5 benchmark on actual knowledge-work tasks
- **Creator:** @danshipper · **Date:** 2026-09-22
- **What it suggests:** Points to a personal benchmark of Opus 5.5 on real-world knowledge-work tasks, reporting it performs at Fable level on many actual work tasks — though on a few it ran into trouble (text truncates, with an image showing more). The benchmark lives at the linked checks page. Verifiable: this is an eval grounded in one person's real work rather than synthetic benchmarks, which makes it more predictive of day-to-day usefulness. The caveat suggests failure modes on some tasks; the full results and methodology are at the permalink.
- **Repos/tools:** Mike's Checks benchmark — checks.every.to/p/mikes-checks
- **Extractable skill:** Evaluate models on your own real work tasks, not just synthetic benchmarks, before committing workflows to them.
- **Source:** https://x.com/danshipper/status/2102438173599297643

### A Jev plugin for Claude that audits tool calls and compacts context in 1 second
- **Creator:** @altryne · **Date:** 2026-09-17
- **What it suggests:** Highlights a Claude plugin using TypeSafe AI's Jev model to review unnecessary tool calls, running in about 1 second — quoting a post that found the ideal Jev use case: instant compaction. The text truncates, so install details are at the permalink; a short demo video and two images show it working. Verifiable: this is the decision-model pattern applied inside the agent loop itself — a cheap model auditing and compressing the expensive model's tool-call trace in real time. Compaction is one of the highest-leverage cost controls in long agent sessions.
- **Repos/tools:** None linked in post text (Jev plugin for Claude; @typesafeai mentioned).
- **Extractable skill:** Audit and compact your agent's tool-call trace with a cheap model in real time to control long-session costs.
- **Source:** https://x.com/altryne/status/2100739055923425589

### shadcn/lint: a linter for Tailwind design systems built for agents
- **Creator:** @ctatedev · **Date:** 2026-09-14
- **What it suggests:** Reacts with enthusiasm to the announcement of shadcn/lint, a linter for Tailwind design systems designed with agents as the primary user. The post is short and complete; the substance is the quoted announcement at the permalink. Verifiable: this is tooling built for agents as the operator — a linter that keeps AI-generated Tailwind consistent with a design system, which only matters once agents are writing most of the UI. The direction is clear: developer tools are being rebuilt around the agent, and linting is where design-system compliance gets enforced on machine-written code.
- **Repos/tools:** shadcn/lint (announced by @shadcn; no URL in post text)
- **Extractable skill:** Adopt agent-first tooling (like design-system linters) that enforces consistency on machine-written code.
- **Source:** https://x.com/ctatedev/status/2099536434285666550

### Skill-driven development: a full CRM dashboard in two days with Claude
- **Creator:** @rauchg · **Date:** 2026-09-14
- **What it suggests:** Names the pattern "skill-driven development," quoting a build where a complete Next.js CRM dashboard was assembled in roughly two days using Claude Fable 5.1, powered by published skills and deployed to a live URL, with a demo video. The quoted post names two skills on skills.sh and the deployed app. Verifiable: the claim is that reusable skills — not prompts — were the leverage that made a two-day full-app build possible. This reframes agent productivity: the asset is the skill library, and skill-driven development is the proposed methodology — compose skills, let the model execute.
- **Repos/tools:** Skills — skills.sh/jakubkrehel/sk; skills.sh/emilkowalski/s… (display truncated in source). Demo app — sales-crm-kargulstudio.vercel.app
- **Extractable skill:** Build a reusable skill library and compose skills to drive full-app builds instead of writing one-off prompts.
- **Source:** https://x.com/rauchg/status/2099500509451502043

### Put HTML-explainer instructions in your CLAUDE.md / AGENTS.md
- **Creator:** @nityeshaga · **Date:** 2026-09-14
- **What it suggests:** Advises that anyone making HTML explainers with an agent should add specific instructions to their CLAUDE.md / AGENTS.md files, quoting an article on the unreasonable effectiveness of HTML with Claude Code. The text truncates, so the actual instruction text is at the permalink. Verifiable: the pattern is persistent agent configuration — project-level instruction files that steer output format (here: HTML explainers) across sessions. The meta-point: the highest-leverage prompt engineering is the kind you write once into AGENTS.md and every future session inherits.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Write output-format instructions once into CLAUDE.md/AGENTS.md so every future session inherits them.
- **Source:** https://x.com/nityeshaga/status/2099394418877125035

### 24 reusable agent skills distilled from 14 years at Google
- **Creator:** @0xCodila · **Date:** 2026-09-13
- **What it suggests:** Quotes an Anthropic engineer and ex-Googler describing 14 years at Google distilled into 24 reusable skills for agents, linking the author's own article on graph engineering for building 1000+ agent loops from one prompt, with a 40-minute video. The post text is a quote and complete; the substance is the linked article at the permalink. Verifiable: the through-line with the skill-driven development post is that senior practitioners are converging on skills — not prompts, not single agents — as the durable unit of agent engineering. Fourteen years of platform experience compressed into 24 reusable skills is the model for how teams should accumulate agent leverage.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Accumulate agent leverage as a library of reusable skills, not as one-off prompts or single agents.
- **Source:** https://x.com/0xCodila/status/2099177605484179532
