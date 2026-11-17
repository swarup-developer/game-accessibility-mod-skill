# Verified Key Bindings and Movement

Read before assigning controls or adding auto-walk. This is the user's preferred workflow: simple controls grounded in the target game, with complete implementation and evidence of behavior. It does not authorize changing unrelated keys or gameplay rules.

## Discover before assigning

Identify the installed game build and active input implementation. Inspect its control settings/current configuration, input source or API, existing mod handlers, and the relevant runtime context. Defaults on a web page do not prove the player's current bindings. Source examples named `Move`, `Fire`, or `gameplay` do not establish that those actions exist in the target game.

Record only what the feature needs: action identity, current effective binding and overrides, press/hold/release semantics, active contexts, original handler, source location, and any runtime confirmation. Include existing help/debug keys. Distinguish a known conflict, a candidate key, and a verified usable binding.

Unity's documented binding enumeration and effective-path/display APIs support inspecting configured actions and overrides. Use them only when that Input System/version is actually present. Other engines and legacy input need their own verified equivalent. [Sources: input binding lookup](research-sources.md#input-lookups), [effective binding display](research-sources.md#input-display).

## Choose the smallest usable control set

- Prefer the game's existing action or menu navigation where it already provides the needed interaction.
- Add a named semantic action only for the requested missing behavior. Prefer one verified single key for a toggle rather than separate arbitrary start/stop shortcuts.
- Do not allocate the entire function-key row, preassign speculative future features, or adopt another mod's layout. F1 is not universally free or universally forbidden; the target game's existing help and the user's choices decide.
- Avoid modifier chords by default for this user. Do not replace a conflicting candidate with an invented Ctrl/Alt/Shift combination. Use another evidenced single-key option, an existing accessible menu, or leave the new action unbound pending the smallest necessary user choice.
- Preserve OS and assistive-technology controls. Alt+Space opens the Windows window menu; it is not a neutral mod shortcut. NVDA's configured Insert/Caps Lock modifiers and numpad review commands also affect candidates. Check the user's actual layout/profile instead of requiring global screen-reader changes. [Sources: Windows menus](https://learn.microsoft.com/en-us/windows/win32/menurc/about-menus), [NVDA keyboard commands](https://download.nvaccess.org/documentation/userGuide.html#TheNVDAModifierKey).
- Reuse keys across mutually exclusive contexts only when focus ownership and transitions are verified. The same key is a conflict if two handlers can respond to one physical press.

## Implement the entire binding

Connect configuration/registration, event subscription or polling, enabled context, the real game action, state feedback, and cleanup. Generate help from the effective binding where possible, so changing a binding does not leave a false instruction.

For a toggle, use an appropriate press edge rather than toggling on every frame held. For a hold action, trace press and release, including cancellation on focus loss. Prevent mod-generated input from recursively retriggering its own command. A physical key can be observed without being consumed; verify whether the original game also handles it.

Unity's conflict handling depends on action type, action-map/asset relationships, and settings. It is not a universal conflict detector for Windows, a screen reader, another mod, or separate raw polling. Do not change the game's global input settings merely to make one shortcut win. [Source: input conflict documentation](research-sources.md#input-conflicts).

For rebinding, target the exact action/binding/control scheme, provide accessible capture/cancel feedback, suppress accidental activation, and restore the prior enabled state. Dispose the capture operation and detach callbacks on completion, cancellation, or teardown. Review a matching-version sample rather than copying development-only APIs. [Sources: interactive rebinding](research-sources.md#input-rebinding), [official sample](research-sources.md#input-rebind-sample).

If persistence is part of the request, preserve the player's unrelated overrides. Unity's default override-loading behavior can replace existing overrides, so inspect the relevant API arguments and ownership before applying a saved set. Verify after restart as well as immediately after saving. [Source: save/load rebinds](research-sources.md#input-persistence).

## Define auto-walk precisely

Continuous forward movement, route guidance, and navigation to a selected target are different features. Reuse established context; ask only if the requested behavior remains materially ambiguous. Do not silently turn a forward toggle into autonomous target selection, sprinting, combat, or pathfinding.

Trace normal player movement first: the game's movement action/controller, frame timing, orientation, grounded/collision state, movement restrictions, and cancellation. For a Green Hell-like open world or a Naruto-style action game, the title/genre is not evidence of a particular class, key, player controller, coordinate unit, or navigation mesh. Inspect the actual version before making those claims.

Use an existing verified movement interface. If the only available method is simulated held input, implement it only where authorized and justified: track the inputs the mod owns, release them on every stop/teardown path, and avoid releasing a key the player is physically holding without a verified ownership strategy. Do not use teleportation or direct transform changes as an unannounced replacement for walking.

Treat a forward toggle as explicit state with meaningful transitions: inactive, active, and stopped/cancelled with a reason. Integrate with the game's real pause, menus, cutscenes, loading, death, or control-lock states where relevant. Focus loss or disabling/unloading the mod must leave no mod-owned movement held. Prefer staying stopped on return until the player restarts. Unity's own device-reset behavior is configurable, so verify it rather than assuming it also clears synthetic/mod-owned state. [Source: focus and background behavior](research-sources.md#input-background).

If target navigation is requested, verify the target identity, reachable destination, player-compatible navigation interface, and path state. NPC pathfinding availability does not establish player compatibility. A requested destination is not a completed route: Unity documents that `SetDestination` success means the request was accepted and a path can remain pending. That engine contract does not establish that the target game uses `NavMeshAgent`. [Source: SetDestination](https://docs.unity3d.com/ScriptReference/AI.NavMeshAgent.SetDestination.html).

Use the game's route/movement completion evidence, not straight-line distance alone, to announce arrival. Stop and explain a lost/unreachable target rather than repeatedly forcing movement. Cliffs, hazards, stamina, jumping, and combat rules require their own verified handling; a warning is not proof of safe travel.

## Acceptance evidence

Exercise the real assigned input and trace: input event, selected semantic action, allowed context, movement/game-state change, and spoken result. Verify one press, a held key, rapid presses, cancellation, pause/menu entry, focus loss, scene change, disabling the feature, and return to gameplay as relevant. Check that normal manual controls still work.

For a movement toggle, confirm actual displacement along the expected direction and cessation of mod-owned movement after stop. A log saying "walking" is insufficient. For navigation, also test an obstacle, unavailable target, and route completion. Preserve saves and use an appropriate test state; do not assume a dangerous live route is suitable.

Record the installed artifact and the evidence actually obtained. If the game or screen-reader session cannot be exercised, provide the exact next keyboard test and mark runtime behavior unverified. Do not manufacture safe-key availability or working auto-walk to complete a checklist.
