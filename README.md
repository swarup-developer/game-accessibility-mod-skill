# Game Accessibility Mod Skill

A reusable guide that helps an AI coding assistant build accessibility mods for blind players. It focuses on screen-reader speech, simple keyboard controls, story text, movement, and honest testing.

You describe the change you want. The assistant should inspect the real game, implement the change, and explain what it actually verified. It should not invent game APIs, assign a row of unrelated shortcuts, or call a feature finished because a settings switch exists.

This is an instruction and helper package, not a game mod or an AI model. It cannot guarantee that an assistant will follow every instruction or eliminate hallucinations.

## Install on Windows

1. Download the full ZIP from this repository's Releases page.
2. Right-click the ZIP and choose **Extract All**. Open the extracted folder. Do not run the installer inside the ZIP preview.
3. Open **install.bat**. You do not need administrator access.
4. Choose your assistant, or press Enter to install for all supported local assistants.
5. Close and reopen your assistant. Ask: **Use the accessibility-mod-development skill to help me make my game accessible.**

The installer uses Windows PowerShell. You do not need Python just to install or read the skill. Python 3.9 or newer is needed only for the optional research helpers.

The installer copies the skill to your own account. It does not install an AI app, a mod loader, or a game. It does not change game files or the assistant's permissions. Existing copies are moved to a dated backup before replacement. The final installer message tells you where that backup is.

## Supported assistants

The same `SKILL.md` and reference files are used for Codex, Claude Code, Gemini CLI, Google Antigravity, and Freebuff CLI. Their documented discovery locations differ. See [compatibility and sources](docs/compatibility.md).

Installation and file integrity are tested in temporary folders. Live discovery and model behavior have not been tested in every listed assistant. Cloud/web sessions may not see skills installed on your computer. This package does not claim to work in every product that happens to use Claude or Gemini.

In Claude Code, you can use `/accessibility-mod-development`. In Codex, mention `$accessibility-mod-development`. In Gemini CLI, check `/skills list` and use `/skills reload` if needed. For other tools, mention the full skill name and ask which skill file was loaded.

## Try a small task first

Tell the assistant the game name, installation folder, your screen reader, and one thing you want to improve. For example:

> Use accessibility-mod-development. Make the main menu readable with NVDA. Inspect the existing controls first, use simple keys, and tell me what you tested.

Or:

> Add a toggle for continuous forward walking. First verify how this game handles movement. Do not choose shortcuts until you have checked the current bindings. Test stopping as well as starting.

The assistant should distinguish a forward toggle from walking to a selected target. It should not silently add pathfinding, teleportation, combat automation, or extra keys.

## What is included

- The skill, indexed reference guides, original template documents, source records, and code starters.
- A read-only game-folder inspector.
- A local source search helper with filenames and line numbers.
- A read-only GitHub search helper for repositories, issues, or code.
- A web-query helper that creates search links. It does not pretend that links are verified search results.
- A binding checker for conflicting controls, unsupported verification claims, and unrequested modifier shortcuts.
- A verification-record checker that checks evidence files and hashes. It cannot certify that a human heard speech or completed gameplay.
- Installer, removal, package validation, and release-building scripts. Development test fixtures are kept outside the public package.

See [research helpers](docs/research-helpers.md) for examples. The assistant can run each helper with `--help`. Searches do not install or execute code from their results.

For the actual game-modding process, read the [practical modding guide](skills/accessibility-mod-development/references/modding-field-guide.md). It connects loader tutorials with a detailed accessibility-mod postmortem and explains why reading a game is different from making its actions usable.

## Install for one game project

For a project-specific installation, open a terminal in this extracted folder and run:

```powershell
.\install.ps1 -Agent All -Scope Project -ProjectPath "D:\My Mod Project"
```

This creates skill folders in that project. It does not overwrite `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`. You can also copy the skill folder manually to a documented discovery location.

On macOS or Linux, the Windows installer does not run. Copy `skills/accessibility-mod-development` to the appropriate personal or project skill folder listed in the compatibility guide. The Python research helpers are portable; game inspection and bundled mod templates have their own platform limits.

## Update or remove

Run the new release's installer to update. Your previous copy is kept as a backup. Do not delete a backup containing edits you still need.

To remove this package's installed copy, open **uninstall.bat** and choose the same assistant. Removal moves the installed copy into a backup instead of deleting it. It refuses to remove an unmarked folder that it cannot identify as this package's installation. Project installs must be removed with the same `-Scope Project -ProjectPath` arguments.

## If the skill does not appear

Restart the assistant and check the destination printed by the installer. Make sure `SKILL.md` is directly inside `accessibility-mod-development`, not inside an extra nested copy. Check whether your app/version supports local Agent Skills and whether workspace trust is required. Tell the assistant the full path to `SKILL.md` if automatic discovery is unavailable.

If a helper fails, give the assistant its error message. Missing authentication, unavailable network access, and no search results are different conditions. None is evidence that a game feature is impossible.

## Sharing and contributing

Please report the assistant/version, requested behavior, expected result, observed result, and a small relevant log excerpt. Leave out passwords, access tokens, private game source, saves, and unnecessary story spoilers. A successful build is useful information, but it is not proof of accessible gameplay.

The package includes credited material from Accessibility-mod-template. Documentation and bundled template material use CC BY 4.0; new utility/installer code uses MIT. See [LICENSE](LICENSE) and [third-party notices](THIRD_PARTY_NOTICES.md).

For release commands and the GitHub publication helper, see [maintaining the package](docs/maintaining.md).
