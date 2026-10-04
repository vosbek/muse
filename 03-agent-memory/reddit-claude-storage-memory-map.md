# Updated Claude Storage/Memory Map: What's Local, What's Cloud, What Changes Oct 6

**Source:** r/ClaudeAI post by u/BenSimonDev — https://www.reddit.com/r/ClaudeAI/comments/1wxiysh/updated_claude_storagememory_map_whats_local/ (posted Oct 4, 2026; 143 upvotes, 27 comments)

## Thesis

Anthropic has spent months migrating Claude's storage and memory from local to cloud, and the community is struggling to track what's where. The post consolidates 21 Anthropic help articles, doc pages, and release notes into one visualization mapping what stays local vs. what lives in the cloud — with the next hard milestone on **October 6**: all new Claude app sessions on Pro/Max become cloud-only.

## Key points

- **Oct 6 milestone:** All new sessions in the Claude app on Pro/Max will be cloud-only. No more local option. Sessions already started locally stay local.
- **Claude Code is the local holdout.** CoWork/chat moving cloud-only does not affect Claude Code — it's still the local option.
- **Cloud sessions and local files:** A cloud session can read/write files in connected folders on your computer only while the desktop app is open on that machine and the session was started on desktop. App closed = session keeps running but can't reach local files.
- **Team/Enterprise:** Admins still decide data location for now; no specific date announced. Pro/Max first, then Team and Free "soon after"; Enterprise gets at least 30 days notice.
- **Memory itself is cloud-prioritized.** The push is part of a general Anthropic move toward cloud storage and memory.
- **Session history locality mattered:** local session history let users recover crashed sessions and point a new session at the old one to pick up where they left off — that recovery path disappears with cloud-only sessions.
- **Community sentiment is sour:** top complaints — CoWork became useless for large files (everything must be fully uploaded), loss of local control ("I don't want my files on Anthropic's servers anyway"), sessions "leaning" on each other via shared memory (one user had to turn memory off).
- **The pointed question:** "If they move Claude Code to be cloud-only, what even would be the point of it?"

## Notable quotes & data

- "Data retention, analysis and ownership. The same it has always been." — u/admirantes (11 upvotes) on why Anthropic is pushing cloud.
- "Cowork genuinely became useless when it meant uploading every file fully, can't work on large files now, or have it use local tools." — u/GeggsLegs (19 upvotes)
- Primary reference for the Oct 6 changes: https://support.claude.com/en/articles/15520349/use-claude-cowork-on-web-desktop-and-mobile

## Tokenomics / efficiency angle

- **Cost of the cloud move for users:** full-file uploads for every interaction means more tokens over the wire and more latency — local-file workflows were effectively free and instant.
- **Local-first implication:** as the Claude app goes cloud-only, Claude Code becomes the only Anthropic surface with local context — its local file access is now a differentiator, not just a feature.

## Local-deploy takeaways

- If your workflow depends on local session recovery, archive session transcripts yourself before Oct 6 — the crash-recovery pattern (point new session at old) breaks under cloud-only sessions.
- For large-file work, Claude Code (local) is now the only path that avoids full uploads; treat the Claude app as cloud-terminal, Code as the local workbench.
- Team/Enterprise admins: you still control data location today — document the setting before Anthropic announces the Team migration date.
