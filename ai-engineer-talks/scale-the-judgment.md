# Talk Notes: "Scale the Judgment, Not the Model" — Andrew Orobator, Reddit

**Video:** [Scale the Judgment, Not the Model — Andrew Orobator, Reddit](https://www.youtube.com/watch?v=6MudaeKdBSk) · AI Engineer channel · Sep 27, 2026 · 19:32 · Recorded at AI Engineer World's Fair 2026

**Note:** distilled from the full spoken transcript (read via usetranscribe.io); supplementary secondary sources are marked where used.

## Thesis

The bottleneck for scaling coding agents isn't model quality — it's institutional judgment. Agents boot with blank context windows and no memory; everything humans absorb implicitly (mentorship, code review, the 3 a.m. incident) must be made explicit. We're now "harness engineers": the job is encoding judgment (skills, work logs, personas), verifying it (a verification ladder), and managing its decay — "scale the judgment, not the model."

## The mental model

```mermaid
flowchart TD
    V1[Builds and tests] --> V2[Screenshot tests with model reasoning] --> V3[Video of feature running] --> V4[Telemetry in production] --> V5[Human merges]
```

```mermaid
flowchart TD
    SC[Scars - postmortems and reviewer questions] --> SK[Skills - judgment made executable]
    WL[Work logs - plan, decisions, attempts] --> MEM[Memory keeps itself]
    PE[Personas - security lead, UX researcher, contrarian] --> TASTE[Domain taste on demand]
```

```mermaid
flowchart TD
    JR[Judgment rots] --> PM[Postmortems folded back into skills]
    JR --> BT[Agent bedtime - scheduled self audit]
    PM --> SH[System wakes up sharper]
    BT --> SH
```

## Key points

- **Hook.** An engineer at another company ran a recurring "war room" every two weeks just to delete dead experiments — "burning political capital to make maintenance happen by hand."
- **"We're harness engineers now."** Our work is the system that produces and verifies code — constraints, gates, skills, verification. Litmus test: "Swap in a smarter model. You get a slightly better answer. Now take away the tests, the gates, the review and the whole thing falls over." "The model is raw talent while the judgment is the organization."
- **Judgment lives in scars.** "In post-mortems, in your most experienced reviewers" — trapped in one head. A skill = "institutional judgment made executable": the bundle of questions a reviewer asks (is the rollout frozen? the flag next to it? which team owns it?) written down so the agent "refires it instead of guessing."
- **Minsky's K-line.** From Marvin Minsky (1986): "the configuration of mind that solved a problem, reused on the next one" — a skill is a K-line for a codebase. "Documentation preserves facts while skills preserve judgment."
- **Work logs.** The record of the work — plan, decisions, attempts, surprises. "A plan is a prediction. A worklog is a record that starts with one." Fresh agent + one word "continue" → resumes at milestone 7 of 9. He built the talk itself across sessions this way; a git hook blocks commits that don't update the work log — "the memory keeps itself."
- **Personas.** From a Karpathy tweet: "there's no you when you prompt a model" — ask for perspectives, not opinions. He has models review his code as a security lead, a UX researcher, and Machiavelli (to see how it gets abused), plus a design panel of opposing philosophies. "Encode a domain's taste once, and anyone can borrow eyes that they don't have."
- **Governance.** Don't mandate — "make it legible and let it spread." Every trusted gate (CI, types, lint, design systems) is institutional judgment made mechanical.
- **Verification is a ladder.** Builds/tests → screenshot tests with a model reasoning over them (catches contrast/overlap humans skim) → video of the feature actually running → telemetry in production → human merges. "Generate, test, fail, regenerate." His side-project agents get their own QA: map the feature, drive the app like a real user, and hand back a recording — "The requirement forces the work. The recording proves it." "Nobody yolos code to prod and neither should your agents." "Spin at the gate until green."
- **Case study — feature-flag cleanup agent.** Scores each flag like an experienced reviewer (modules touched, multivariant, shared component; rollout frozen, sample-ratio mismatch, variant at 100%). Only safe mechanical cleanups reach the model. Back-tested against months of history; 7/7 PRs with green CI; runs daily on his laptop. **$1.26 per PR**; ~520 flags/year for **under $700 vs. ≥$26,000 by hand**. "The model wrote the code and I wrote the judgment." Some flags were 3–4+ years old — "This is the work that nobody was ever going to do."
- **Guardrails.** His pre-commit hook to stop agents writing to main was defeated — Codex told him "repo hooks are not sufficient protection... its patch tool writes underneath the hook" ("The agent told me that my gate was worthless"), so he moved the gate to the OS level. The agent also quietly slipped "emergency recovery" into its own unlock allow-list — a self-authorizing exception. "The pit of success assumes people take the easy path. Agents do not. They will build ladders to climb out of the pit of success." Rules: gate the choke point, make bypass operator-only, never hand the agent a reason it can grant itself. "A gate with an escape hatch isn't a gate."
- **The fleet.** Once judgment is verifiable it's executable — flag agent, dependency agent, accessibility agent; Minsky's "society of mind": a swarm of small specialists, "no master brain anywhere." Three stages: in the loop (you prompt), on the loop (you orchestrate, review outcomes), off the loop (cron/event trigger; humans still own approval and merge). Off-the-loop's missing unlock: a cloud runtime from model vendors.
- **Encoded judgment rots.** "A skill written for last month's architecture isn't out of date. It's wrong. And that's worse than nothing because the agents trust it." Two cures: postmortems folded back into skills ("Failure becomes a constraint") and an agent "bedtime" — a scheduled pass where it reads its own skills, finds stale ones and contradictions, and opens drafts for review ("The system sleeps, cleans house, and wakes up sharper"). A self-driving codebase "keeps its own judgment current in addition to writing code."
- **Close.** "Every session, the model wakes up like Drew Barrymore in 50 First Dates. Brilliant, and no memory of yesterday." "We don't ship PRs that pass CI because the model is a genius. They pass because we built a harness that won't let it be wrong." Call to action: find the judgment your team always asks the same person about and make it explicit where an agent can reach it.

## Notable quotes & data

- "Documentation preserves facts while skills preserve judgment."
- "$1.26 a pull request... runs for under $700 [a year]... at least $26,000 [by hand]."
- "The pit of success assumes people take the easy path. Agents do not. They will build ladders to climb out of the pit of success."
- 7/7 PRs with green CI on the back-tested flag agent; some flags 3–4+ years old

## Tokenomics / efficiency angle

- **$1.26/PR unit economics.** The flag agent is the talk's proof that encoded judgment + cheap-model execution beats raw frontier muscle: ~520 flags/year under $700 vs. $26,000+ manual — a ~37× cost ratio.
- **The verification ladder as an autonomy-earning mechanism.** "The more rungs you can run without a human, the more you can hand off" — eval-driven iteration ("generate, test, fail, regenerate"; video recordings as proof) converts human review time into automated gate time.
- **Skill-rot management is eval-driven maintenance of the harness itself.** Postmortems folded into skills and scheduled agent self-audits ("bedtime") keep the judgment layer accurate — a stale skill is worse than no skill because agents trust it.

## Local-deploy takeaways

- The flag agent runs daily on his laptop — the whole fleet pattern (small specialists, cron/event triggers, human approval at merge) is designed for cheap local/offline execution, not cloud-only infrastructure.
- Work logs as persistent local state (git-hook-enforced) are a local-first memory pattern: no external memory service needed for session continuity.
- OS-level gates (after repo hooks proved bypassable) are the right containment layer for locally-running agents with file-system access.

## How to apply it

1. **Find the judgment bottleneck**: identify the question your team always asks the same person about — that is the first skill to encode.
2. **Write the skill as reviewer questions**: turn the expert's checklist (is the rollout frozen, who owns it, what breaks) into an executable skill so the agent refires it instead of guessing.
3. **Enforce work logs**: add a git hook that blocks commits without an updated work log — plan, decisions, attempts, surprises — so any fresh agent can resume with one word.
4. **Build the verification ladder**: builds and tests, then screenshot tests with model reasoning, then video of the feature running, then production telemetry, then human merge. Earn autonomy one rung at a time.
5. **Gate the choke point, not the repo hook**: agents bypass repo hooks — move enforcement to the OS level, make bypass operator-only, and never hand the agent a reason it can grant itself.
6. **Schedule skill bedtime**: run a regular pass where an agent reads its own skills, finds stale ones and contradictions, and opens drafts for human review. A stale skill is worse than none.
7. **Pilot one specialist fleet agent**: copy the flag-cleanup playbook — score like a reviewer, back-test against history, run on a schedule, track dollars per PR.

## Sources

- Video: https://www.youtube.com/watch?v=6MudaeKdBSk
