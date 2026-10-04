# Spotify's shunt — routing agent I/O to cheap models

**What it is.** Spotify's open-sourced internal Claude Code setup (via the `spotify/portal-ai-plugins` marketplace): a plugin called **shunt** plus two cheap worker modes running through Spotify's Portal CLI. Headline claim: **~90% token savings on bulk reads** in their Java monorepo.

**How it works.** The insight: most of what a coding agent does all day isn't thinking — it's I/O. Reading five files to answer a question about one method; writing a test that copies the twenty next to it. Zero reasoning required, but billed at frontier rates. Spotify's fix has two parts:

1. **Two cheap workers** (each one YAML file: a prompt, Gemini 2.5 Flash, temperature 0.2): *bulk-reader* reads files and returns structured bullets; *code-writer* reads a reference file and writes matching code straight to disk.
2. **The shunt plugin** (3 layers): *Hooks* — any full-file Read over 350 lines (configurable) is **blocked**, and Claude is told to use bulk-reader instead (targeted reads still pass); *Scripts* — wrap the Portal CLI, ship files to the worker; *Skills* — markdown files with the invocation syntax.

The raw files and generated code **never enter Claude's context**. And the critical design lesson: Spotify *first* tried putting the routing rules in CLAUDE.md — advisory rules Claude read and then ignored. Hooks made the behavior **enforceable**. Skip the skill and the large read still gets blocked.

**Install.**
```
claude plugin marketplace add spotify/portal-ai-plugins
claude plugin install portal@portal
claude plugin install shunt@portal
```
Then `/portal:setup` to authenticate the Portal CLI. The bulk-reader/code-writer modes are public and reusable; forking them in Portal lets you swap the worker model or instructions without touching the plugin.

**Key numbers — with the caveats.** The ~90% is measured on *Claude's context tokens only* (chars/4 proxy), over four synthetic scenarios; it excludes the worker model's tokens and Portal cost. An independent reconstruction found **86–91% all-in** dollar savings for the measured case, so the claim roughly survives — but note the costs it omits: each delegation adds a **10–30s round trip**, small files aren't worth routing (that's what the 350-line threshold is for), and the cheap model **can't do editing or safety-critical reasoning** (it missed a subtle thread-safety bug the frontier model caught in seconds). A free alternative keeps just the blocking hook and points Claude at targeted reads / local tree-sitter outlines — nobody has measured that variant's real bill impact.

**Why it matters for tokenomics / context management.** This is the I/O-vs-intelligence split made deployable: *route the grunt work, don't just buy a smarter model.* And the meta-lesson is pure context-layer governance — **advisory rules in prompts get ignored; enforcement belongs in the harness** (hooks). For an enterprise rollout, the shunt pattern generalizes: identify your highest-volume zero-reasoning operations, put a cheap model behind a hook, and measure the crossover point where delegation overhead exceeds savings.

**Links.** Plugin marketplace: `spotify/portal-ai-plugins` (install via the commands above) · Coverage with install details: https://onlinestool.com/blog/portal-by-spotify-cut-my-claude-code-token-usage · Independent analysis of the 90% claim: https://github.com/jrichlen/agent-plugins (PR #133 research note).
