# Game Accessibility Mod Skill

This project, maintained by Swarup Baral, provides a portable skill with researched references, practical helpers, and a Windows installer.

It provides reusable guidance to help an AI coding assistant build accessibility mods for blind players, focusing on screen-reader speech, simple keyboard controls, story text, movement, and honest testing.

You describe the change you want. The assistant should inspect the real game, implement the change, and explain what it actually verified. It should not invent game APIs, assign a row of unrelated shortcuts, or call a feature finished because a settings switch exists.

This is an instruction and helper package, not a game mod or an AI model. It cannot guarantee that an assistant will follow every instruction or eliminate hallucinations.

**New here? Download the full release ZIP, extract it, run `install.bat`, and restart your assistant.** The steps below explain each part. You do not need Git or terminal commands for the normal Windows installation.

## Before you start

- Have a supported local AI coding assistant installed and set up. This package does not install the assistant or sign you in.
- For automatic installation, use Windows with Windows PowerShell available. Administrator access is not required.
- Python is not required for installation or reading the skill. Python 3.9 or newer is needed only for the optional Python helpers.
- You need internet access to download the package. Bundled guides and local source search can be used offline; public GitHub/web research needs a network connection.
- A particular mod may also need a game-specific loader, SDK, or development tools. The assistant should identify those for the actual game. This installer does not install them.

## Download the right ZIP

Open the [latest release and downloads](https://github.com/swarup-developer/game-accessibility-mod-skill/releases/latest). You do not need a GitHub account to download this public package. Expand **Assets** if it is collapsed.

- **`game-accessibility-mod-skill-VERSION.zip`** is the recommended full download. It contains `install.bat`, `uninstall.bat`, the README, skill, guides, and helpers. `VERSION` represents the release number; it is not text you need to type.
- **`accessibility-mod-development-VERSION.skill.zip`** contains only the skill folder and its license. It is for manual installation or compatible skill importers. It does not contain `install.bat`.
- **`SHA256SUMS.txt`** contains checksums for checking the downloads. This is optional for normal installation.
- GitHub also shows automatically generated **Source code** downloads. To follow the simple steps below, choose the full named release ZIP above instead.

Save the full ZIP somewhere easy to find, such as Downloads. Installing this skill will not make a game accessible by itself; it gives the assistant a workflow for developing and testing a game-specific mod.

## Install on Windows

1. Open the folder where you saved the full release ZIP.
2. Select the ZIP and open its context menu by right-clicking or pressing **Shift+F10**. Choose **Extract All**. You can also use File Explorer's **Extract all** command if shown there.
3. Choose a destination folder and select **Extract**. Extract the entire package, not just the batch file.
4. Open the extracted folder. If another package folder is inside it, open that too, until `README.md`, `install.bat`, `uninstall.bat`, and the `skills` folder appear together. **Do not run the installer from inside the ZIP preview.**
5. Open **`install.bat`**. If filename extensions are hidden, look for the file whose type is **Windows Batch File**.
6. The text window offers: **1 All, 2 Codex, 3 Claude Code, 4 Gemini CLI, 5 Antigravity, 6 Freebuff CLI**. Type the number and press Enter, or press Enter without a number for All.
7. Read the result. Successful copying prints **Installed:** and the destination. If a previous copy existed, its backup location is also printed. If an error appears, do not assume installation succeeded; keep the message for troubleshooting.
8. When prompted, press a key to close the installer window. Close and reopen your assistant, then ask: **Use the accessibility-mod-development skill. Tell me which SKILL.md file you loaded, then help me make my game accessible.**

The installer uses Windows PowerShell. You do not need Python just to install or read the skill. Python 3.9 or newer is needed only for the optional research helpers.

The installer copies the skill to your own account. It does not install an AI app, a mod loader, or a game. It does not change game files or the assistant's permissions. Existing copies are moved to a dated backup before replacement. The final installer message tells you where that backup is.

Choosing All places the skill in the listed local discovery locations even if some assistants are not installed yet. It does not install those applications. The installer verifies its file inventory before copying; do not edit that inventory to force a damaged package to install.

## Where it installs

- Codex, Gemini CLI, and Freebuff CLI: `~/.agents/skills/accessibility-mod-development`.
- Claude Code: `~/.claude/skills/accessibility-mod-development`.
- Antigravity: `~/.gemini/config/skills/accessibility-mod-development`.

`~` means your home folder, usually `C:\Users\YourName` on Windows. Each installed folder contains `SKILL.md` directly inside it. Use the actual destination printed by the installer rather than guessing your account folder name.

**The `.agents` copy is shared by Codex, Gemini CLI, and Freebuff CLI.** Updating it affects all three; removing it for one also removes that shared copy from the other two's discovery locations. Another copy installed elsewhere may still be discovered.

## Supported assistants

The same `SKILL.md` and reference files are used for Codex, Claude Code, Gemini CLI, Google Antigravity, and Freebuff CLI. Their documented discovery locations differ. See [compatibility and sources](docs/compatibility.md).

Installation and file integrity are tested in temporary folders. Live discovery and model behavior have not been tested in every listed assistant. Cloud/web sessions may not see skills installed on your computer. This package does not claim to work in every product that happens to use Claude or Gemini.

In Claude Code, you can use `/accessibility-mod-development`. In Codex, mention `$accessibility-mod-development`. In Gemini CLI, check `/skills list` and use `/skills reload` if needed. For other tools, mention the full skill name and ask which skill file was loaded.

Follow any workspace-trust or activation prompt required by your assistant. Local installation does not upload the skill to an account, regular chatbot, or remote/cloud session. A cloud product may need its own import process or may not support this workflow. If native discovery is unavailable but file access is supported, ask the assistant to read the installed `SKILL.md` and its relevant references directly; that is a manual fallback, not a claim of native compatibility.

## Try a small task first

Tell the assistant the game name, installation folder, your screen reader, and one thing you want to improve. For example:

Also include the game version/storefront if known, preferred controls, and any important limits such as keeping original game files untouched. Start with one useful interaction rather than asking for an entire game at once. You may need to run the game and report what the screen reader says.

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
.\install.bat -Agent All -Scope Project -ProjectPath "D:\My Mod Project"
```

This creates skill folders in that project. It does not overwrite `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`. You can also copy the skill folder manually to a documented discovery location.

Replace the example path with an existing project folder. You may replace All with Codex, Claude, Gemini, Antigravity, or Freebuff. Start the assistant in the intended project and follow its workspace-trust requirements.

On macOS or Linux, the Windows installer does not run. Copy `skills/accessibility-mod-development` to the appropriate personal or project skill folder listed in the compatibility guide. The Python research helpers are portable; game inspection and bundled mod templates have their own platform limits.

For manual installation, copy the **entire** `accessibility-mod-development` folder, including references, assets, scripts, and license. Do not copy only `SKILL.md`. If using the skill-only ZIP, extract it first and avoid adding an extra nesting level.

## Update or remove

Run the new release's installer to update. Your previous copy is kept as a backup. Do not delete a backup containing edits you still need.

To remove this package's installed copy, open **uninstall.bat** and choose the same assistant. Removal moves the installed copy into a backup instead of deleting it. It refuses to remove an unmarked folder that it cannot identify as this package's installation. Project installs must be removed with the same `-Scope Project -ProjectPath` arguments.

For example, remove a project installation with:

```powershell
.\uninstall.bat -Agent All -Scope Project -ProjectPath "D:\My Mod Project"
```

To recover a previous copy, use the printed backup location. Close the assistant first and preserve the current folder separately before restoring the complete backup folder. Ask for help with the actual paths if unsure; do not delete folders by guesswork.

Removing this skill does not uninstall any game mod developed with it. Each mod needs its own removal instructions.

## If the skill does not appear

Restart the assistant and check the destination printed by the installer. Make sure `SKILL.md` is directly inside `accessibility-mod-development`, not inside an extra nested copy. Check whether your app/version supports local Agent Skills and whether workspace trust is required. Tell the assistant the full path to `SKILL.md` if automatic discovery is unavailable.

If a helper fails, give the assistant its error message. Missing authentication, unavailable network access, and no search results are different conditions. None is evidence that a game feature is impossible.

Other common problems:

- **No install.bat:** check that you downloaded the full named release ZIP and opened the inner folder containing the README. The skill-only ZIP does not include the installer.
- **Missing package files:** extract the entire ZIP and keep its folder structure. Do not move only the batch file elsewhere.
- **Package verification failed:** keep the message and extract a fresh release into a new folder. Do not bypass the inventory check.
- **Windows or an organisation blocks the installer:** do not disable security protections to force it to run. Use manual installation or ask for help with the exact message.
- **The assistant ignores an installed skill:** explicitly request it and ask which file was loaded. Installation does not prove activation or compliance.
- **A Python helper fails:** the skill installation may still be correct. Helpers are optional and need Python 3.9+. Report the exact error instead of downloading unrelated scripts.
- **A compiled mod does nothing:** verify the installed artifact and loader result, then reproduce the action in the running game. A successful build or an "enabled" announcement is not proof the action works.

## Sharing and contributing

Please report the assistant/version, requested behavior, expected result, observed result, and a small relevant log excerpt. Leave out passwords, access tokens, private game source, saves, and unnecessary story spoilers. A successful build is useful information, but it is not proof of accessible gameplay.

Contributions are welcome: clearer instructions, corrected sources, useful examples, compatibility fixes, and focused helper improvements all help. Use [GitHub Issues](https://github.com/swarup-developer/game-accessibility-mod-skill/issues) for suggestions/problems or open a pull request with a proposed change. Include your operating system and relevant versions. Do not upload decompiled game source or proprietary assemblies, and preserve the original credits and licenses.

The package includes credited material from Accessibility-mod-template. Documentation and bundled template material use CC BY 4.0; new utility/installer code uses MIT. See [LICENSE](LICENSE) and [third-party notices](THIRD_PARTY_NOTICES.md).

For release commands and the GitHub publication helper, see [maintaining the package](docs/maintaining.md).

## Disclaimer and limitations

- **AI can still make mistakes.** The skill encourages evidence-based work but cannot eliminate hallucinations, force an assistant to follow instructions, or guarantee perfect code, safe bindings, or working movement.
- **No universal game support is promised.** Each game, version, engine, loader, and input system needs investigation. A method from another mod is not evidence of a matching API in your game.
- **Installing the skill does not make a game accessible.** A game-specific mod still needs development and real interaction testing. No complete-game accessibility claim is made for a particular title by this package.
- **Verification has different levels.** Compilation, file hashes, source inspection, runtime logs, audible screen-reader output, and completing a gameplay path establish different things. Helpers and package checks cannot stand in for all of them.
- **Compatibility is conditional.** Discovery paths are documented and installer/helper checks have passed, but live loading and model behavior have not been tested in every listed assistant/version. Local installations may be unavailable in cloud sessions.
- **Platform limits remain.** The installer is Windows-only. The common skill format is portable, but the executable inspector, speech backends, templates, and individual games have their own platform/runtime requirements.
- **No AI service or game is supplied.** The package does not include models, usage credits, subscriptions, assistant accounts, games, mod loaders, or screen-reader binaries. Those have their own requirements and terms.
- **Research can become outdated.** Bundled references are dated; blogs describe particular experiences. Verify findings against the actual installed game before applying them.
- **Preserve game files and saves.** Review relevant changes and keep suitable backups. Check the game's modding policy and any online/anti-cheat restrictions; this package is not permission to bypass them or redistribute game code.
- **You remain in control.** Review proposed changes and what was actually tested. Missing runtime or speech evidence should remain explicitly unverified, rather than being described as complete.

## Credits

**Original project credits:** Thank you to **Happy Starfish / Plueschyoda** and the contributors behind the [Accessibility Mod Template](https://github.com/HappyStarfish/Accessibility-mod-template), and to **VIPPotato** for the [Codex edition](https://github.com/VIPPotato/Accessibility-mod-template-Codex-edition). Their work provided this project's foundation. The original documents, attribution, and license notices remain included.
