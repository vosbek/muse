# VS Code Storage/Memory Map: What's Local, What's Cloud

**Source:** Companion graphic to the r/ClaudeAI "Claude storage/memory map" post (u/BenSimonDev, Oct 4 2026) — same dark green/amber visual language, applied to VS Code. Facts verified via web research, Oct 2026.

![VS Code storage/memory map](vscode-storage-memory-map.png)

## Thesis

VS Code is overwhelmingly local — your files, settings, extensions, terminals, and history never leave the machine — but it phones home in four specific ways: Settings Sync, the extension Marketplace, telemetry (on by default), and Remote Tunnels. Know the four and you know your exposure.

## The map (text version)

**On your disk:**
- settings.json, keybindings.json, snippets — local User folder; workspace settings in the project's `.vscode/`
- Named profiles — local user-data `profiles/` directory
- Secrets (SecretStorage) — OS-keychain encrypted, **never synced, full stop**
- Sign-in tokens — Microsoft/GitHub OAuth cached locally (`~/.vscode/cli`)
- Extension host — extensions run in a dedicated local Node.js process
- Your files, local history/Timeline snapshots, workspace trust DB, integrated terminal PTYs — all machine-local

**Their servers:**
- Settings Sync → Microsoft sync service (settings, shortcuts, snippets, tasks, UI state, extensions, profiles)
- Extension Marketplace — downloads + auto-updates
- Telemetry — **on by default**, usage data → Microsoft
- Experiments (A/B) service — disabled when telemetry is off
- Update checks — product + extension updates from Microsoft
- Codespaces — full dev environments on GitHub's cloud VMs
- Remote Tunnels — relayed through Microsoft's Dev Tunnels service

**Either (a setting decides):** Remote SSH / WSL windows — the extension host moves to the remote machine.

## Notable facts

- Telemetry levels: `all` (default) / `error` / `crash` / `off` — set `telemetry.telemetryLevel` to `off`. Individual extensions may collect their own telemetry outside this setting.
- Settings Sync is encrypted in transit and at rest, but Microsoft publishes no zero-knowledge claim — treat it as readable-by-Microsoft.
- The one hard privacy boundary: SecretStorage secrets never sync at all.

## Local-deploy takeaways

- For a fully local VS Code: telemetry off, skip Settings Sync (or accept Microsoft-held settings), prefer SSH/WSL remotes you control over Tunnels/Codespaces.
- Secrets in SecretStorage are the only thing guaranteed never to leave — keep tokens there, not in settings files that might sync.
