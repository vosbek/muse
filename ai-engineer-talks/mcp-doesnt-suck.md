# Talk Notes: "MCP Doesn't Suck. Your Agent Does." — Jan Čurn, Apify

**Video:** [MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](https://www.youtube.com/watch?v=pAnLpiAG6Es) · AI Engineer channel · Oct 2, 2026 · 18:43 · Recorded at AI Engineer World's Fair 2026

**Note:** YouTube's transcript was unreadable in our environment, so this is distilled from the video's own description/chapters plus biggo.com's AI-generated talk summary — treat secondary-derived points as the speaker's arguments per those summaries, not verbatim transcript. Partial auto-transcript chunks via NoteGPT covered the opening through ~07:20.

## Thesis

The backlash against MCP is misdirected — the protocol is sound, and the failures people blame on it (context bloat, cost, sensitive data sitting in context, poor tool discovery) are failures of naive agent harnesses, not the protocol. The fixes already exist (subagents, progressive tool discovery, code mode) but most clients ignore them; Apify's open-source **mcpc** wraps the full MCP protocol behind a single bash-style tool call, and the right architecture is "MCP for remote, CLI for local" — MCP plus CLI beats either alone.

## Key points

- **The critics' catalog.** Anthropic itself admitting "MCP sucks"; Theo calling it "the wrong abstraction"; "MCP was a mistake, long live CLIs"; "MCP is dead in the water"; "MCPs are mostly useless, I'll die on this hill"; "every MCP could have been a deterministic CLI"; Gary Tan ("MCP sucks, honestly, oh my god"); Peter Levels ("Thank god MCP is dead").
- **The core complaint mechanism.** Early agents registered every tool from every connected MCP server into context up front — ~10 servers × ~10 tools ≈ **100 tools loaded before any user request**, potentially a third of the context window gone. Tool results then append, rot, lose accuracy, and cost money.
- **The spec says nothing about harness design.** "It's your job when you're building your agent to make sure you use MCP effectively. It's not a problem of the protocol."
- **Scale.** Introduced by Anthropic ~2 years before the talk (~2024); an estimated **10,000–15,000 servers**; registries of registries; now used by Claude and ChatGPT for tools/connectors.
- **Three remedies emerged in late 2025:**
  1. **Subagents** — delegate to a subagent with its own context. Limitation: tokens still cost; passwords still sit in a context abusable by other tool calls; it only pushes the problem further.
  2. **Progressive Tool Discovery** — Anthropic's "Tool Search Tool," then Cursor; load tools only when needed. Limitation: clients must actually implement it.
  3. **Code Mode** — Cloudflare; treat MCP tools as code, models navigate via grep. Limitation: Cloudflare's implementation is tightly platform-coupled and hard to use.
- **Why Code Mode works:** models are better at writing/calling code than at tool calling, because tool calling is an artificial construct synthesized into training data rather than something present in real-world data. "Most agents are living in the dark ages" — the protocol evolved, clients didn't.
- **Why CLIs win locally:** agents never load a full CLI into context; they explore progressively, know basic Linux commands from training data, learn from `--help`, and run CLI tools as code — Code Mode is native to CLIs. Unix shell dates to **1969** (Ken Thompson, Dennis Ritchie); the ~80-column terminal is a representation refined over decades; "agents know shell by heart," and labs can synthesize effectively unlimited shell training data.
- **CLI's structural weakness:** "a local black box with no standard out and transport protocol" — for enterprise use you must introspect whether it uses API or websockets, and you cannot cleanly inject credentials. Hence: **CLIs for local, MCP for remote.**
- **mcpc (demoed live).** Apify's universal CLI client for MCP; began as a hobby project in **December 2025** ("the winter of Claude"); claimed "probably the most feature-rich MCP client on the market." Design goals: support everything MCP offers (tasks, resources, prompts), maximize compatibility, stay lightweight with **no LLM inside** (pure CLI wrapper), usable by agents and humans, Code Mode throughout. Every command has `--json` returning spec-compliant JSON, composable with **jq** and shell pipes.
- **Demo specifics.** Connects to a local filesystem MCP server over STDIO (surfaces server name, capabilities, tools, commands; tool lists as JSON); connects to Apify's remote server via browser login with credentials in the local OS keychain; displays the server's **instructions field** — a basic MCP primitive most clients still don't support.
- **Capabilities.** Persistent sessions (set up once; Claude Code/Codex share config without re-auth); progressive discovery via grep (searching "find" → 3 matches on filesystem server, 4 on Apify's); async tasks (`--task` runs server-side while the agent works locally; check progress or detach/reattach — most clients lack this); **x402** support (recently added; local-wallet tooling); sandboxing proxies (mentioned).
- **Connector Evals.** Apify's benchmark framework that flips the usual comparison — holds the agent constant and compares connectors (CLI vs raw MCP vs mcpc). Early results with Claude Code on Sonnet 5: mcpc and CLI comparable on time and token cost; raw MCP faster in one test but consumed more tokens and worse in two others. Čurn is candid the tests are early and invites contributions.

## Notable quotes & data

- "You can provide all the protocol features of MCP through a simple tool call that all the agents already know, just called bash. The full complexity of MCP is hidden behind single tool call bash."
- "Please stop saying CLI is better than MCP because MCP plus CLI is the best." (closing line)
- ~100 tools pre-loaded ≈ a third of context burned before any work happens.

## Tokenomics / efficiency angle

- **Context/token efficiency is the talk's central efficiency theme:** progressive discovery and `--json`+jq piping let scripts "run MCP servers in the background without wasting your context tokens."
- **Connector Evals** explicitly measures token cost and time per connector, framing connector choice as a measurable cost lever.
- **Async tasks** (`--task`, detach/reattach) let agents do local work while long tools run server-side (latency win).

### Local-deploy takeaways

- **mcpc is a pure CLI wrapper with no LLM inside** — the kind of local-first building block that fits a self-hosted agent stack: run it against local servers over STDIO, keep credentials in the OS keychain, no cloud gateway required.
- **Adopt the mcpc pattern in agent harnesses:** one `bash` tool call + `--json` + jq pipelines instead of registering dozens of MCP servers as native tool definitions — converts per-request context cost into progressive, grep-driven discovery.
- **"MCP for remote, CLI for local"** is a deployment principle: keep local tool calls on CLIs (native Code Mode, no transport needed), reserve MCP for remote services where a standard transport and credential injection actually matter.

## Sources

- YouTube description/chapters: https://www.youtube.com/watch?v=pAnLpiAG6Es
- BigGo AI talk summary: https://finance.biggo.com/podcast/ec71d05c7d54d1cc
- Partial auto-transcript chunks via NoteGPT (opening through ~07:20)
