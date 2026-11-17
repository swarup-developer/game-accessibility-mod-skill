# Regression Checks and Game Updates

Use for substantial behavior changes, compatibility repairs, and release preparation. Select the cases that exercise the changed boundary; do not create a large test suite for a small documentation or reversible configuration edit.

## Preserve a reproducible compatibility record

Record the game version/storefront/branch, executable hash where useful, OS/architecture, loader and interop versions, mod artifact hash, speech library build, screen reader version, language, input mode, and starting scene/save. A source branch or repository commit is not proof that a matching release binary was tested.

After a game update, inspect the specific types, signatures, hooks, assets, and input actions used by the mod. Verify registration and execution separately. Keep optional-feature incompatibility visible without unnecessarily disabling unrelated working features. Do not interpret a reflective lookup returning null as an authoritative game value.

## Useful automated boundaries

Tests are most valuable where the mod owns deterministic behavior that can fail independently of the game:

- Semantic text conversion: preserve costs, quantities, negative values, comparison signs, translated names, and identified icons while removing presentation tags.
- Localized messages: placeholder substitution, missing-key diagnostics, language changes, Unicode, and meaningful fallback behavior.
- Focus arbitration: one press reaches one context; closing a modal does not activate the underlying control; stale targets lose their binding.
- Event routing: category/source filters, history retention independent of speech, cancellation of obsolete requests, and two identical legitimate events.
- Configuration: migrated settings, unknown bindings, restoring defaults, and invalid values without silent data loss.

The inspected Say the Spire tests exercise markup/icon interpretation, variable substitution, missing translations, and event settings. They illustrate testable boundaries; do not copy their exact strings or permissive fallback choices as requirements. [Sources: message tests](research-sources.md#spire-message-tests), [event settings tests](research-sources.md#spire-event-tests).

## Runtime acceptance paths

For the changed feature, verify the smallest complete player journey with the actual screen reader where available:

- Cold launch to menu to gameplay, then pause/resume and return to menu.
- Navigate, activate, cancel, reopen, and recover focus after item removal or context replacement.
- Read a long description or dialogue, inspect choices, change selection, and confirm exactly once.
- Save/load or scene reload; ensure old references, subscriptions, context paths, and queued speech are invalidated.
- Lose/regain window focus while a key is held; check there is no stuck movement or unintended activation.
- Restart/switch the reader or backend if supported; verify useful diagnostics and no obsolete speech replay.

For requested controller, braille, alternate language, mono audio, or multiplayer support, add a representative case. Test client/host authority and only information available to the local player when multiplayer behavior changes. Do not claim all those modes merely because a dependency advertises them.

## Profile the failing boundary

When navigation feels delayed, measure input receipt, game-state resolution, announcement construction, bridge call duration, and audible onset where feasible. A fast asynchronous return measures submission latency, not speech onset. Keep profiling optional and avoid logging full private dialogue unless required for diagnosis.

Compare repeated use in the same scene with scene reload and long sessions. Look for growing event queues, duplicated subscriptions, persistent stale references, and cross-domain object leaks. Differentiate frame-time work from the speech backend's own latency. The inspected speech manager times backend dispatch, which is useful evidence but does not measure what the player hears. [Source](research-sources.md#spire-speech).

## Report the supported conclusion

State which artifact and scenario were checked and what remains uncertain. "Build passed", "hook executed", "state changed", "NVDA spoke the expected label", and "the required gameplay path was completed" are progressively different conclusions. Package validation cannot establish game accessibility.

Preserve the previous installable mod artifact and rollback notes when deploying a compatibility repair. Do not overwrite a working installation with an unverified build simply to make an update appear complete.
