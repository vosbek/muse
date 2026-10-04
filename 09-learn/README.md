# 09 — Learn

**Thesis:** The on-ramp shelf: fundamentals that don't expire, project-based learning that beats courses, and free tutorial collections. @lostandlucky's reel is the anchor — fundamentals are fundamentals whether AI exists or not — and the other two are the practice: build eight real projects, follow six free automation tutorials. Learn by shipping, with the graph-theory foundations underneath.

### Build a Second Brain on graph fundamentals
- **Creator:** @lostandlucky · **Date:** 2026-07-01
- **What it suggests:** Jake Van Clief's core argument: most people use AI incorrectly by treating the model itself as memory, when what large companies actually build is a "Second Brain" — a structured store of past work and research the AI can access instantly. He teaches it from first principles with graph theory on a whiteboard: nodes are nouns (people, teams, places), edges are verbs (relationships, actions). The demo maps a company — teams as nodes, inter-team relationships as edges, workflows like a Product team consuming Slack questions and tickets to produce answers — with markdown files organizing processes, ideas, and jobs generating the visual graph. His refrain, "the fundamentals are fundamentals whether AI exists or not," is the point: graph thinking, clean markdown, and structured knowledge outlast every model release. He offers hours of free lectures through his Clief Notes community (40,000+ members) via the link in his bio.
- **Repos/tools:** Obsidian (graph view), markdown; Clief Notes community (link in bio)
- **Extractable skill:** Graph-first knowledge design — model your domain as nodes (nouns) and edges (verbs) in markdown before involving any AI.
- **Source:** https://www.instagram.com/reel/DaQ39vaPgjo/

### Eight AI projects that teach more than college
- **Creator:** @sabrina_ramonov · **Date:** 2025-06-03
- **What it suggests:** A project-based curriculum in listicle form: eight builds that together teach more applied AI than four years of coursework. The range is the syllabus — from making a custom GPT with ChatGPT, to a directory website with Lovable.dev, to an AI email agent, to a native mobile app with Bolt.new. The pedagogy is the takeaway: each project forces contact with a real tool, a real deployment, and real users, which is where the actual learning happens. For teams onboarding to AI tooling, this is a better template than another video course — assign the builds, not the lectures. Pick the projects that match your stack (the email agent and custom GPT map directly onto this repo's automation and skills themes) and work through them in order of increasing integration complexity.
- **Repos/tools:** ChatGPT (custom GPTs), Lovable.dev (lovable.dev), Bolt.new (bolt.new)
- **Extractable skill:** Project-based onboarding — learn AI tooling by shipping eight increasingly-integrated builds, not by watching tutorials.
- **Source:** https://www.instagram.com/reel/DKcfEvJCBdJ/

### Free AI automation tutorials: N8N, Make, Voiceflow
- **Creator:** @sabrina_ramonov · **Date:** 2025-04-13
- **What it suggests:** A curated entry point: six free YouTube tutorials covering the practical automation stack — building AI chatbots with Voiceflow, creating AI clones and multi-platform posting with Make.com and N8N. The framing is explicit: AI automation skill is a productivity and income lever, and the tutorials are free, so the only cost is time. As a resource it pairs naturally with this repo's automation category — watch the N8N/Make tutorials, then implement the Power Automate and Playwright patterns from 04 with real understanding of the underlying concepts (triggers, actions, data mapping). Free, structured, and hands-on beats expensive and theoretical for this particular skill set.
- **Repos/tools:** N8N (n8n.io), Make.com (make.com), Voiceflow (voiceflow.com); YouTube tutorials (links in the reel)
- **Extractable skill:** Tutorial-then-implement — use the free N8N/Make/Voiceflow tutorials as the conceptual base, then build the repo's automation patterns for real.
- **Source:** https://www.instagram.com/reel/DIZ_mBmhYm_/

## From X bookmarks (Sep 2026)
Distilled from Matt's X bookmarks, newest first. Full post text at each permalink (X truncates long posts in timelines).

### What fine-tuning actually updates inside the model
- **Creator:** @techNmak · **Date:** 2026-09-20
- **What it suggests:** Observes that everyone is fine-tuning LLMs but almost nobody understands what is actually being updated inside the model (text truncates), with an image presumably illustrating the internals. Verifiable: the point is a knowledge gap — fine-tuning is treated as a black-box recipe while the mechanistic question (which weights change, what the update does to representations) goes unexamined. For practitioners, the lesson is to learn what fine-tuning does before spending the budget: the image and full post at the permalink are the teaching artifacts.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Learn what fine-tuning actually updates inside the model before spending budget on it.
- **Source:** https://x.com/techNmak/status/2101614143447200124

### The senior engineer death spiral
- **Creator:** @elithrar · **Date:** 2026-09-20
- **What it suggests:** Strongly recommends an essay about compressing a month of senior-engineer work into a single week, unnoticed — calling it an incredible piece every senior engineer should read (text truncates) — quoting the announcement of the essay titled "the senior engineer death spiral," with a link. Verifiable: this is a career-craft essay about senior engineers and AI leverage, recommended emphatically by a practitioner. The substance is the linked essay at the permalink. For the playbook's learn section, the note is: the highest-leverage reading right now isn't model news, it's how senior engineers avoid being hollowed out by the tools.
- **Repos/tools:** None linked in post text. Essay — sunilpai.dev/posts/the-seni… (display truncated in source)
- **Extractable skill:** Study how senior engineers stay leveraged (not hollowed out) as agents absorb more of the work.
- **Source:** https://x.com/elithrar/status/2101546297496834493

### Load-testing a system design in a simulator
- **Creator:** @uthman_dev · **Date:** 2026-09-12
- **What it suggests:** Describes designing a URL shortener targeting 100 million requests per day — built and tested in a simulation tool, with an architecture image. The post is short and complete. Verifiable: this is a system-design exercise executed in a simulator rather than just whiteboarded — the design was built and load-tested against the 100M req/day target. For learning, the pattern is the takeaway: don't just draw the architecture, simulate the load. The image presumably shows the design; discussion at the permalink.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Validate system designs by simulating target load, not just whiteboarding the architecture.
- **Source:** https://x.com/uthman_dev/status/2098799345373954060

### Second batch (Aug 24 – Sep 12)

### Kiro's manifesto: frontier engineering for AI-tool developers
- **Creator:** @clare_liguori · **Date:** 2026-09-09
- **What it suggests:** "I just published a manifesto for all the developers out there who use an AI coding tool, but feel li[ke something is off, truncated]" — kiro.dev ("Frontier engineering"). 52 replies, 282 reposts, 1,893 likes. A manifesto aimed at developers who use AI coding tools but feel uneasy — presumably arguing for a more engineering-disciplined approach to AI-assisted development (spec-driven, verified, systematic) over vibes. Manifestos matter less for their arguments than as coordination points: this is where the "frontier engineering" school is naming itself. Read the full piece at the permalink; file its principles next to the factory posts.
- **Repos/tools:** kiro.dev
- **Extractable skill:** Name your engineering discipline for AI-assisted work; vague unease becomes improvable practice once it's specified.
- **Source:** https://x.com/clare_liguori/status/2097836812958097915

### Uber published what its agents actually cost
- **Creator:** @Saboo_Shubham_ · **Date:** 2026-08-30
- **What it suggests:** "Uber published what its agents actually cost. 70%+ of pull requests now come from agents. 3,600 age[nts, truncated]." Real numbers from real scale: the majority of PRs at Uber are agent-authored, across thousands of agents — and they published the cost. This is the tokenomics benchmark this whole batch points at: when a company operating at Uber's scale puts real cost figures next to real throughput figures, every enterprise tokenomics program gets a reference point. The 70% figure also marks the phase change: agents aren't assisting engineers anymore, they're the primary producers with humans reviewing. Full numbers at the permalink; pair with the Uber factory article below.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Benchmark your agent program against published at-scale numbers (Uber: 70%+ agent PRs); cost-per-PR is the metric.
- **Source:** https://x.com/Saboo_Shubham_/status/2093944679104659608

### "Software Factories" — the emerging-architecture article
- **Creator:** @JoshARosen · **Date:** 2026-08-30
- **What it suggests:** "Article 'Software Factories: Emerging Architectures and Why Frontier Labs Should Care' — Software factories are suddenly everywhere. Factory.ai (which is called Factory throughout) has made [truncated]." The concept piece for this batch's factory theme: software factories as an emerging architecture category, with Factory.ai as the reference implementation and frontier labs as the audience that should care. Read alongside the Zach Lloyd factory talk and the Uber/LimestoneHQ factory posts — the category is consolidating from scattered experiments into named architecture.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Track the software-factory category as it consolidates; reference architectures are emerging now.
- **Source:** https://x.com/JoshARosen/status/2094075909242294713

### Running a Software Factory Efficiently at Uber Scale
- **Creator:** @UberEng · **Date:** 2026-08-28
- **What it suggests:** "Article 'Running a Software Factory Efficiently at Uber Scale' — Post author: @udaykiran. Introduction: AI tools are now embedded in every phase of software developm[ent, truncated]." 63 replies, 951 reposts, 4,810 likes — the most-shared factory piece in the batch. Uber Engineering describing AI tooling embedded in every phase of development at their scale, with efficiency as the explicit topic. This is the enterprise end-state document: not a pilot, not a lab result — every phase, at scale, with efficiency engineering. For a tokenomics and context-management remit, this is the closest thing to a peer playbook in the public domain; read the full article via the permalink and map its phases to your own rollout.
- **Repos/tools:** None linked in post text.
- **Extractable skill:** Map Uber's factory phases to your rollout; treat their efficiency work as the peer benchmark.
- **Source:** https://x.com/UberEng/status/2093444169037762840
