# Interaction and Acceptance Checks

Choose checks for the feature being changed. Test expected speech and actual game outcomes together; announcements alone can conceal a failed action.

## Menus and lists

- Identify the layout, existing focus/navigation system, available item types, activation callbacks, and modal ownership.
- Announce screen name, focused label, role where useful, value, selected/checked state, and a relevant disabled reason.
- Verify first opening, forward/backward navigation, value changes, activation, cancellation, reopening, and restoration of focus.
- Verify empty lists, dynamically added/removed items, loading, and inaccessible/missing labels. Do not silently omit an actionable control.
- Confirm rapid presses, held keys, nested screens, and closing a popup do not activate the underlying screen. Check gameplay input still works after leaving the menu.
- Keep announcements concise. Position/count information is useful when it provides orientation; avoid redundant counters on every focus change. Native controls may already supply this through the screen reader.

## Dialogue and story-heavy games

- Trace speaker, complete displayed text, page/line completion, choices, selection, confirmation, and the game's next-line action. Handle typewriter text at an appropriate completion boundary instead of announcing each partial frame.
- Keep narrator text, speaker names, subtitles, tutorial prompts, quest text, and inspectable descriptions distinguishable. Avoid duplicating fully voiced dialogue unless requested or needed for clarity.
- Offer a navigable way to review the currently available long text when the game lacks one. Ordinary screen-reader review does not guarantee that injected speech remains available for later review.
- Announce choices with their displayed wording and availability. Only disclose timers, consequences, hidden checks, or relationships that the game currently reveals to the player.
- Verify one-line and multiline text, identical lines on separate events, scrolling, dialogue interruption, timed choices, skipped scenes, save/load, and returning from pause/settings.
- Read text and move focus without advancing or choosing automatically. Do not freeze story timers or choose a response unless that assist was requested.
- Test transitions between dialogue and movement; accessible dialogue alone does not establish an accessible story game.

## Movement and world interaction

- Determine the coordinate system, player orientation, camera relationship, interaction range, and relevant reachable objects from evidence.
- Name targets using current game identities and labels; list indices can shift after movement or state changes.
- Expose useful location, facing, nearby interactive objects, obstacles, and action results using concise speech or configurable audio cues. Convey distance/direction only when reliably derived and appropriate to information the game reveals.
- Test turns, walls, stairs, doors, scene changes, disappearing targets, and changes in elevation where relevant. A hazard warning does not guarantee fall prevention or a safe route.
- Do not announce unexplored objectives through walls or promise pathfinding unless the feature has verified navigation data. Separate orientation guidance from any requested auto-movement.

## Speech and recovery

- Confirm speech with the user's actual screen reader when available, including focus changes and rapid navigation. A bridge-success log is not proof the user heard the text.
- Check startup with and without the screen reader, missing/wrong-architecture native dependencies, and bridge failure where relevant. Keep diagnostics discoverable and avoid repeated error storms.
- Verify high-priority speech does not permanently suppress navigation or truncate every dialogue line. Clear queued stale text after leaving a context.
- Check save/load and scene reload invalidate old object references. Errors should leave game controls usable whenever possible.

## A useful test handoff

State the installed artifact/version and starting game state, then provide the few keys needed to exercise the feature and the expected spoken result. Identify what the developer observed versus what still needs user confirmation. Ask for only the relevant error excerpt or behavior; do not require a blind user to confirm visual details.

Adapted from the Accessibility-mod-template documentation; attribution and license are in [SKILL.md](../SKILL.md).
