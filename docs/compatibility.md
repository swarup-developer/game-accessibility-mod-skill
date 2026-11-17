# Compatibility and evidence

Checked 17 November 2026. The package uses the common Agent Skills format: a directory named `accessibility-mod-development` containing `SKILL.md` and optional resources. It does not depend on a specific model, connector, or automatic approval mode. [Agent Skills specification](https://agentskills.io/specification).

## Local installation paths

- Codex: `.agents/skills` in the project, or `~/.agents/skills` for the user. [Official guide](https://developers.openai.com/codex/skills).
- Claude Code: `.claude/skills` in the project, or `~/.claude/skills` for the user. Account/cloud skills are a separate mechanism. [Official guide](https://code.claude.com/docs/en/skills).
- Gemini CLI: `.gemini/skills` or the `.agents/skills` alias, at project or user scope. This installer uses `.agents/skills` to share the same copy with other compatible agents. Workspace trust and activation consent still apply. [Official guide](https://geminicli.com/docs/cli/skills/).
- Google Antigravity: `.agents/skills` in the project, or `~/.gemini/config/skills` globally. The documentation covers App, CLI, and IDE; it also describes legacy `.agent/skills` compatibility. [Official guide](https://antigravity.google/docs/skills).
- Freebuff CLI: the inspected CLI opts into home skills; its loader searches `.agents/skills` and `.claude/skills` at user and project scope. This installer uses `.agents/skills`. [CLI registry](https://github.com/CodebuffAI/freebuff/blob/46aeca799e36a405bd5f832b8b88f232f30d96fd/cli/src/utils/skill-registry.ts), [SDK loader](https://github.com/CodebuffAI/freebuff/blob/46aeca799e36a405bd5f832b8b88f232f30d96fd/sdk/src/skills/load-skills.ts).

`~` means your account's home folder. On Windows this is usually the folder opened by entering `%USERPROFILE%` in File Explorer. Each path above ends in `accessibility-mod-development/SKILL.md` after installation.

## What has and has not been tested

The installer and package tests use temporary profile/project folders. They verify destination mapping, integrity checks, backups, updates, removal, and preservation of unrelated files. Helper tests verify their own defined behavior.

These checks do not establish that a particular assistant/version discovered or followed the skill. Live model behavior and game testing are separate. Restart your assistant, explicitly request the skill, and verify that it identifies the intended file before relying on it. Remote/cloud sessions cannot be assumed to see local installations. Older product versions may use different paths or lack skills.

The skill's instructions are portable. The `.bat` installer is Windows-only, the game-folder inspector reads Windows PE headers, and the template code is mostly Unity/C# and Windows speech oriented. Other engines/platforms need a verified integration route.

## Design research used in this release

- Anthropic's [Agent Skills article](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) describes modular instructions and loading supporting material only when needed. Applied here through the focused entry point and reference index.
- The [Agent Skills authoring guide](https://agentskills.io/skill-creation/best-practices) advises making fragile procedures precise, surfacing concrete gotchas, and testing through real use. Applied to input conflicts, speech contracts, and completion examples.
- OpenAI's [skill evaluation article](https://developers.openai.com/blog/eval-skills) separates invocation problems from execution problems and recommends testing realistic scenarios. Applied through the evaluation cases and explicitly limited verification claims.
- Vercel's [Next.js evaluation report](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals) found that skill availability did not ensure activation in its particular benchmark. It is not evidence of game-mod performance. Applied here by documenting explicit activation and asking the agent to identify the loaded skill, without overwriting people's project instruction files.

These are design lessons, not measured claims that this package reduces hallucinations by a particular percentage.
