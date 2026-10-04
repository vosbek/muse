# jevgrep — Jev-powered code research CLI

**What it is.** A research-agent CLI by David Zhang that lets a coding agent find the right files by asking what the code *does* instead of where it lives. You ask `jg "How are telemetry events recorded and sent?" ./my-project` and get back relevant files, reading leads, and verbatim source excerpts in one stdout response. Relevance judgment is done by TypeSafe's Jev decision model, not by the expensive frontier model driving the agent.

**How it works.** Jevgrep explores the repository hierarchy and follows qualifying branches, selects files using content previews, then identifies useful source units and surrounding context. It keeps qualifying file locations even when it can't confidently return an excerpt, and doesn't force every search into a fixed top-N list. Output order is deliberate: summary and compact file list first, then selected source with line references, then detailed declaration and call locations. Declaration parsing covers Python, TypeScript/JavaScript, Go, and Rust; other text gets a fallback. The output is evidence for the agent to use — not a generated answer, and not a guarantee every relevant file was found. When you already know an exact symbol or path, a direct read or `rg` is still the right call; jevgrep earns its keep on questions spanning unfamiliar files.

**Run it locally.**
```sh
npm install -g @dzhng/jevgrep   # requires Node.js 22+
jg auth                          # key for Vercel AI Gateway, TypeSafe, OpenRouter, OpenCode Zen, or a custom TypeSafe-compatible endpoint
jg skill                         # installs the agent skill (Claude Code, Codex, OpenCode…) — required, the CLI alone doesn't teach the agent to use it
jg "Where is authentication checked before a request reaches a handler?" .
```
`jg skill` detects your agents and asks where to install (`--global` for user-wide, `--yes` for unattended). It delegates to the `skills` CLI; you can also run `npx skills add dzhng/jevgrep --skill jevgrep` directly. The bundled skill makes the agent check for `jg` and install the CLI if missing; authentication still needs your provider key. Upgrade with `npm install -g @dzhng/jevgrep@latest` and re-run `jg skill` (skill files in projects aren't overwritten on upgrade).

**Key numbers (from the repo's own evals, not the X hype).** Ten tuned Python SWE-bench tasks: jevgrep and the no-Jev baseline both solved 8/10. Full solution cost fell from **$7.62 to $5.44 — a measured 28.6% reduction** (rounded to "~30%" in the README), including failed attempts and excluding Jev cost. A 0.4.3 rerun including Jev cost measured **25.8% lower total cost** with the same 8/10 solved. Note the gap vs the "40% (verified on SWE-bench)" claim in the launch post — the repo's published methodology supports ~26–29%. Per-task costs and limitations are in `evals/results/` in the repo.

**Why it matters for tokenomics / context management.** This is retrieval-as-cost-control made concrete: the most expensive part of an unfamiliar coding task is the agent wandering the repo, loading files into context that turn out irrelevant. Jevgrep inserts a *cheap* decision model (Jev) at the triage step so the *expensive* model only reads what matters. It's the same pattern as the Jev MCP tool-selection idea — spend pennies on judgment, save dollars on context. For an enterprise rollout, this is a drop-in context tax cut: better first-retrieval means shorter sessions, fewer wasted turns, and less context rot from irrelevant files.

**Links.** Repo: https://github.com/dzhng/jevgrep · Eval methodology: `evals/results/relevance-threshold-2026-09-27.md` in the repo · Skill: `skills/jevgrep/SKILL.md` in the repo.
