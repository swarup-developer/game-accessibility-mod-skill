# Research helpers

These tools make a few repeated checks predictable. They do not replace game source analysis or playing the changed interaction with a screen reader. Installation does not need Python; using these helpers needs Python 3.9 or newer.

The commands below assume you are in the extracted package folder. An AI using an installed skill should resolve `scripts` relative to that skill's `SKILL.md`, not the game project.

## Inspect a game folder

```powershell
python skills/accessibility-mod-development/scripts/inspect_game.py --game-dir "D:\Games\My Game"
```

Reads root executable headers and selected folder names. Reports architecture evidence, layout hints, and loader-log locations. It does not launch the game, read log contents, or install anything. A launcher's architecture may differ from the game process.

## Search local source

```powershell
python skills/accessibility-mod-development/scripts/search_local.py --root "D:\My Mod Project\decompiled" --query "Move" --glob "*.cs" --limit 30
```

Returns literal, case-insensitive matches with relative filenames and line numbers. It skips binary/unreadable/oversized files and common generated folders. No local content is uploaded. A matching method name does not prove that method controls the player.

## Search GitHub

```powershell
python skills/accessibility-mod-development/scripts/search_github.py --kind repositories --query "accessibility mod screen reader" --limit 10
python skills/accessibility-mod-development/scripts/search_github.py --kind issues --repo Unity-Technologies/InputSystem --query "rebinding focus"
```

This sends the query to GitHub's API. Keep private code, logs, names, and secrets out of queries. Repository/issue search may work without signing in; code search normally needs authentication. The script optionally uses `GH_TOKEN` or `GITHUB_TOKEN` from the environment. It does not print or save those values. It does not use a CLI's stored login automatically, change repositories, or download/run code.

Missing authentication, rate limits, and zero matches are reported distinctly. Prefer a connected GitHub tool when your assistant already has one; this script is a portable alternative.

## Build web searches

```powershell
python skills/accessibility-mod-development/scripts/search_web.py --query "My Game accessibility movement" --mode primary
python skills/accessibility-mod-development/scripts/search_web.py --query "game mod speech queue" --mode blogs
```

Creates relevant search links without fetching results. Add `--open` only if you want to open them in your browser. The assistant must then read and verify actual sources; generated URLs are not findings.

## Review proposed bindings

Copy `assets/bindings.example.json` from inside the skill and fill it with the actual inspected actions, keys, contexts, and evidence. Leave unknown keys unassigned.

```powershell
python skills/accessibility-mod-development/scripts/check_bindings.py "D:\My Mod Project\bindings.json"
```

Flags declared overlaps, unrequested modifier shortcuts, known system combinations, missing evidence for a verified label, and unrequested allocation of all F1-F12 keys. It never chooses a key. Context names must be consistent; use `*` for a genuinely global binding. It cannot detect controls omitted from your inventory or validate evidence strings on its own.

An exit code of 1 means review is needed; 2 means invalid input or a tool error. A clean inventory means only that these declared checks found no conflicts, not that a game key is safe or functional.

## Check verification attachments

Copy `assets/verification-record.example.json` from inside the skill. Record the requested feature and the stages actually observed. For a passed stage, add evidence entries containing `path`, `description`, and `sha256`. Relative paths are resolved from the record's folder. Leave untested stages pending.

```powershell
python skills/accessibility-mod-development/scripts/check_evidence.py "D:\My Mod Project\verification.json" --require runtime_observed
```

This checks attachment existence and hashes and reports missing required stages. It does not decide whether a log tells the truth, whether NVDA was audible, or whether the game's route was completed. Never use its output as a replacement for those observations.
