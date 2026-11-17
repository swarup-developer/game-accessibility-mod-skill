# Expert Workflow

Use this for initial architecture, a substantial new feature, or a difficult integration failure. Scale the investigation to the requested change.

## Establish the runtime contract

Record the game build and storefront, executable architecture, engine/backend, mod loader and version, framework target, screen reader and bridge, deployment destination, and relevant logs. Distinguish the original game executable from launchers and helper processes. Use inspected binary metadata and runtime logs to corroborate file-layout clues.

Record existing game and screen-reader bindings before assigning keys. Identify whether input uses legacy Unity polling, the new Input System, a custom abstraction, or another engine. Test which layer owns a press before attempting interception.

For Unity, distinguish Mono from IL2CPP before choosing references and hooks. An IL2CPP type dump can establish names and signatures while lacking implementation bodies; do not treat generated stubs as proof of behavior. Use compatible interop tooling and runtime probes rather than an unrelated Mono project file.

## Research in tiers

Before the first game-integrated feature, establish the minimum shared foundation:

- Entry points and object lifetime: how relevant systems become available, are replaced, and are destroyed.
- Input: current controls, focus ownership, modal priority, and safe bindings.
- UI: active-screen detection, item enumeration, label/value sources, activation, and cancellation.
- State: whether a simple exclusive handler suffices or nested screens need an explicit context stack.
- Localization: how the game resolves language and updates text, if relevant to the feature.

Analyze combat, crafting, navigation, inventory, and other mechanics when implementing those features. Avoid spending the setup phase cataloguing unrelated systems.

For each integration point, document declaring type, exact overload, field/property ownership, parameter/return types, lifecycle, source location, and runtime observations. For each player feature, document trigger, available information, game action, spoken result, and a reproducible test. Keep unknowns visible instead of assigning guessed defaults.

## Choose hooks by their purpose

Prefer a documented API or event. Use a postfix for observing completed actions when its timing is correct. Use a prefix when interception is actually needed; returning false may skip game behavior and other prefixes, so inspect the consequences. A menu input hook must not suppress unrelated simulation updates.

Verify the declaring type, overload, generic arguments, and runtime method signature. Inspect patch registration logs and hook execution separately. A successful patch installation does not prove the relevant code path runs.

Keep Unity-object access on its appropriate game thread. Do not repair lifecycle uncertainty with arbitrary sleeps. Correlate scene/context, object identity, input event, hook entry, game-state change, and speech request in a debug trace.

## Make focus and speech agree with game state

Use the game's active screen as the authority. When a popup opens, its context owns input. On cancel, invoke the game's real close action and reconcile focus with the resulting screen. Prevent the same press from reaching the newly exposed context.

For changing lists, preserve stable selection identity where possible and provide a predictable nearest-item recovery if the item disappears. Announce the new state rather than reading a stale cached string.

Prioritize navigation response, essential story text, urgent hazards, and supporting detail according to the game. Bind pending speech to its originating context so it can be discarded when obsolete. Do not infer speech completion from text length or an unsupported backend status query.

Map tooltips, hints, tutorial prompts, hover descriptions, icons, and dynamic values as part of coverage. A focusable button without its cost, disabled reason, or explanatory tooltip may remain unusable. Translate meaningful rich-text symbols to labels only after identifying what they mean in that game; do not globally erase every symbol.

## Diagnose by the failing layer

- No loader log: inspect launch target and loader compatibility before changing mod logic.
- Loader starts but plugin is missing: inspect discovery path, plugin metadata, architecture, runtime target, and dependency resolution.
- Plugin starts but no speech: inspect native loading, ABI, reader detection, output result, and actual reader behavior.
- Speech works but an action fails: trace input ownership, selected game object, eligibility, invoked callback, and authoritative state change.
- Wrong or repeated speech: trace event identity, typewriter updates, duplicate hooks, stale contexts, and queue cancellation.
- Scene/load crashes: trace destroyed references, static caches, initialization ordering, and repeated subscription or patch registration.

Address the first failing boundary. Change one justified cause, reproduce, and compare evidence. Do not use a catch-all handler to hide a broken integration.

## Build and installation are separate outcomes

Inspect project files for automatic post-build copying. Build to a staging location when possible, then deploy the verified artifact through the target project's script. A copy warning can coexist with a successful build; record the installed file hash/version independently.

Do not ship game assemblies copied by dependency resolution. Distinguish references needed to compile from files users may redistribute. Keep decompiled output excluded from compilation and publication.

After a game update, compare the specific signatures, assets, and behavior the mod uses. Re-run affected interaction tests; do not replace the entire architecture merely because a version changed.

## Verification that supports claims

Use meaningful tests for mod-owned parsing, focus ownership, queue cancellation, localization formatting, or other logic when changes warrant them. Compilation proves type/build consistency; simulated key presses prove only what the simulation observes. Runtime logs support lifecycle and state claims. Actual screen-reader interaction supports audible usability claims. Full playability requires coverage of the game's required paths.

In the handoff, name what changed, the installed artifact, evidence obtained, remaining limitations, and the next small keyboard test. Persist concise source/API findings and status so another session can continue without rediscovering them.

For engine-specific choices, capability-aware speech, complex review/navigation, or compatibility testing, follow the focused routes in [the library index](library-index.md). This synthesis adapts the licensed template guides. Technical caveats and primary sources are listed in [technical-cautions.md](technical-cautions.md), [external-sources.md](external-sources.md), and the [additional GitHub research register](research-sources.md).
