# 08 — Tools & APIs

**Thesis:** The infrastructure layer beneath the agents: free API directories, voice input that beats typing, agentic browsers that act without APIs, and — most importantly for the local-first thesis — proof that a capable agent runs in 44 lines on your own machine. These five reels are the "what to actually install" shelf of the collection.

### public-apis: free APIs for everything
- **Creator:** @softwarewithnick · **Date:** 2025-10-08
- **What it suggests:** A tour of the public-apis GitHub repo — an enormous categorized directory of free APIs spanning sports, fitness, crypto, anime, and hundreds more topics. The reel doubles as a quick explainer of what an API is, but the durable value is the resource itself: it's the fastest way to answer "is there a free API for X?" before writing a line of integration code. For agent builders, it's doubly useful — agents that need real-world data (scores, prices, weather, transit) usually don't need a paid tier or a custom scraper; they need this list. Bookmark it as the first stop in any "agent needs external data" design.
- **Repos/tools:** [public-apis/public-apis](https://github.com/public-apis/public-apis)
- **Extractable skill:** API-first data sourcing — check the free directory before building scrapers or buying tiers.
- **Source:** https://www.instagram.com/reel/DPkja3vDD_f/

### Three voice AI apps that beat typing
- **Creator:** @sabrina_ramonov · **Date:** 2025-08-15
- **What it suggests:** Voice input is three to four times faster than typing, and three apps worth knowing: WhisperFlow, which cleans spoken transcripts into polished, email-ready text; SuperWhisper, which does its AI processing locally on your machine — private by construction, no voice data to the cloud; and Voice Inc, free and open-source, newer with fewer features but worth watching. The comparison is really a decision framework: pick WhisperFlow for output polish, SuperWhisper for privacy and offline use, Voice Inc for zero cost and hackability. The local-processing pick (SuperWhisper) echoes the collection's local-first economics — the best voice tool may be the one that never leaves your machine.
- **Repos/tools:** WhisperFlow, SuperWhisper, Voice Inc (open source)
- **Extractable skill:** Voice-first capture — dictate-then-polish for anything long-form; default to local processing where privacy matters.
- **Source:** https://www.instagram.com/reel/DNY9TEUKlaR/

### A real AI agent in 44 lines, running entirely locally
- **Creator:** @ai.christianson · **Date:** 2025-08-15
- **What it suggests:** The most economically significant demo in this category: a genuinely useful AI agent built in 44 lines of code with open-source tools, running entirely on a personal computer. The recipe: Hugging Face's smolagents library plus the open-weight Qwen3 30B model, with exactly two tools — shell-command execution and file writing. That's enough for it to query system info like disk space and organize files. The point isn't the specific tasks; it's the collapsed floor. Capable agentic behavior no longer requires cloud APIs, API keys, or per-token billing — it requires a decent open model and a weekend afternoon. For tokenomics, this is the existence proof behind the SLM thesis: the long tail of agentic work can move local, and the build cost is trivial.
- **Repos/tools:** [huggingface/smolagents](https://github.com/huggingface/smolagents), Qwen3 30B (open weights)
- **Extractable skill:** Local-agent baseline — before reaching for a cloud agent, check what smolagents + an open model + two tools can already do.
- **Source:** https://www.instagram.com/reel/DNYjqVfNYHT/

### Fellou: the agentic browser
- **Creator:** @sabrina_ramonov · **Date:** 2025-05-19
- **What it suggests:** Fellou bills itself as "the world's first agentic browser": a browser with an agent that acts on private, logged-in websites, works in a virtual workspace, and generates reports. The demo example — logging into LinkedIn, writing a post, and publishing it without any API — shows the category's real proposition: automating the long tail of web tasks that have no API and never will. The presenter adds a cautionary note, which is worth keeping: a browser agent with your credentials acting on private sites is powerful and also a meaningful trust and security surface. Evaluate agentic browsers on credential handling and action auditability, not just capability demos.
- **Repos/tools:** Fellou (agentic browser)
- **Extractable skill:** API-less automation assessment — for sites with no API, agentic browsers are the answer; vet them on credential security and audit trails first.
- **Source:** https://www.instagram.com/reel/DJ2RwR3IiG-/

### Showcase AI work on Hugging Face Spaces
- **Creator:** @edhonour · **Date:** 2025-05-04
- **What it suggests:** Hugging Face Spaces as the default place to showcase AI projects — the argument being that unlike GitHub, which shows code, Spaces gives visitors a fully interactive environment where they can see the model or app actually running. For anyone building in this collection's patterns (skills, agents, demos), the takeaway is about distribution: interactive demos convert better than repos, because the evaluator experiences the behavior instead of inferring it from code. If you're publishing agent work — especially for hiring, clients, or community feedback — ship the Space alongside the repo.
- **Repos/tools:** Hugging Face Spaces (huggingface.co/spaces)
- **Extractable skill:** Demo-driven distribution — publish an interactive Space with every significant AI project, not just the code.
- **Source:** https://www.instagram.com/reel/DJPz_Ulya7Q/

## From X bookmarks (Sep 2026)
Distilled from Matt's X bookmarks, newest first. Full post text at each permalink (X truncates long posts in timelines).

### Debug Visualizer: see your data structures inside VS Code
- **Creator:** @code · **Date:** 2026-09-23
- **What it suggests:** Recommends the Debug Visualizer extension for VS Code for anyone working with data structures — it renders them visually during debugging (text truncates), with a demo video. Verifiable: this is a visualization tool that renders data structures instead of making you read raw object dumps. For agent-assisted development it matters twice: humans reviewing agent-written data-structure code comprehend it faster visually, and it's the kind of comprehension tooling that keeps human review effective as machine-written code volume grows.
- **Repos/tools:** Debug Visualizer (VS Code extension; no URL in post text)
- **Extractable skill:** Visualize data structures during debugging instead of reading raw dumps, especially when reviewing agent-written code.
- **Source:** https://x.com/code/status/2102760396490719499

### Link collection: skill evaluation and agent infrastructure
- **Creator:** @OrenMe · **Date:** 2026-09-20
- **What it suggests:** This post has no body text — it is a pure link collection, listed here as shown. The theme is evaluation and agent infrastructure: NVIDIA's SkillEvaluator (link card describes it as a multi-tier framework for evaluating AI agent skills), Microsoft's Waza site, a Harbor framework repo, Microsoft's APM site, and a GitHub Marketplace link. With no commentary from the poster, treat this as a reading list: the SkillEvaluator repo is the standout for anyone building the skill libraries discussed elsewhere in this collection, since skills need evals to stay trustworthy as they accumulate.
- **Repos/tools:** NVIDIA SkillEvaluator — github.com/NVIDIA/skillev… (display truncated in source); microsoft.github.io/waza/; Harbor framework — github.com/harbor-framewo… (display truncated in source); microsoft.github.io/apm/; github.com/marketplace/re… (display truncated in source)
- **Extractable skill:** Pair every skill library with an evaluation framework so skills stay trustworthy as they accumulate.
- **Source:** https://x.com/OrenMe/status/2101685294961422461

### Alibaba open-sourced its production code reviewer
- **Creator:** @agenticgirl · **Date:** 2026-09-13
- **What it suggests:** Reports that Alibaba open-sourced the code reviewer it claims has served tens of thousands of developers and found significant issues (text truncates), with an image. Verifiable: this is a production-hardened review tool — battle-tested at massive developer scale — now available as open source. That provenance matters: unlike demo-ware, its rules and workflows survived real enterprise use. The detailed findings are at the permalink. For teams building review automation, this is a reference implementation worth studying before building your own.
- **Repos/tools:** None linked in post text (repo link not in visible text — see permalink).
- **Extractable skill:** Study production-hardened open-source reviewers before building your own review automation.
- **Source:** https://x.com/agenticgirl/status/2099087022900367845
