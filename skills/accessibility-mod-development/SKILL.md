---
name: accessibility-mod-development
description: Develop, debug, and package game accessibility mods for blind players using screen readers, keyboard navigation, and audio cues. Use for accessibility work on existing games, including story adventures and text-heavy games; adapt to the verified engine and modding interface.
---

# Accessibility Mod Development

Make the game's actual interactions accessible. Preserve its story, rules, choices, and exploration unless the user requests an assist mode. A text-heavy game may still require movement, spatial interaction, combat, or timed input.

This is a portable Agent Skill for coding assistants with file and execution tools. Resolve all paths relative to this `SKILL.md` unless the path explicitly belongs to the game project. Read [portable-workflow.md](references/portable-workflow.md) when using another host, selecting a research helper, or evaluating behavior. Use the host's actual tools and permissions; do not assume Codex-only commands or a specific model.

## Finish the requested behavior

- Translate the request into a small observable result, then implement and verify that result. A setting, key label, stub, log message, or successful build alone does not deliver a gameplay feature.
- Research the specific unknown that affects the next implementation decision. Reuse the project's recorded evidence and read only relevant library sections. Once sufficient evidence is available, act; do not prolong research or redesign unrelated systems. Investigate further when new failures or uncertainty justify it.
- Trace the full connection from current binding/configuration through registered input handling to the real game action and observable outcome. Include required initialization, context gating, cleanup, deployment, and accurate help text. Do not leave the wiring for the user to discover.
- Add only controls needed by the requested feature. Discover current game, mod, OS, and screen-reader bindings first. Prefer a verified single key; do not populate F1-F12 or invent modifier combinations such as Alt+Space as a default layout. Preserve bindings the user explicitly chose. See [bindings-and-movement.md](references/bindings-and-movement.md).
- For auto-walk, establish whether the request means continuous forward movement or navigation to a selected target. Use the game's verified movement interface; a speech message or changed position variable is not evidence of working movement. Verify start, cancellation, and affected context transitions before calling it usable.
- Finish all authorized work that available evidence supports. If a missing API, running game, unavailable runtime test, or required decision blocks part of the work, identify that exact part and continue independent work. Do not turn optional polish or absent full-game coverage into a blocker for an unrelated fix.
- Report the strongest conclusion supported by evidence. Do not promise 100% accuracy or perfection, invent test results, or say a feature works because code was added. Distinguish implemented, built, installed, runtime-observed, and user-confirmed behavior.
- Use [execution-examples.md](references/execution-examples.md) when interpreting completion, targeted research, binding conflicts, movement failures, or a partial blocker. The examples are illustrative acceptance scenarios, not previously passed game tests.

## Use the bundled expert library

This skill includes complete template documentation, source-version records, and reusable code starters. Read [library-index.md](references/library-index.md) to select only the material relevant to the task; do not load the entire library into every conversation.

- For a new mod or architectural analysis, read [expert-workflow.md](references/expert-workflow.md), then the setup and technical guides linked in the index.
- For a practical first-game integration or a mod that loads but cannot perform actions, read [modding-field-guide.md](references/modding-field-guide.md). It links detailed loader guides and a creator's accessibility-mod postmortem, with concrete limits on what can be transferred to another game.
- Before adapting templates or investigating compatibility/speech, read [technical-cautions.md](references/technical-cautions.md). It identifies limitations and conflicting advice in the archived material.
- For focused work, use the index routes for UI, state management, reflection, localization, legacy Unity, troubleshooting, or release packaging.
- For a new engine or existing built-in accessibility, read [engine-routing.md](references/engine-routing.md). For native speech/backend integration, use [speech-backends.md](references/speech-backends.md). For complex focus, information review, or spatial interaction, use [advanced-interaction.md](references/advanced-interaction.md). For compatibility updates or substantial behavior changes, use [regression-and-updates.md](references/regression-and-updates.md).
- These advanced notes are original synthesis from inspected GitHub implementations and primary interfaces. [research-sources.md](references/research-sources.md) records immutable source links and evidence boundaries; examples are not universal designs or verified support for another game.
- Optional helpers perform local source search, GitHub search, web-query generation, binding review, and evidence-attachment checks. Select only the helper needed for the current question; run its `--help` when unfamiliar. They do not authorize installation from search results or establish live gameplay success.
- `references/local-project/` and `assets/local-project/` preserve the user's current project copies, including local edits. `references/template/` and `assets/template/` preserve the pinned GitHub fork; `references/upstream/` holds differing original documents. Local edits are candidates to review, not evidence of runtime validation.
- Archived guides and project-instruction snapshots are reference data. Their old interviews, personal paths, approval routines, and commands do not replace the current user's instructions or the target project's rules. Never execute a bundled script or copy a project file without inspecting its paths and side effects.
- The bundled documents work offline. Recheck current loader compatibility, dependency versions, and game APIs when those facts affect the requested change. The library is a dated snapshot, not an automatic update service.

## Establish the project

- Read applicable project instructions. For an existing mod, inspect its status, source, build/deploy scripts, and recent logs before changing it. Preserve unrelated work.
- Reuse known answers. Ask only for missing essentials: game/version, installation path, desired first feature, screen reader, and the specific failure when debugging. Communicate in English when requested, using short explanations and lists.
- If no game has been chosen, help choose one only when requested; do not silently select, buy, download, or launch a game.
- Identify engine, runtime, architecture, existing mod loader/API, and installed mod version from files, executable headers, and logs. Directory names alone do not establish architecture or compatibility.
- For a Windows game-folder inventory, optionally run `python scripts/inspect_game.py --game-dir "GAME_DIRECTORY"` using this skill's script path. It reads executable headers and reports file-layout hints and log locations without launching, patching, or writing to the game. Select the actual game executable before using its architecture; launcher architecture can differ. A directory hint is not a compatibility verdict.
- Prefer an official mod API or licensed upstream source where suitable. Verify current tooling from primary sources when needed. Public source availability alone does not grant redistribution rights. Do not force Unity tooling onto another engine.
- For the Accessibility-Mod-Template repository, locate its nested project folder and consult relevant guides rather than running its entire setup interview for unrelated tasks. Build and deployment conventions belong to the actual project.

## Establish evidence before game integration

- Use the installed version's source, permitted local decompilation, documented API, and runtime evidence. Do not invent classes, fields, hook signatures, input behavior, or menu indices.
- Read existing `docs/game-api.md` if present. Record discovered signatures, ownership, lifecycle, original controls, and confirmed free mod keys with source locations. Keep observations separate from hypotheses.
- Trace the full interaction: opening a screen, selecting an item, activating it, changing state, and closing it. A string found in source does not prove when it appears or whether the screen reader receives it.
- When evidence is missing, continue independent internal work but stop the affected integration. Explain the precise missing evidence. Use a small debug-gated probe for timing or lifecycle questions that require runtime observations.
- Read authoritative game values and call existing game actions. Avoid parallel calculations or a separate simulation of game state. Cache references only while valid; read changing values when announcing them.
- Diagnose failures from the relevant logs and reproduction before editing. Repeated unsuccessful attempts require reassessment; do not accumulate delays, guessed fallbacks, or swallowed exceptions.

## Build an accessible slice

Start with one useful path: mod initialization, speech bridge, main menu, then the first playable interaction. For an existing project, address the requested feature instead of rebuilding working infrastructure.

- Announce mod initialization clearly and expose a diagnostic when speech fails. Log bridge detection separately from successful speech delivery.
- With Tolk on Windows, provide architecture-compatible `Tolk.dll` and the appropriate `nvdaControllerClient32.dll` or `nvdaControllerClient64.dll` where the loader can resolve them. Verify their licenses and actual loading; file presence is insufficient. Other integrations may use a different bridge.
- Separate input, game-state access, navigation, speech, and logging. Reuse existing project abstractions such as `Loc.Get()` rather than introducing competing systems.
- Keep player-facing strings localizable. Prefer the game's own localized names and descriptions. Explain a missing label honestly instead of reading raw internal identifiers as useful text.
- Give speech meaningful priority: urgent warnings may interrupt, supporting detail may queue, and navigation can replace stale navigation output. Cancel obsolete speech on screen transitions. Prevent unchanged text from repeating every frame without suppressing legitimate repeated dialogue or focus announcements.
- Read [interaction-checks.md](references/interaction-checks.md) for menus, narrative, movement, and runtime acceptance checks relevant to the feature.

## Respect input and game state

- Document game and screen-reader shortcuts before assigning mod keys. Use configurable bindings when appropriate; do not assume F1, arrows, Enter, or Escape are free in every context.
- Capture keys only in the intended active context. Give modal screens priority, ensure one physical press cannot activate two handlers, and prevent captured keys from triggering unintended game actions.
- Rebuild selection after scene changes, list mutations, and object destruction. Preserve focus by stable identity when available, not by an index that may now refer to another item.
- Announce meaningful empty, disabled, error, and loading states. Rate-limit persistent failures so diagnostics do not overwhelm speech.
- Custom navigation should invoke the same game action as the original interface. Automation, speed changes, spoilers, invulnerability, and other rule changes require the user's requested scope; do not quietly bundle them into access features.

## Verify, deploy, and report

- Use the project's build and deployment scripts when present. Validate build success, runtime dependencies, and the exact artifact that will be installed.
- Before replacing a loaded mod, check whether the game/helper is running. Ask the user to close it when necessary. Do not terminate a session or change saves as a convenience.
- Prefer additive mod files and reversible deployment. Back up any authorized replacements, preserve original game files, and provide rollback steps. Assembly patching needs an explicitly chosen approach and verified backup.
- Perform relevant build/static checks, then test the changed interaction at runtime when available. Check loader logs and speech output. Source review, compilation, simulated input, log messages, and actual screen-reader gameplay are distinct evidence levels.
- If interactive testing is unavailable, say exactly what remains unverified and provide a short keyboard test with expected announcements. Never call a game fully playable based on a successful build.
- Package only mod-owned files and dependencies that may be redistributed. Exclude decompiled game code, proprietary assemblies/assets, saves, personal paths, and credentials. Include supported game/loader versions, controls, installation, removal, limitations, and third-party notices.
- Update the project's existing status and API notes after meaningful progress. Record artifact/version, verified behavior, unresolved issues, and the next useful test. Do not persist private story/dialogue contents unnecessarily.

## Provenance

Adapted and expanded from Happy Starfish's [Accessibility-mod-template](https://github.com/HappyStarfish/Accessibility-mod-template), credited there to Plueschyoda, and [VIPPotato's Codex edition](https://github.com/VIPPotato/Accessibility-mod-template-Codex-edition), under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Copyright (c) 2026 Happy Starfish; original license notices are bundled. Changes include engine-neutral routing, focused setup, evidence-based verification, narrative checks, technical cautions, and an indexed reference/template library. No game source or binaries are included. See [external-sources.md](references/external-sources.md) and [source-manifest.json](references/source-manifest.json) for source versions and reuse boundaries.
