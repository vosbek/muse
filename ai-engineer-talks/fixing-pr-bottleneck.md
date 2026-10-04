# Talk Notes: "Fixing the PR Bottleneck" — Matt Pocock, AIHero

**Video:** [Fixing the PR Bottleneck — Matt Pocock, AIHero](https://www.youtube.com/watch?v=LlgiOCmFG_w) · AI Engineer channel · Sep 25, 2026 · 22:34 · Recorded at AI Engineer World's Fair 2026

**Note:** distilled from the full spoken transcript (read via usetranscribe.io); secondary sources are marked where used.

## Thesis

AI agents massively increased PR volume — the "software factory," where agents rather than humans initiate work (classifiers turning bug reports into fixes, PlanetScale slow-query reports auto-triggering work) — which without brakes becomes a "slop cannon." The fix is three quality brakes — automated checks (cheap, deterministic), automated review (agents as lie detectors for the checks), and human review — arranged so that raising code quality counterintuitively speeds everything up: better code needs fewer human interventions. Key mechanisms: deep-module codebase design, coding standards enforced at review time rather than implementation time, one-way vs two-way door triage, human-friendly PR bodies, and a "retro" skill that compounds review learnings back into checks and standards.

## Key points

- The PR bottleneck predates AI (piles of unreviewed PRs), but AI massively increased the strain. The central promise of AI: agents let us scale up — "do more with less."
- **The "software factory"** (his "biggest buzzword of the day"): humans no longer initiate all work — agents do. Examples: a classifier turning bug reports into fixes/repros; PlanetScale slow-query reports triggering work; deterministic code (not humans) firing factory steps. Acceleration pushes more code through — but with only acceleration and no brakes, "you're going to end up with a slop cannon."
- **Brakes** = mechanisms that slow down to increase quality, preventing a "software entropy nightmare" — because code is the environment your agent operates in, and "bad code begets more bad code." Three brakes form a cake: automated checks → automated review → human review. Goal: make human review faster by leaning on the first two. First principle: "stop the slop" — higher shipped quality → less human review → counterintuitively faster.
- **Automated checks (layer 1) are cheap:** no tokens (unlike automated review), no human effort — just CPU cycles. (Tokens spent fixing agent bugs that tests catch are "tokens pretty well spent.") Layer loads of them on; most repos underuse them.
- **Checks can lie:** green CI ≠ ready to merge. Human and automated review are "lie detectors" for the checks.
  - **Lie 1 — tautological tests:** tests that reassert the implementation ("Opus 5 got addicted to these") — e.g., X-post char limit = 280, tested by expecting the limit to be 280. Extremely structure-sensitive: renaming a constant breaks the test.
  - **Lie 2 — structure-sensitive UI test:** reads the source file into memory and asserts "videos" appears after "content plan" in the source text, instead of rendering — any layout change breaks it.
  - **Lie 3 — tests that cannot fail:** abused mocking (useAudioBoost stubbing the DOM AudioContext with fakes) never exercises real error modes → strange production failures.
- **Design your way out: deep modules** (John Ousterhout, *A Philosophy of Software Design*) — module A hides a large implementation behind a tiny interface (deep); module B exposes a large interface where each function does little (shallow). Deep modules → fewer structure-sensitive tests, because tests sit at the interface. His codebase-design skill finds deepening opportunities and emits a before/after HTML doc (reducing duplication, creating deep testable modules) — works even on the "craziest vibe-coded codebase." It also defines a shared team language: locality (related code located together), leverage (caller gets big value from a simple call), seam.
- **Don't put coding standards in the implementer agent:** implementation is OVERLOADED (explore + change + debug in one context window) — standards make it worse. Instead, a code-review skill receives the diff, reads coding-standards.md from the repo, and checks compliance — running in a SUBAGENT with its own context window and budget; review is UNDERLOADED (a little exploration, no implementation/debugging), so it absorbs standards far better. Two-part process: implement = make it work; review = make it good — red-green-refactor across two context windows. Keep standards out of AGENTS.md (drowns the implementer); coding-standards.md is for the reviewer only.
- **Don't outsource automated review:** generic third-party reviewers (Cursor bugbot, CodeRabbit) are too general (false positives) or too specific (TypeScript-only, useless for Rust). Build your own; accumulate coding standards over time; share them across the team; put those unread docs to work.
- **The reviewer should COMMIT, not comment:** verbose PR comments just create triage work for the human. Default to commits that fix findings; comment only on genuine questions — so the human reviews "a really nice artifact." "Stop trying to one-shot good code."
- **Human-friendly PRs** (his upcoming "PR skill"):
  - **Principle 1 — not all reviews are equal;** triage with AWS one-way vs two-way doors. Most PRs are two-way doors (merge + revert — "the glorious benefit of software vs civil engineering"), but nuance matters: a trivial change that emails 60,000 people is a one-way door; expensive migrations/data loss = one-way door → "review the hell out of that PR." Attach a "merge danger" summary (door type + blast radius): two-way door with localized blast radius → light review.
  - **Make the "why" fast to grasp:** pseudocode and diagrams over prose (credit: the "show me" skill by Dex Hadley, humanlayer skills repo) — mermaid/UML sequence diagrams, CLI command/flag summaries. "It's hard to overstate" the difference.
- **Review the system, not just the code:** the process producing the code matters as much as the code — "never write the same comment twice"; never catch the agent doing the same thing across two PRs. The mechanism is his new **"retro" (retrospective) skill:** feed it a session, a PR+session, or a week's PRs+reviews, and it suggests new automated checks and coding-standards.md updates — a compounding effect where each human review raises the quality of the next. Retro also audits navigation pointers (add AGENTS.md pointers), tool economy (token efficiency of tools used), and bloat (bloated steering files/skills → reorganize).
- **Goal:** make human review fast, simple, and optional — "you really don't need to review every single two-way door. Every single one-way door you do."
- Skills at aihero.dev/skills; v1.3 shipping that week. Most-viewed of the eight at ~147K views; talk given in Paris.

## Notable quotes & data

- "If you just have permanent acceleration pushing stuff through your factory, you're going to end up with a slop cannon."
- "Code is the environment your agent operates in. If you have bad code in your codebase, that is going to beget more bad code."
- "Automated checks are cheap… they don't cost tokens like automated review does… just CPU cycles."
- "Does a green CI mean that the code is ready for merge? No, it does not."
- "Stop trying to one-shot good code."
- "You never want to write the same comment twice."

## Tokenomics / efficiency angle

- Automated checks cost CPU cycles, not tokens or human effort — layer them aggressively; tokens spent fixing test-caught agent bugs are "tokens pretty well spent."
- The retro skill explicitly audits **tool economy** (token efficiency of tools used) and steering-file/skill bloat (bloated skills → reorganize).
- Reviewer commits fixes directly (saves human triage); one-way/two-way-door triage focuses scarce human attention where it matters; the underloaded reviewer subagent keeps the implementer's context window lean.

## Local-deploy takeaways

- The overloaded-implementer / underloaded-reviewer split is a context-management pattern to adopt everywhere: keep standards out of AGENTS.md (drowns the implementer), run review in a separate subagent with its own context window and budget.
- Checks-first is the cheapest quality spend: deterministic CPU-cycle checks before any token-burning review — build the check layer before the review layer.
- Run the retro loop locally: feed a week's PRs+reviews to a retrospective pass that proposes new checks and standards updates — each review compounds, and the retro explicitly audits token economy and steering-file bloat.

## Sources

- Video page: https://www.youtube.com/watch?v=LlgiOCmFG_w
- Full transcript: https://www.usetranscribe.io/yt/LlgiOCmFG_w/pr-bottleneck-fix
