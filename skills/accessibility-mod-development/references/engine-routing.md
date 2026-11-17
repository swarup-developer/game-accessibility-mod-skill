# Engine Routing and Native Accessibility

Use before choosing a loader, building a second speech layer, or treating a text-heavy game as fully accessible. Sources below are pinned research observations, not a promise that an older shipped game has current engine features.

## Choose the smallest suitable integration

Inspect the target game's existing keyboard controls, accessibility settings, exposed accessibility tree, and mod API first. Prefer repairing labels, focus order, descriptions, and missing state in a usable native system. Add custom speech where the existing system cannot convey the needed information. Verify that native and mod announcements do not both speak the same event.

The optional [game-folder inspector](../scripts/inspect_game.py) provides executable architecture evidence and layout hints. It neither establishes that a mod loader works nor identifies the correct executable among launchers.

## Ren'Py narrative games

The inspected upstream documentation describes self-voicing, direct screen-reader mode, clipboard mode, accessibility settings, and alternative text for displayables. It also describes `who_alt`, `what_alt`, grouping, and optional detail labels. [Source: Ren'Py self-voicing](research-sources.md#renpy-self-voicing).

For a target title, verify its bundled Ren'Py version and actual behavior before using those APIs or shortcut defaults. New upstream screen-reader integration must not be assumed available in an older release. Test a representative path through dialogue, choices, custom image buttons, preferences, save/load, rollback, and any custom movement screen.

When source-level modification is available, identify missing semantic text in the actual screen/displayable. Give image-only controls meaningful alternative labels; retain translated text and the game's own actions. Ensure speaker changes, thoughts, and meaningful visual-only story events have suitable descriptions without revealing future story content. Description should not unexpectedly add an interaction or advance the story.

Self-voicing and screen-reader mode are distinct output paths. Confirm which is active and whether the player's speech/braille settings apply. Clipboard output changes the clipboard and is an explicitly selected fallback, not a transparent speech bridge.

## Godot games

The inspected documentation describes AccessKit-based screen-reader integration, accessibility labels, and project configuration. Engine TTS is a separate facility. [Source: Godot screen-reader integration](research-sources.md#godot-accessibility).

Verify the shipped engine version, build options, and game's actual controls. A project built with custom-drawn UI may require semantic accessibility nodes or a custom interaction layer even when the engine supports accessibility. Do not automatically disable built-in accessibility because a different mod does so.

Check initial focus, directional neighbors, next/previous ordering, hidden controls, and modal restoration. The documented UI action namespace is for UI focus; do not reuse it indiscriminately for gameplay movement. [Source: Godot focus guide](research-sources.md#godot-focus).

Inspect available engine APIs in the target version before writing to accessibility labels or using `AccessibilityServer`. The inspected master API is not proof that a released game exposes the same class. [Source: Godot accessibility API](research-sources.md#godot-accessibility-api).

## Unity Mono and IL2CPP

For Mono, inspect matching managed game assemblies and loader/runtime references. For IL2CPP, generated managed proxies and metadata establish an interop surface, not reconstructed C# method bodies. Separate a missing hook, unsupported signature, collected native object, and failed cast before choosing a fix.

The inspected Il2CppInterop guide requires type registration before use of injected classes, describes different construction paths, and warns that native lifetime can outlast or undercut managed expectations. A managed reference alone does not prove an injected native object remains alive. Cross-domain reference cycles can also leak. [Source: class injection](research-sources.md#il2cpp-injection).

Use the loader's exact supported interop version and documented construction/cast model. Track ownership, scene lifetime, registration, and callback teardown. Verify ordinary entry, scene reload, save/load, and shutdown. Do not add arbitrary pointer reconstruction or repeated casts to conceal lifetime failures.

## Other engines and mod APIs

Existing projects demonstrate that the general accessibility design does not require Unity: Stardew Access uses its game's modding ecosystem, and Say the Spire 2 integrates Godot controls and game-specific types. Their classes, action names, and scene assumptions are not portable. [Source: case-study index](research-sources.md).

For another engine, establish its supported extension/source route and actual UI/input representation. Reuse the skill's evidence, speech, focus, and testing principles while choosing engine-appropriate tooling. If the supported route is unclear, identify the missing evidence before promising an implementation.
