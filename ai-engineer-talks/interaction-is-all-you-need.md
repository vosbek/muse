# Talk Notes: "An Interaction Is All You Need" — Ivan Leo, Google DeepMind

**Video:** [An Interaction Is All You Need — Ivan Leo, Google DeepMind](https://www.youtube.com/watch?v=8aVbXXvJUY4) · AI Engineer channel · Oct 3, 2026 · 17:03 · Recorded at AI Engineer World's Fair 2026

## Thesis

Models became agents but APIs didn't keep up — Google DeepMind rebuilt the API surface: the Interactions API (server-side state via interaction IDs, thought signatures handled automatically, a steps data model, strongly typed outputs) plus Managed Agents (the Antigravity harness running in the cloud with persistent sandboxes), with a credential-injecting proxy so agents can call private APIs without ever seeing tokens.

## Key points

- **Evolution**: single completions → function calling (JSON payloads) → models that reason and act → agents; the "agent = LLM in a loop" scaffolding is falling away (models now just use a bash tool directly).
- **Why a new API**: older endpoints were deeply nested objects; new workloads (deep research agent, spawning agents, multimodal) need the Interactions API.
- **Server-side state**: thought signatures — manually managing them was brittle (a single whitespace broke it); with the Interactions API you return the same interaction ID and context is preserved.
- **Demo (Vampsy)**: Nano Banana image variations ("Nanovana") chained into Omni-model video generation via interaction ID; code pattern: Gemini 3.1 Flash image → take the interaction ID → client.create with the Omni flash model.
- **Strongly typed outputs**: every output is demarcated by a strong type; same client.create method, just change the response modality.
- **Tool use**: mix built-in and custom tools — URL context tool retrieves web pages; the model figures out what information it needs rather than being told.
- **Steps data model**: replaces the legacy outputs array with a discriminated union of steps; records model output, thought signatures, function calls, content types (audio/video).
- **Managed Agents**: Antigravity as a remote agent — the harness is co-trained with Gemini; a single API call gets you a sandbox; demo analyzed a GitHub repo autonomously (boots a remote sandbox, reads files, generates a report).
- **Persistent sandboxes**: interaction ID + environment ID route to the exact same context/sandbox; no state-persistence management.
- **Loading sources**: GCS buckets, GitHub repos, inline files; installed packages persist.
- **Same agent locally and in the cloud**: tune locally in the Antigravity IDE, package into a folder, upload — same skills, same harness, same prompt.
- **Credential-injecting proxy**: the model never sees credentials; the proxy intercepts outbound calls and injects the GitHub API token dynamically; even if prompt-injected and "leaked," the attacker only sees code that runs against the GitHub API.

## Notable quotes & data

- "You only pay for the model. You don't pay for the storage. You don't pay for the sandbox." (named agents — up to 1,000 per account)
- 2M tokens burned analyzing a repo built on a custom DSL (reinforcement-learning environments / Scratch-like).
- Gemini API CLI open-sourced; an Interactions API migration skill is fed to coding agents and regularly evaluated.

## Tokenomics / efficiency angle

- Named agents: pay only for model usage, not sandbox or storage.
- Server-side state and persistent sandboxes avoid re-sending context or rebuilding environments.

## Local-deploy takeaways

- **Server-side state as a pattern**: persistent session handles (interaction IDs) eliminate re-sending full context on every call — mirror this in local agent design by keeping long-lived session state server-side rather than rehydrating prompts.
- **Credential-injecting proxy for local agents**: agents never see API tokens; the proxy injects them at call time — a clean security pattern for enterprise agents that call internal APIs, and it survives prompt injection by design.
