# 04 — Automation

**Thesis:** The highest-ROI automation work isn't building agents from scratch — it's gluing tools together so the boring parts run themselves. These five reels cover the full ladder: no-code scheduled flows (Power Automate), agent-driven browser control (Playwright MCP), platform-native agent builders (Gmail) with an honest assessment of their limits, free AI engines as automation components (NotebookLM), and the unglamorous prerequisite nobody skips — making your files machine-usable first (MarkItDown → Obsidian).

### Power Automate: the daily email recap flow
- **Creator:** @metric_maven · **Date:** 2026-04-28
- **What it suggests:** A concrete, replicable build: a scheduled cloud flow (make.powerautomate.com) running Monday–Friday at 6 PM that pulls the day's Outlook emails, sorts them into "Action Items" vs "Non Action Items" using a keyword list ("follow up," "project," "Action Required"), converts each group into HTML tables, and sends one summary email. The construction details matter — initialize variables for today's date and the keyword list, use "Get emails (V3)," filter to today, loop and classify. It's keyword-based, not AI-based, which is the real lesson: deterministic rules beat model calls for well-bounded triage, at zero marginal cost and full auditability. Reserve the model for the ambiguous remainder.
- **Repos/tools:** Microsoft Power Automate (make.powerautomate.com), Outlook
- **Extractable skill:** Deterministic-first triage — use scheduled flows with keyword rules for routine sorting; escalate only the ambiguous cases to AI.
- **Source:** https://www.instagram.com/reel/DXs7cBziNfx/

### MarkItDown + Obsidian: make your files usable for agents first
- **Creator:** @bryrobbie · **Date:** 2026-04-22
- **What it suggests:** Everyone loves the Obsidian graph view; almost nobody does the prerequisite. The argument: agents can't reason over PDFs, Word docs, PowerPoints, and Excel files in their native formats — the first real step is converting everything to clean, lightweight markdown. The tool is Microsoft's free MarkItDown (converts PDF, PPTX, DOCX, XLSX, images, audio, HTML, CSV, JSON, XML, ZIP, even YouTube URLs to markdown). The workflow: drop files in a folder, have an agent run MarkItDown over them, copy the .md outputs into Obsidian. The demo (a PDF handbook → clean markdown, side by side) makes the payoff tangible. The deeper point is about knowledge pipelines generally: retrieval quality — and therefore agent quality and token cost — is bounded by input hygiene. Pretty graphs are downstream of clean files.
- **Repos/tools:** [microsoft/markitdown](https://github.com/microsoft/markitdown), Obsidian (obsidian.md)
- **Extractable skill:** Ingest-then-reason — convert all source material to clean markdown before any agent touches it; treat input hygiene as a cost control.
- **Source:** https://www.instagram.com/reel/DXbrQCJgWBH/

### NotebookLM as a free content engine for Claude Code
- **Creator:** @jens.heitmann · **Date:** 2026-03-18
- **What it suggests:** NotebookLM was designed as a research tool, but it functions as a free content engine: feed it sources, and it generates audio, video, slides, and infographics you can then personalize in your own voice. The integration pattern is what matters — Claude Code handles the orchestration and personalization while Google's free tier does the heavy comprehension and generation. It's the same economic move as the YouTube pipeline skill (04's companion pattern): identify the most token-expensive step in a creative workflow and relocate it to a free engine, keeping only the judgment and voice work in the metered session.
- **Repos/tools:** NotebookLM (notebooklm.google.com), Claude Code, plus a GitHub repo for the integration shown in the video
- **Extractable skill:** Free-engine content pipeline — draft with NotebookLM's free generation, refine with your own voice in Claude Code.
- **Source:** https://www.instagram.com/reel/DWB5dLkEVxY/

### Automate any browser task with Claude Code + Playwright
- **Creator:** @agentic.james · **Date:** 2025-12-10
- **What it suggests:** A complete method for browser automation: perform the task yourself once, record a plain-language description of the actions (he uses Voice Memos for transcription), then have Claude Code turn that narration into a reusable automation via the Playwright MCP server, exposed as a custom slash command. The demo is Substack article scraping, but the pattern is general — the human demonstration becomes the specification, the agent writes the automation, the slash command makes it repeatable. The key insight is that demonstration beats specification for UI work: describing clicks ("clicking the back button," "scrolling down") in natural language is more reliable than writing selectors by hand, because the agent grounds each step against the live page.
- **Repos/tools:** Claude Code, Playwright MCP server
- **Extractable skill:** Demonstrate-then-automate — narrate the task once, let the agent build the Playwright automation, save it as a slash command.
- **Source:** https://www.instagram.com/reel/DSGmEW9jTmP/

### Google's Gmail agent builder — and why Zapier still wins on breadth
- **Creator:** @digitalsamaritan · **Date:** 2025-12-04
- **What it suggests:** A hands-on demo of Google's AI agent builder inside Gmail: create custom workflows from natural-language instructions — sentiment analysis on incoming mail, label assignment, response drafting with custom "gems." Then the honest pivot: the builder only supports a restricted set of integrated tools, which caps what real workflows can do. The verdict is that Zapier remains the superior choice for organizations needing broad application connectivity across their whole stack. The durable lesson isn't about either product — it's the evaluation frame: judge automation platforms by integration breadth and the escape hatches they offer, not by how slick the demo is. A beautiful builder with ten integrations loses to an ugly one with ten thousand, for production work.
- **Repos/tools:** Google AI agent builder (Gmail), Zapier (zapier.com)
- **Extractable skill:** Breadth-first platform evaluation — score automation tools on integration coverage and escape hatches before committing workflows to them.
- **Source:** https://www.instagram.com/reel/DR3pQ5OETRH/
