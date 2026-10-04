# show-me — the visual-explanation skill

**What it is.** A skill in the `humanlayer/skills` repo (`plugins/show-me/skills/show-me/SKILL.md`) that teaches a coding agent to explain the current topic *visually* instead of in prose. Its frontmatter sets `disable-model-invocation: true` — it's a skill the agent (or user via `/show-me`) invokes deliberately, not something that fires on its own.

**How it works.** The skill gives the agent a decision procedure: skip the preamble, keep prose brief, and **pick the smallest view that makes the key point clear**:

- **Pseudocode** for logic or algorithms (e.g. an `on(save)` cache-check sketch)
- **Call trees** for runtime control flow (`submitForm → createSession → persistPrompt…`)
- **Component trees** (tsx) for UI structure, including state and module boundaries with file paths
- **File trees** for refactors and file responsibility
- **Mermaid diagrams** (sequence diagrams) for component interaction and data flow
- **`diff`-shaped views** matched to the change: component diffs, file-layout diffs, call-stack diffs, state-transition diffs
- **Full code blocks** when most of it is new or the user needs a copyable target shape
- **Focused HTML artifacts** — a diagram, infographic, or short slide deck matching the product's colors/spacing/components, opened via `Bash(open …)` — for anything too dense for Mermaid

Guidance: place each visual next to the short text it supports; keep only the calls, files, props, states, and boundaries needed; you may use one view or several, "it is unlikely you will use all of them. Use your judgement and don't overwhelm the user."

**Install.** It's part of the humanlayer skills collection: clone https://github.com/humanlayer/skills and install the `show-me` plugin (`plugins/show-me/`), then invoke with `/show-me`.

**Why it matters for tokenomics / context management.** Indirect but real: output tokens are half the bill, and a diagram routinely replaces paragraphs of explanation — *visual-first responses compress the output side*. More importantly, the "smallest sufficient view" discipline is context economy applied to UX: the skill explicitly trains the agent against the failure mode of dumping everything it knows. For an enterprise building agent UX standards, this is a template for response-shape governance — constrain *how* the agent answers and you constrain what it costs.

**Links.** Repo: https://github.com/humanlayer/skills · Skill file: `plugins/show-me/skills/show-me/SKILL.md` in the repo.
