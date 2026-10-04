# Talk Notes: "Stop Fine-Tuning to Fix Retrieval Problems" — Anant Srivastava

**Video:** [Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava](https://www.youtube.com/watch?v=qflLT3SoVbw) · AI Engineer channel · Oct 3, 2026 · 20:11 · Recorded at AI Engineer World's Fair 2026

## Thesis

Most teams never deliberately decide where knowledge lives — prompt, memory/retrieval, or model weights — so six months of normal product work decides it for them by accident. These aren't a ladder to climb but three tools for three jobs, and you need a deliberate harness for circulating knowledge between them; fine-tuning should be reserved for knowledge that has stopped changing.

## Key points

- **Prompt's job = behavior**: small, stable, editable knowledge about how to act (e.g., support-agent tone, "offer human escalation after three failures"). Wrong job: storing facts — too many instructions dilute, and you pay context cost.
- **Memory's job = knowledge that is current, large, and citable** — covers both agent memory and external/RAG memory like refund policies. Changes faster than you can fine-tune; can't fit in a prompt.
- **Wrong job for memory: behavior/reasoning** — if the model can't reason over retrieved docs, more context doesn't help; you need the right model.
- **Access control belongs in memory** — per-user/per-repo data must be retrievable with permission checks, never baked into weights.
- **Code-assistant example**: don't fine-tune on code (changes too fast); use code-aware chunking, filtering, and denormalized metadata (repo, user, commit) to retrieve exact chunks.
- **Weights = what has stopped changing**; fine-tuning needs a strong reason — retraining locks in a boundary that may still be moving.
- **Classic fine-tuning mistake**: a team fine-tuned on documentation when it was actually a retrieval problem — stale docs got baked into weights.
- **When fine-tuning works**: ambiguous judgment tasks (content moderation, claims processing) — bootstrap with a frontier model + human corrections, wait until human override rates flatline, fine-tune the stable "center," keep humans on the contested edge.
- **Medical coding example (ICD-10, 70k codes; IMO Health / Mount Sinai)**: fine-tune the reflex (format understanding), not the codes themselves.
- **Fine-tuning decision = capability vs. cost** — fine-tune a small model and run volume cheap (e.g., 10M requests/day).
- **Decision table**: prompt = behavior; memory = what to know (facts); weights = how to act (reflexes).
- **Circulating architecture**: prompt → signals → durable knowledge in memory → memory pulled back into prompt on new sessions; over time, patterns move memory → weights via fine-tuning and retrieval needs shrink — the loop makes the agent better.

## Notable quotes & data

- "The model is the easy part. What you build around the model... is the key architecture."
- ICD-10 has 70,000 codes — fine-tune the format reflex, not the codes.
- Human override rates flatlining = the signal that knowledge is stable enough to fine-tune.

## Tokenomics / efficiency angle

- Stuffing facts into the prompt wastes context tokens ("you pay the cost for it") and dilutes instruction-following.
- Fine-tune small models to run high volume cheaply when it's a cost problem, not a capability problem.
- Circulating memory → weights reduces retrieval needs over time.

## Local-deploy takeaways

- **Keep a standing decision table for every skill/pipeline**: behavior → prompt/skills, facts → local RAG/retrieval, reflexes → fine-tuned small local model. Review it whenever a new knowledge source enters the system.
- **The circulation loop is the local strategy**: use local retrieval (sqlite/LanceDB) for fast-changing knowledge, and only bake the stable center into a locally fine-tuned small model — exactly the Ollama + local RAG split Matt already runs.
- **Access control is the hard constraint for local-first**: per-user/per-repo data must stay retrievable with permission checks, never baked into weights — weights can't do ACLs.
