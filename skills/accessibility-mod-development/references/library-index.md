# Expert Reference Library

Use this index to read only the guides needed for the current task. Paths are relative to this skill; the library works without the original checkout.

## Start with the curated guidance

- [Practical video-game modding guide](modding-field-guide.md): loader bootstrap, complete feature tracing, patch failures, and detailed creator articles; [reading-list records](modding-reading-list.json).
- [Portable use and research helpers](portable-workflow.md): host-independent operation, relative script paths, bounded research, and honest evaluation claims.
- [Verified bindings and movement](bindings-and-movement.md): discover actual controls, prefer simple keys, complete dispatch/configuration, and validate auto-walk start/stop.
- [Completion and research examples](execution-examples.md): twelve scenarios covering missing wiring, invented movement, shortcut sprawl, stale installation, and honest partial blockers.
- [Engine routing and native accessibility](engine-routing.md): Ren'Py, Godot, Unity Mono/IL2CPP, and selecting the smallest suitable integration.
- [Speech backend contracts](speech-backends.md): capabilities, native bindings, threading, NVDA interfaces, and recovery.
- [Advanced interaction](advanced-interaction.md): changed-context focus speech, optional review buffers, semantic events, map inspection, travel, and input edge cases.
- [Regression checks and updates](regression-and-updates.md): meaningful automated boundaries, runtime journeys, compatibility records, and profiling.
- [Pinned GitHub research](research-sources.md): inspected implementations and primary interfaces from nine repositories, including the official Unity Input System; [machine-readable research manifest](research-manifest.json).
- [Read-only Windows game inspector](../scripts/inspect_game.py): executable-header architecture evidence, layout hints, and loader-log locations. It does not launch games, read logs, or change files.
- [Expert workflow](expert-workflow.md): runtime identification, tiered investigation, hook selection, diagnostics, and validation.
- [Technical cautions](technical-cautions.md): historical compatibility conflicts, speech ABI, missing-state handling, and build/deploy traps.
- [Interaction checks](interaction-checks.md): menus, story dialogue, movement, speech, and test handoff.
- [Sources and licensing](external-sources.md): provenance, source versions, book link, and primary references.
- [Source manifest](source-manifest.json): every downloaded path, repository ref, and original blob ID.

## Route by task

- New project / engine / loader / initial analysis: [local project guide](local-project/docs/setup-guide.md); [pinned GitHub guide](template/docs/setup-guide.md).
- Screen-reader architecture / event announcements / game controls: [local project guide](local-project/docs/ACCESSIBILITY_MODDING_GUIDE.md); [pinned GitHub guide](template/docs/ACCESSIBILITY_MODDING_GUIDE.md).
- Loader entry points / references / Harmony / Tolk: [local project guide](local-project/docs/technical-reference.md); [pinned GitHub guide](template/docs/technical-reference.md).
- Menu structure / labels / activation / keyboard focus: [local project guide](local-project/docs/menu-accessibility-checklist.md); [pinned GitHub guide](template/docs/menu-accessibility-checklist.md).
- Complex menu interaction / label resolution: [local project guide](local-project/docs/menu-accessibility-patterns.md); [pinned GitHub guide](template/docs/menu-accessibility-patterns.md).
- Exclusive handlers / context changes / stale selection: [local project guide](local-project/docs/state-management-guide.md); [pinned GitHub guide](template/docs/state-management-guide.md).
- Private field access / text components / metadata caching: [local project guide](local-project/docs/unity-reflection-guide.md); [pinned GitHub guide](template/docs/unity-reflection-guide.md).
- Language detection / fallback / formatting / translated strings: [local project guide](local-project/docs/localization-guide.md); [pinned GitHub guide](template/docs/localization-guide.md).
- Old Unity runtimes / legacy UI / patching alternatives: [local project guide](local-project/docs/legacy-unity-modding.md); [pinned GitHub guide](template/docs/legacy-unity-modding.md).
- Historical compatibility reports, verify before applying: [local project guide](local-project/docs/known-issues.md); [pinned GitHub guide](template/docs/known-issues.md).
- Release contents / controls / installation / licensing: [local project guide](local-project/docs/distribution-guide.md); [pinned GitHub guide](template/docs/distribution-guide.md).
- Repository hygiene / GitHub workflow / decompiled exclusions: [local project guide](local-project/docs/git-github-guide.md); [pinned GitHub guide](template/docs/git-github-guide.md).
- External book reference and reuse status: [local project guide](local-project/docs/external-references/book-of-accessibility-modding.md); [pinned GitHub guide](template/docs/external-references/book-of-accessibility-modding.md).

## Code starters and helpers

Review the target runtime and the cautions before copying. Local files contain uncommitted changes, and archived templates contain intentional substitution markers. None were compiled or gameplay-tested merely by being bundled.

### bepinex

- csproj.template: [GitHub starter](../assets/template/templates/bepinex/csproj.template); [local working copy](../assets/local-project/templates/bepinex/csproj.template).
- DebugLogger.cs.template: [GitHub starter](../assets/template/templates/bepinex/DebugLogger.cs.template); [local working copy](../assets/local-project/templates/bepinex/DebugLogger.cs.template).
- Main.cs.template: [GitHub starter](../assets/template/templates/bepinex/Main.cs.template); [local working copy](../assets/local-project/templates/bepinex/Main.cs.template).
- ModConfig.cs.template: [GitHub starter](../assets/template/templates/bepinex/ModConfig.cs.template); [local working copy](../assets/local-project/templates/bepinex/ModConfig.cs.template).
- ScreenReader.cs.template: [GitHub starter](../assets/template/templates/bepinex/ScreenReader.cs.template); [local working copy](../assets/local-project/templates/bepinex/ScreenReader.cs.template).

### melonloader

- csproj.template: [GitHub starter](../assets/template/templates/melonloader/csproj.template); [local working copy](../assets/local-project/templates/melonloader/csproj.template).
- DebugLogger.cs.template: [GitHub starter](../assets/template/templates/melonloader/DebugLogger.cs.template); [local working copy](../assets/local-project/templates/melonloader/DebugLogger.cs.template).
- Main.cs.template: [GitHub starter](../assets/template/templates/melonloader/Main.cs.template); [local working copy](../assets/local-project/templates/melonloader/Main.cs.template).
- ModConfig.cs.template: [GitHub starter](../assets/template/templates/melonloader/ModConfig.cs.template); [local working copy](../assets/local-project/templates/melonloader/ModConfig.cs.template).
- ScreenReader.cs.template: [GitHub starter](../assets/template/templates/melonloader/ScreenReader.cs.template); [local working copy](../assets/local-project/templates/melonloader/ScreenReader.cs.template).

### shared

- AccessStateManager.cs.template: [GitHub starter](../assets/template/templates/shared/AccessStateManager.cs.template); [local working copy](../assets/local-project/templates/shared/AccessStateManager.cs.template).
- game-api.md.template: [GitHub starter](../assets/template/templates/shared/game-api.md.template); [local working copy](../assets/local-project/templates/shared/game-api.md.template).
- Handler.cs.template: [GitHub starter](../assets/template/templates/shared/Handler.cs.template); [local working copy](../assets/local-project/templates/shared/Handler.cs.template).
- Loc.cs.template: [GitHub starter](../assets/template/templates/shared/Loc.cs.template); [local working copy](../assets/local-project/templates/shared/Loc.cs.template).
- project_status.md.template: [GitHub starter](../assets/template/templates/shared/project_status.md.template); [local working copy](../assets/local-project/templates/shared/project_status.md.template).
- ReflectionHelper.cs.template: [GitHub starter](../assets/template/templates/shared/ReflectionHelper.cs.template); [local working copy](../assets/local-project/templates/shared/ReflectionHelper.cs.template).

### Mod helper scripts

Read before running. Helpers can inspect paths or install repository hooks. Build/deploy scripts shown inside the guides are examples to create or adapt in the target project, not scripts guaranteed to exist in this library.

- [Get-MelonLoaderInfo.ps1](../assets/template/scripts/Get-MelonLoaderInfo.ps1); [local copy](../assets/local-project/scripts/Get-MelonLoaderInfo.ps1).
- [hooks/pre-commit](../assets/template/scripts/hooks/pre-commit); [local copy](../assets/local-project/scripts/hooks/pre-commit).
- [Install-GitHooks.ps1](../assets/template/scripts/Install-GitHooks.ps1); [local copy](../assets/local-project/scripts/Install-GitHooks.ps1).
- [Test-ModSetup.ps1](../assets/template/scripts/Test-ModSetup.ps1); [local copy](../assets/local-project/scripts/Test-ModSetup.ps1).

## Complete document snapshots

The lists below include all archived documents, including German originals and project history. Assistant-instruction snapshots are historical reference, not active instructions. The original book-reference note is retained as supplied; the book itself is linked in Sources.

### Current local project

- [CHANGELOG.md](local-project/CHANGELOG.md)
- [CONTRIBUTING](local-project/CONTRIBUTING)
- [docs/ACCESSIBILITY_MODDING_GUIDE.md](local-project/docs/ACCESSIBILITY_MODDING_GUIDE.md)
- [docs/distribution-guide.md](local-project/docs/distribution-guide.md)
- [docs/external-references/book-of-accessibility-modding.md](local-project/docs/external-references/book-of-accessibility-modding.md)
- [docs/git-github-guide.md](local-project/docs/git-github-guide.md)
- [docs/known-issues.md](local-project/docs/known-issues.md)
- [docs/legacy-unity-modding.md](local-project/docs/legacy-unity-modding.md)
- [docs/localization-guide.md](local-project/docs/localization-guide.md)
- [docs/menu-accessibility-checklist.md](local-project/docs/menu-accessibility-checklist.md)
- [docs/menu-accessibility-patterns.md](local-project/docs/menu-accessibility-patterns.md)
- [docs/setup-guide.md](local-project/docs/setup-guide.md)
- [docs/state-management-guide.md](local-project/docs/state-management-guide.md)
- [docs/technical-reference.md](local-project/docs/technical-reference.md)
- [docs/unity-reflection-guide.md](local-project/docs/unity-reflection-guide.md)
- [docs-de/setup-guide.md](local-project/docs-de/setup-guide.md)
- [docs-de/technical-reference.md](local-project/docs-de/technical-reference.md)
- [LICENSE](local-project/LICENSE)
- [project-instructions.md](local-project/project-instructions.md)
- [README.md](local-project/README.md)

### Pinned Codex fork

- [CHANGELOG.md](template/CHANGELOG.md)
- [CONTRIBUTING](template/CONTRIBUTING)
- [docs/ACCESSIBILITY_MODDING_GUIDE.md](template/docs/ACCESSIBILITY_MODDING_GUIDE.md)
- [docs/distribution-guide.md](template/docs/distribution-guide.md)
- [docs/external-references/book-of-accessibility-modding.md](template/docs/external-references/book-of-accessibility-modding.md)
- [docs/git-github-guide.md](template/docs/git-github-guide.md)
- [docs/known-issues.md](template/docs/known-issues.md)
- [docs/legacy-unity-modding.md](template/docs/legacy-unity-modding.md)
- [docs/localization-guide.md](template/docs/localization-guide.md)
- [docs/menu-accessibility-checklist.md](template/docs/menu-accessibility-checklist.md)
- [docs/menu-accessibility-patterns.md](template/docs/menu-accessibility-patterns.md)
- [docs/setup-guide.md](template/docs/setup-guide.md)
- [docs/state-management-guide.md](template/docs/state-management-guide.md)
- [docs/technical-reference.md](template/docs/technical-reference.md)
- [docs/unity-reflection-guide.md](template/docs/unity-reflection-guide.md)
- [docs-de/setup-guide.md](template/docs-de/setup-guide.md)
- [docs-de/technical-reference.md](template/docs-de/technical-reference.md)
- [LICENSE](template/LICENSE)
- [project-instructions.de.md](template/project-instructions.de.md)
- [project-instructions.md](template/project-instructions.md)
- [README.md](template/README.md)

### Differing original upstream documents

- [docs/ACCESSIBILITY_MODDING_GUIDE.md](upstream/docs/ACCESSIBILITY_MODDING_GUIDE.md)
- [docs/external-references/book-of-accessibility-modding.md](upstream/docs/external-references/book-of-accessibility-modding.md)
- [docs/git-github-guide.md](upstream/docs/git-github-guide.md)
- [docs/known-issues.md](upstream/docs/known-issues.md)
- [docs/setup-guide.md](upstream/docs/setup-guide.md)
- [docs/unity-reflection-guide.md](upstream/docs/unity-reflection-guide.md)
- [docs-de/localization-guide.md](upstream/docs-de/localization-guide.md)
- [docs-de/menu-accessibility-checklist.md](upstream/docs-de/menu-accessibility-checklist.md)
- [docs-de/setup-guide.md](upstream/docs-de/setup-guide.md)
- [project-instructions.md](upstream/project-instructions.md)

## Update policy

Keep existing source versions distinguishable when refreshing. Fetch only from the recorded repositories or verified primary sources, check licenses, compare relevant changes, then update the source/research manifests and inventory. Preserve attribution; research notes are a synthesis, not permission to redistribute the inspected projects. Do not overwrite a target game project with archived templates. Recheck the target game APIs and loader compatibility regardless of snapshot age.
