# Talk Notes: "I Built a Personal AI Agent on a Raspberry Pi" — Jeremy Adams, Neo4j

**Video:** [I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j](https://www.youtube.com/watch?v=oUZEt4EiPbk) · AI Engineer channel · Oct 3, 2026 · 20:10 · Recorded at AI Engineer World's Fair 2026

## Thesis

A useful, private personal AI agent doesn't need a laptop or a Mac Mini — it can run on a cheap old Raspberry Pi 4B using NanoClaw (a compact, hackable agent runtime), WhatsApp as the interface, Claude as the cloud brain, and a Neo4j knowledge-graph memory with a POLE schema — built for hackability and understanding over feature-completeness.

## Key points

- **Hardware**: Raspberry Pi 4B (not the latest model), previously ran a 32-bit OS; originally used to measure dish weight in the sink — "Will it claw? It claws real good."
- **Wanted no laptop agent** — wanted it open, hackable, understood more than feature-complete (sysadmin/devops background).
- **Rejected a Mac Mini with pre-installed OpenClaw off Craigslist** — "pre-installed... ick."
- **NanoClaw** (github.com/qwibitai/nanoclaw): ~15 source files, compact, Docker-based, built on the Claude Agent SDK; encourages modification with skills.
- **Architecture**: WhatsApp (iPhone/MacBook) → NanoClaw on the Pi → Claude cloud API; no LLM inference on the Pi — big brain over a wire, peripherals and local graph on the device.
- **Memory graph**: Neo4j (Aura cloud + local Docker) with the POLE schema (Person, Object, Location, Event + Organization) — borrowed from a European police investigation schema / cop-show string diagrams.
- **Querying over MCP**: the agent connects to Neo4j via an MCP server; "tell me what movies Tom Hanks acted in" → the agent wrote Cypher via MCP and answered.
- **Voice-to-text**: a physical button wired to the Pi's GPIO pins records voice notes; used to record expo booth pitches.
- **Offline mode**: local Neo4j captures booth voice notes when conference Wi-Fi is bad; notes are uploaded and enriched in the cloud later.
- **Demo data**: expo booths at AI Engineer World's Fair modeled with booth numbers/names; cloud enrichment produced theme nodes — Buildkite and LangChain both connected to "Evaluation and observability" → novel knowledge generated.
- **Upgraded to the Neo4j Agent Memory service**: all historical WhatsApp messages distilled into memories — people, locations, concepts — accessible via MCP server.
- **Resources**: Neo4j GraphAcademy free courses; Neo4j booth P3.

## Notable quotes & data

- "I wanted to understand what was happening more than it being feature-complete. Understanding was more important to me."
- "Will it claw? It claws real good."
- NanoClaw = ~15 source files; POLE = Person, Object, Location, Event (+Organization).

## Tokenomics / efficiency angle

- Repurposed old hardware instead of buying a Mac Mini; no local inference cost — cloud brain only for reasoning, local graph for cheap storage/retrieval.
- Offline-first voice notes reduce dependence on conference Wi-Fi.

## Local-deploy takeaways

- **The architecture is Matt's local-first pattern at pocket scale**: cloud reasoning over the wire + local graph memory on-device. Enterprise version: local decision models with local RAG/memory, cloud frontier only for reasoning overflow.
- **POLE schema (Person, Object, Location, Event + Organization) is a ready-made memory ontology** — steal it for the governed memory layer instead of inventing a custom schema.
- **Capture-local, enrich-cloud** is the offline pattern: cheap local writes during capture, expensive enrichment later — directly analogous to batching retrieval/enrichment off the hot path.
