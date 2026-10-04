# GitHub Copilot Storage/Memory Map: What's Local, What's Cloud

**Source:** Companion graphic to the r/ClaudeAI "Claude storage/memory map" post (u/BenSimonDev, Oct 4 2026) — same dark green/amber visual language, applied to GitHub Copilot. Facts verified via web research, Oct 2026.

![GitHub Copilot storage/memory map](github-copilot-storage-memory-map.png)

## Thesis

Copilot's latency-critical work is all client-side — context extraction, ranking, and prompt assembly happen on your disk — but every inference is a cloud call, and retention/training policies differ sharply by plan and surface. The map's punchline: zero-data-retention is real but surface-specific, and content exclusions are not airtight.

## The map (text version)

**On your disk:**
- Client-side extraction — prefix/suffix, open tabs, import graph gathered per keystroke
- Local ranking — Fixed Window Jaccard Matcher, no local neural model
- Prompt assembly — context batched into the prompt payload before any network call
- `.github/copilot-instructions.md` — injected into every prompt by the client
- Agent-mode edits — files + terminal commands run in your workspace
- Telemetry opt-out — a local setting (`github.copilot.advanced.telemetry.enabled: false`)

**Their servers:**
- Completions API — `POST api.githubcopilot.com` with the assembled prompt
- Copilot Chat — prompt + history sent every turn
- Retention: IDE completions/chat on Business/Enterprise = **zero retention** (in-memory, discarded); github.com/CLI/mobile chat = 28 days; engagement data = 2 years; coding-agent logs = life of account
- Training: Business/Enterprise = **never**; Free/Pro/Pro+ = **opt-out since Apr 24, 2026**; third-party models contractually barred from training/retention
- PR code review — diff analyzed on github.com; coding agent — ephemeral GitHub Actions cloud environment

**Either (a setting decides):** Content exclusions — excluded paths filtered locally, **but agent mode can still `cat` them**, and file names/paths can leak indirectly.

## Notable facts

- Zero data retention is surface-specific: IDE completions/chat for Business/Enterprise are discarded; the same org's github.com chat, CLI, and mobile usage falls in the 28-day bucket.
- Since Apr 24, 2026, Free/Pro/Pro+ interaction data is used for model training by default — toggle off at Settings → Copilot.
- Processing happens in Microsoft Azure; EU Data Boundary options exist for Enterprise.

## Local-deploy takeaways

- The most data ever leaves via Chat and the coding agent — for sensitive codebases, prefer inline completions (zero-retention on Business) and local agent-mode edits over cloud chat threads.
- Don't rely on content exclusions as a security boundary for agent mode — they don't cover it.
- Free/Pro users: check the training opt-out toggle; it's off-by-default only for paying business tiers.
