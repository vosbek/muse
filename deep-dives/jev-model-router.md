# Jev model router for Claude Code

**What it is.** A family of Claude Code mods/plugins that route each task or turn to the right model tier *using Jev as the decision-maker*. Implementations found: **satviksinha/jev-model-router** (standalone mod), the **jev-model-router mod in davila7/claude-code-templates** (`productivity/jev-model-router`), and **chrishan17/claude-jev-mod** (adds a `$.jev` helper over Jev for any plugin).

**How it works.** A Jev *Choice* question is asked over model tiers (e.g. nano / fast / balanced / frontier, or haiku / sonnet / opus / fable), each tier described by a one-line rubric of what it's for. Jev returns a probability per tier plus confidence; the router picks the tier and rewrites the request. The davila7 mod exposes three switches, not equally safe:

| Switch | What it sets | Default |
|---|---|---|
| `routeSubagentModel` | model of each subagent, at `agent.spawn` | **on** |
| `routeMainEffort` | reasoning effort of the main conversation, at `turn.step` | **on** |
| `routeMainModel` | model of the main conversation, at `turn.step` | **off** — switching models mid-session invalidates the prompt cache |

Example tier table from one implementation: nano `openai/gpt-5-nano` ($0.05/$0.40 per M), fast `google/gemini-3-flash` ($0.50/$3.00), balanced `anthropic/claude-sonnet-5` ($2.00/$10.00), frontier `anthropic/claude-fable-5.1` ($10.00/$50.00). Editing the tier rubrics is how you change routing behavior.

**Providers.** Jev is reachable several ways; the mod picks by whichever key is set:

| Backend | Endpoint | Notes |
|---|---|---|
| `typesafe` | `POST api.typesafe.ai/v1/systemone` (`TYPESAFE_API_KEY`) | **Preferred** — the only one reporting calibrated confidence per answer, so `minConfidence` thresholds actually fire |
| `vercel` (AI Gateway) | `POST ai-gateway.vercel.sh/…/evaluation-model` (`AI_GATEWAY_API_KEY`, model `typesafe-ai/jev`) | No confidence field; confidence derived from the optional probability distribution |
| openrouter / cloudflare / litellm / custom | various | Same System One wire shape |

**Deploy it locally.**
```jsonc
// ~/.claude/settings.json
{ "env": {
    "TYPESAFE_API_KEY": "...",      // or AI_GATEWAY_API_KEY
    "CLAUDE_CODE_ENABLE_FUNCTION_HOOKS": "1"   // not optional — without it the mod loads and silently does nothing
} }
```
Then `claude --plugin-dir <mod-dir>`; move to `~/.claude/skills/jev-router/` to keep it on permanently. Notes: the router **fails open** — misconfiguration shows up as "mod doing nothing," so run the bundled check script (`npm run check-jev`) when nothing routes. The Vercel gateway needs a card on file even for free credits. The gateway's evaluation endpoint isn't publicly documented; one implementation read it from the AI SDK source.

**Why it matters for tokenomics / context management.** This is the deployable version of the oldest cost insight in the playbook: *most turns don't need the frontier model*. The design details are the valuable part — route subagents (the volume) aggressively, route main-loop *effort* but not the main-loop *model* (cache invalidation), gate escalation on calibrated confidence, and fail open so a router outage never breaks the session. For an enterprise, this is the reference implementation to copy before building a bespoke router.

**Links.** https://github.com/satviksinha/jev-model-router · Mod: https://github.com/davila7/claude-code-templates (`cli-tool/components/mods/productivity/jev-model-router/`) · `$.jev` helper: https://github.com/chrishan17/claude-jev-mod.
