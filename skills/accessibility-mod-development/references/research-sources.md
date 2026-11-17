# GitHub Research Sources

Research date: 2026-11-17. These are immutable source references for the advanced notes. Findings are original technical synthesis; no third-party source files or binaries from these projects are redistributed in this expansion.

Development branches may describe unreleased APIs. Reading code establishes the implementation at that source revision, not correctness, installed-version compatibility, or screen-reader gameplay success. Design recommendations in the notes are explicitly adaptations or inferences. Do not copy code without checking its own license.

The accompanying [research manifest](research-manifest.json) records all inspected files, including comparison material not promoted to guidance. Read only the relevant source if an exact API or runtime claim needs re-verification.

## input-settings

[Unity-Technologies/InputSystem: Packages/com.unity.inputsystem/Documentation~/input-settings.md](https://github.com/Unity-Technologies/InputSystem/blob/6cb24c08607bfb90b8b688239c5fb0049cc089b8/Packages/com.unity.inputsystem/Documentation~/input-settings.md)

Ref: `6cb24c08607bfb90b8b688239c5fb0049cc089b8`. Blob: `a08781a12b06fe4b4cecc8cdf2a6eaf932efd4ff`.

Routing to focus/background, update-mode, and supported-device settings.

## input-lookups

[Unity-Technologies/InputSystem: Packages/com.unity.inputsystem/Documentation~/look-up-bindings.md](https://github.com/Unity-Technologies/InputSystem/blob/6cb24c08607bfb90b8b688239c5fb0049cc089b8/Packages/com.unity.inputsystem/Documentation~/look-up-bindings.md)

Ref: `6cb24c08607bfb90b8b688239c5fb0049cc089b8`. Blob: `d25c11b875286acf3c6f3a95547c2553ce2ebb0d`.

Enumerating actual actions and bindings; example action names are not a target-game contract.

## input-conflicts

[Unity-Technologies/InputSystem: Packages/com.unity.inputsystem/Documentation~/binding-conflicts.md](https://github.com/Unity-Technologies/InputSystem/blob/6cb24c08607bfb90b8b688239c5fb0049cc089b8/Packages/com.unity.inputsystem/Documentation~/binding-conflicts.md)

Ref: `6cb24c08607bfb90b8b688239c5fb0049cc089b8`. Blob: `bc9e96ddd8660749e23b6b122e27f484e861c6b4`.

Action-type and map/asset limits of built-in shortcut conflict resolution.

## input-rebinding

[Unity-Technologies/InputSystem: Packages/com.unity.inputsystem/Documentation~/interactive-rebinding.md](https://github.com/Unity-Technologies/InputSystem/blob/6cb24c08607bfb90b8b688239c5fb0049cc089b8/Packages/com.unity.inputsystem/Documentation~/interactive-rebinding.md)

Ref: `6cb24c08607bfb90b8b688239c5fb0049cc089b8`. Blob: `3f126457c80ca9be56387bf1589d0910a74a77f8`.

Targeted capture, exclusions, cancellation, and disposal of rebinding operations.

## input-persistence

[Unity-Technologies/InputSystem: Packages/com.unity.inputsystem/Documentation~/save-load-rebinds.md](https://github.com/Unity-Technologies/InputSystem/blob/6cb24c08607bfb90b8b688239c5fb0049cc089b8/Packages/com.unity.inputsystem/Documentation~/save-load-rebinds.md)

Ref: `6cb24c08607bfb90b8b688239c5fb0049cc089b8`. Blob: `6bc8b55d64a70dd6e1fa8732fc917571e5d2bc49`.

Saving/restoring overrides; default restore behavior can remove other overrides.

## input-display

[Unity-Technologies/InputSystem: Packages/com.unity.inputsystem/Documentation~/display-bindings.md](https://github.com/Unity-Technologies/InputSystem/blob/6cb24c08607bfb90b8b688239c5fb0049cc089b8/Packages/com.unity.inputsystem/Documentation~/display-bindings.md)

Ref: `6cb24c08607bfb90b8b688239c5fb0049cc089b8`. Blob: `d529883ca3c66f64224758d1b28e2f98fdb51b26`.

Effective overrides and human-readable display strings; keyboard layout can change labels.

## input-background

[Unity-Technologies/InputSystem: Packages/com.unity.inputsystem/Documentation~/background-behavior.md](https://github.com/Unity-Technologies/InputSystem/blob/6cb24c08607bfb90b8b688239c5fb0049cc089b8/Packages/com.unity.inputsystem/Documentation~/background-behavior.md)

Ref: `6cb24c08607bfb90b8b688239c5fb0049cc089b8`. Blob: `bd04108a3c3ba9db0c2b333f5944350f3ce10606`.

Configurable focus-loss resets, cancellation, and background behavior.

## input-rebind-sample

[Unity-Technologies/InputSystem: Assets/Samples/RebindingUI/RebindActionUI.cs](https://github.com/Unity-Technologies/InputSystem/blob/6cb24c08607bfb90b8b688239c5fb0049cc089b8/Assets/Samples/RebindingUI/RebindActionUI.cs)

Ref: `6cb24c08607bfb90b8b688239c5fb0049cc089b8`. Blob: `9b581edd160393428b35871233dd628b40f3bf39`.

Official sample: saved enable state, targeted capture, action-map suppression, cancel/complete cleanup, disposal, and display refresh. Development APIs require target-version checks.

## renpy-self-voicing

[renpy/renpy: sphinx/source/self_voicing.rst](https://github.com/renpy/renpy/blob/dd84698dbe32bcc646ff4fc42567b0790333348e/sphinx/source/self_voicing.rst)

Ref: `dd84698dbe32bcc646ff4fc42567b0790333348e`. Blob: `a721e2c3f9d017e9f3e63187a385f0063d2ff26c`.

Self-voicing, alternate labels, distinct output modes; verify the shipped engine version.

## renpy-accessibility-implementation

[renpy/renpy: renpy/common/00accessibility.rpy](https://github.com/renpy/renpy/blob/dd84698dbe32bcc646ff4fc42567b0790333348e/renpy/common/00accessibility.rpy)

Ref: `dd84698dbe32bcc646ff4fc42567b0790333348e`. Blob: `4d38dc70f675625333cce8ef7a2bc2133865d58c`.

Conditional descriptive text and accessibility implementation; inspected relevant opening section.

## godot-accessibility

[godotengine/godot-docs: tutorials/ui/creating_applications.rst](https://github.com/godotengine/godot-docs/blob/889adb4a3fa815e6efc4e3007e84454e96162b1f/tutorials/ui/creating_applications.rst)

Ref: `889adb4a3fa815e6efc4e3007e84454e96162b1f`. Blob: `e6235c8c84c499f1980cc5222d5d429eda736fc4`.

Screen reader integration section; AccessKit, labels, configuration, and TTS distinction.

## godot-focus

[godotengine/godot-docs: tutorials/ui/gui_navigation.rst](https://github.com/godotengine/godot-docs/blob/889adb4a3fa815e6efc4e3007e84454e96162b1f/tutorials/ui/gui_navigation.rst)

Ref: `889adb4a3fa815e6efc4e3007e84454e96162b1f`. Blob: `7a98bb2db1664eb2b176a1ec1cf84c3484bce16f`.

Initial focus, explicit neighbors, UI action scope, and hidden-node focus.

## godot-accessibility-api

[godotengine/godot-docs: classes/class_accessibilityserver.rst](https://github.com/godotengine/godot-docs/blob/889adb4a3fa815e6efc4e3007e84454e96162b1f/classes/class_accessibilityserver.rst)

Ref: `889adb4a3fa815e6efc4e3007e84454e96162b1f`. Blob: `a785c70265b9a7a3a9a93e1c032a0584f3833476`.

AccessibilityServer interface; development documentation, not a target game's guaranteed API.

## il2cpp-injection

[BepInEx/Il2CppInterop: Documentation/Class-Injection.md](https://github.com/BepInEx/Il2CppInterop/blob/81a6f78c8b653e0da4a3420ac4cd00819e8b6292/Documentation/Class-Injection.md)

Ref: `81a6f78c8b653e0da4a3420ac4cd00819e8b6292`. Blob: `c9d6dfc72c2819f69eeba86f51115ace1224564f`.

Registration, construction, cross-domain lifetime, and reference-cycle caveats.

## nvda-controller

[nvaccess/nvda: extras/controllerClient/readme.md](https://github.com/nvaccess/nvda/blob/25e8f022113df7251a022c9714c10407cfb0a702/extras/controllerClient/readme.md)

Ref: `25e8f022113df7251a022c9714c10407cfb0a702`. Blob: `d4788c6defde978b1d22ac1fc97776b68a70244a`.

Status codes, architecture matching, and versioned controller interfaces.

## nvda-controller-idl

[nvaccess/nvda: nvdaHelper/interfaces/nvdaController/nvdaController.idl](https://github.com/nvaccess/nvda/blob/25e8f022113df7251a022c9714c10407cfb0a702/nvdaHelper/interfaces/nvdaController/nvdaController.idl)

Ref: `25e8f022113df7251a022c9714c10407cfb0a702`. Blob: `462396950b552169bfc684392a7cf29743d65d08`.

SSML asynchronous/synchronous behavior, mark callback conditions, and interface signatures.

## nvda-managed-example

[nvaccess/nvda: extras/controllerClient/examples/example_csharp/NVDA.cs](https://github.com/nvaccess/nvda/blob/25e8f022113df7251a022c9714c10407cfb0a702/extras/controllerClient/examples/example_csharp/NVDA.cs)

Ref: `25e8f022113df7251a022c9714c10407cfb0a702`. Blob: `d00a5da8603ce23fe5c3abc3c346cbe92f15adf3`.

Native imports and error propagation; example code, not a complete lifetime guarantee.

## prism-header

[ethindp/prism: include/prism.h](https://github.com/ethindp/prism/blob/2819206318c3e9040f5f5bae840ddff9a40294fb/include/prism.h)

Ref: `2819206318c3e9040f5f5bae840ddff9a40294fb`. Blob: `26abaad229ba3ccb622563fe5eed0b9316487f2b`.

Calling convention, configuration declarations, ownership-related interface symbols.

## prism-backends

[ethindp/prism: doc/src/api/c/backend-functions.md](https://github.com/ethindp/prism/blob/2819206318c3e9040f5f5bae840ddff9a40294fb/doc/src/api/c/backend-functions.md)

Ref: `2819206318c3e9040f5f5bae840ddff9a40294fb`. Blob: `72453243f5381df34734c02040b09b786ab0b0cb`.

Feature flags, advisory availability, backend disposal, and UTF-8 contracts.

## prism-threading

[ethindp/prism: doc/src/api/c/thread-safety.md](https://github.com/ethindp/prism/blob/2819206318c3e9040f5f5bae840ddff9a40294fb/doc/src/api/c/thread-safety.md)

Ref: `2819206318c3e9040f5f5bae840ddff9a40294fb`. Blob: `6641bafc61f75907952a5888e95be3cbcc988c2a`.

Shared instance serialization, registry behavior, callback threads, and shutdown races.

## prism-conventions

[ethindp/prism: doc/src/api/c/conventions.md](https://github.com/ethindp/prism/blob/2819206318c3e9040f5f5bae840ddff9a40294fb/doc/src/api/c/conventions.md)

Ref: `2819206318c3e9040f5f5bae840ddff9a40294fb`. Blob: `6c12fc6494b8a4a78717dd846d7702925f50e8b7`.

Return values, nullability, pointer ownership, and data lifetime.

## prism-context

[ethindp/prism: doc/src/api/c/context-management.md](https://github.com/ethindp/prism/blob/2819206318c3e9040f5f5bae840ddff9a40294fb/doc/src/api/c/context-management.md)

Ref: `2819206318c3e9040f5f5bae840ddff9a40294fb`. Blob: `0adf7e6a4d6b92264a0125648f1aad4c30a34928`.

Versioned config, default initialization, independent context/backend lifetime.

## spire-speech

[bradjrenshaw/say-the-spire2: Speech/SpeechManager.cs](https://github.com/bradjrenshaw/say-the-spire2/blob/237df52ac8f807ecadc25ef61c9b31d00ec95ee2/Speech/SpeechManager.cs)

Ref: `237df52ac8f807ecadc25ef61c9b31d00ec95ee2`. Blob: `3696904c791a3852abe563e6184112f742089ed6`.

Backend selection, unload, override, and dispatch profiling.

## spire-focus

[bradjrenshaw/say-the-spire2: UI/FocusContext.cs](https://github.com/bradjrenshaw/say-the-spire2/blob/237df52ac8f807ecadc25ef61c9b31d00ec95ee2/UI/FocusContext.cs)

Ref: `237df52ac8f807ecadc25ef61c9b31d00ec95ee2`. Blob: `4ff5ce0da1383c81f5d4563a405225f3686608b2`.

Container-path divergence and reset for changed-context announcements.

## spire-events

[bradjrenshaw/say-the-spire2: Events/EventDispatcher.cs](https://github.com/bradjrenshaw/say-the-spire2/blob/237df52ac8f807ecadc25ef61c9b31d00ec95ee2/Events/EventDispatcher.cs)

Ref: `237df52ac8f807ecadc25ef61c9b31d00ec95ee2`. Blob: `944e2037c0c73753549280aac7551644412d9336`.

Separate source filtering, automatic speech, event-buffer insertion, and ordering.

## spire-buffer

[bradjrenshaw/say-the-spire2: Buffers/Buffer.cs](https://github.com/bradjrenshaw/say-the-spire2/blob/237df52ac8f807ecadc25ef61c9b31d00ec95ee2/Buffers/Buffer.cs)

Ref: `237df52ac8f807ecadc25ef61c9b31d00ec95ee2`. Blob: `d5ce7e83e09800b7dada3ed3cd69a3de1a82ee8a`.

Review cursor, optional follow-latest, repopulation, and clearing live bindings.

## spire-message-tests

[bradjrenshaw/say-the-spire2: Tests/MessageTests.cs](https://github.com/bradjrenshaw/say-the-spire2/blob/237df52ac8f807ecadc25ef61c9b31d00ec95ee2/Tests/MessageTests.cs)

Ref: `237df52ac8f807ecadc25ef61c9b31d00ec95ee2`. Blob: `95ad0b2ee6762e19a8ebe3d637d7071c96c842a8`.

Markup/icon conversion, substitutions, missing localization, and independent tests.

## spire-event-tests

[bradjrenshaw/say-the-spire2: Tests/EventRegistryTests.cs](https://github.com/bradjrenshaw/say-the-spire2/blob/237df52ac8f807ecadc25ef61c9b31d00ec95ee2/Tests/EventRegistryTests.cs)

Ref: `237df52ac8f807ecadc25ef61c9b31d00ec95ee2`. Blob: `e4989d4f60458bd7ae24670326c07558178f29ed`.

Event descriptors and distinct announce/buffer settings.

## spire-map

[bradjrenshaw/say-the-spire2: Map/MapReachability.cs](https://github.com/bradjrenshaw/say-the-spire2/blob/237df52ac8f807ecadc25ef61c9b31d00ec95ee2/Map/MapReachability.cs)

Ref: `237df52ac8f807ecadc25ef61c9b31d00ec95ee2`. Blob: `25e098cd37d0aec056543dc874128fa13470c442`.

Graph traversal and modifiers; documented approximations are not portable game rules.

## spire-input

[bradjrenshaw/say-the-spire2: Input/InputManager.cs](https://github.com/bradjrenshaw/say-the-spire2/blob/237df52ac8f807ecadc25ef61c9b31d00ec95ee2/Input/InputManager.cs)

Ref: `237df52ac8f807ecadc25ef61c9b31d00ec95ee2`. Blob: `3fd0731c6336611aecdff6af4e9c7edbe87ebcb0`.

Input action inventory, rebind capture, held-button snapshot, and game-specific interception.

## spire-controller

[bradjrenshaw/say-the-spire2: Input/ControllerInput.cs](https://github.com/bradjrenshaw/say-the-spire2/blob/237df52ac8f807ecadc25ef61c9b31d00ec95ee2/Input/ControllerInput.cs)

Ref: `237df52ac8f807ecadc25ef61c9b31d00ec95ee2`. Blob: `c6d16550452dbfe1664b56f2ab6bea047ddca78f`.

Named controller actions; inventory alone is not evidence of hotplug/rebind correctness.

## stardew-features

[stardew-access/stardew-access: docs/features.md](https://github.com/stardew-access/stardew-access/blob/c3568b659783975cd25f2385853a48ec15911e9c/docs/features.md)

Ref: `c3568b659783975cd25f2385853a48ec15911e9c`. Blob: `45a1941661114c050e7844bd21b0ed174b627c1a`.

Documented narration, inspection/travel distinctions, interruption settings, and limitations.

## stardew-speech

[stardew-access/stardew-access: stardew-access/ScreenReader/ScreenReaderImpl.cs](https://github.com/stardew-access/stardew-access/blob/c3568b659783975cd25f2385853a48ec15911e9c/stardew-access/ScreenReader/ScreenReaderImpl.cs)

Ref: `c3568b659783975cd25f2385853a48ec15911e9c`. Blob: `9ab746bc5bdcd7e3680235200d7a8115c6c8a4cb`.

Separate menu/tile/chat comparisons and speech history; implementation tradeoffs require review.

## stardew-radar

[stardew-access/stardew-access: stardew-access/Features/Radar.cs](https://github.com/stardew-access/stardew-access/blob/c3568b659783975cd25f2385853a48ec15911e9c/stardew-access/Features/Radar.cs)

Ref: `c3568b659783975cd25f2385853a48ec15911e9c`. Blob: `ae3da0ccd9c6fcd3e146fbbdead8a77f7f448753`.

Category-filtered scanning and directional sound cues; not route reachability.

## stardew-pathfinder

[stardew-access/stardew-access: stardew-access/Utils/Pathfinder.cs](https://github.com/stardew-access/stardew-access/blob/c3568b659783975cd25f2385853a48ec15911e9c/stardew-access/Utils/Pathfinder.cs)

Ref: `c3568b659783975cd25f2385853a48ec15911e9c`. Blob: `c63859b0bff36348d08cebf6ca69fba5e73209ee`.

Game path controller, cancellation, timers, and retry logic as an example to review critically.

## ats-map

[rashadnaqeeb/ats-accessibility-mod: ATSAccessibility/Handlers/MapNavigator.cs](https://github.com/rashadnaqeeb/ats-accessibility-mod/blob/983f35a62d4ede63ca03a88901e69ca235693607/ATSAccessibility/Handlers/MapNavigator.cs)

Ref: `983f35a62d4ede63ca03a88901e69ca235693607`. Blob: `0d5966cb94cc906f54f871585eafe9921e414a79`.

Virtual cursor, game bounds, origin-relative coordinates, and context reset.

## ats-input

[rashadnaqeeb/ats-accessibility-mod: ATSAccessibility/Core/InputBlocker.cs](https://github.com/rashadnaqeeb/ats-accessibility-mod/blob/983f35a62d4ede63ca03a88901e69ca235693607/ATSAccessibility/Core/InputBlocker.cs)

Ref: `983f35a62d4ede63ca03a88901e69ca235693607`. Blob: `e329c7c93848cb4818ff52eda8e96b549120b0f8`.

Game-specific action whitelist, text-entry caveat, and one-shot cancel handling.

## ats-speech

[rashadnaqeeb/ats-accessibility-mod: ATSAccessibility/Utils/Speech.cs](https://github.com/rashadnaqeeb/ats-accessibility-mod/blob/983f35a62d4ede63ca03a88901e69ca235693607/ATSAccessibility/Utils/Speech.cs)

Ref: `983f35a62d4ede63ca03a88901e69ca235693607`. Blob: `8beedc0a0a0753978f4b8effdff1307a9ba61b34`.

Version-specific UTF-8 bindings, backend ownership, and markup conversion; not a universal binding.
