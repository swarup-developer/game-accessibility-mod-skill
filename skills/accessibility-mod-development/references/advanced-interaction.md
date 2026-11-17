# Advanced Focus, Review, Events, and Spatial Interaction

These are adaptable design patterns from inspected implementations. An implementation's existence does not establish that every detail is correct, necessary, or suitable for a different game.

## Announce changed context

For hierarchical menus, represent the focused element's container path. When focus changes, announce the group names that changed, then the element, rather than repeating every ancestor. Reset that comparison on screen changes and ensure re-entering an identically named group is distinguishable by identity. Say the Spire's inspected `FocusContext` illustrates path comparison. [Source](research-sources.md#spire-focus).

Retain role, enabled/selected state, and essential values even when contextual names are suppressed. Names alone are not stable identities. Test two controls with identical text, focus restoration, a removed parent, and nested modals.

## Separate immediate speech from review

High-rate combat, status changes, and long descriptions may benefit from optional review buffers. Keep spoken-event preference and retained-event preference distinct so reducing automatic speech does not necessarily discard useful review information. The inspected dispatcher independently controls announcements and event-buffer insertion. [Source](research-sources.md#spire-events).

Choose bounded retention for append-only history. Preserve the review cursor while the user reads; make following the latest event an explicit behavior. For live object details, refresh current state and clear bindings when that context disappears. Avoid restoring by numeric position when item identity matters. Existing buffer code illustrates these concerns but is not a ready-made universal retention policy. [Source](research-sources.md#spire-buffer).

Do not require persistent disk history merely to support review. Keep story spoilers and other players' private information outside logs unless intentionally needed. Provide only review controls that solve an actual gap; native screen-reader review and injected speech have different capabilities.

## Treat events as semantic observations

Capture event identity, source, ordering, and the value at the relevant occurrence when historical meaning matters. Read live values for current-state queries. This distinction qualifies the rule against caching stale game values: an event snapshot records what happened, while a status query reports what is true now.

Use deduplication scoped to event/context identity. Two real hits of equal damage, two dialogue lines with identical text, or returning to the same control may all deserve separate output. Combine noisy event sequences only when the resulting summary preserves necessary order and decisions. User-configurable source/category filters can help high-volume games. The inspected event dispatcher and menu/tile speech checks provide examples. [Sources: event dispatch](research-sources.md#spire-events), [Stardew speech](research-sources.md#stardew-speech).

## Keep inspection, targeting, and travel distinct

A virtual map cursor supports inspection without moving the player. Use authoritative map bounds, visibility/discovery, terrain, and interaction eligibility. Explain the coordinate frame and origin; reset it when the session/map changes. The inspected Against the Storm navigator demonstrates bounded cursor movement and origin-relative coordinates. [Source](research-sources.md#ats-map).

An object list can be sorted by distance while leaving category filters and favorites optional. Euclidean proximity is not route length, and detection is not proof of reachability. A radar scan that enumerates tiles does not establish a collision-valid route. The inspected Stardew radar and pathfinder are different systems. [Sources: radar](research-sources.md#stardew-radar), [pathfinder](research-sources.md#stardew-pathfinder).

If travel assistance is in scope, use verified game navigation data, represent unreachable/lost targets explicitly, cancel on relevant context changes, and provide an immediate player stop action. Recheck target identity and route validity as the world changes. Do not copy another game's retry timers or background game-object access without validating thread and lifecycle rules.

For strategic graph maps, verify edges and traversal permissions against the current game, including temporary charges or rule modifiers. Browsing a possible route must not consume resources. An example mod's approximation for an unknown modifier is not evidence that the target game permits that route. [Source: inspected reachability implementation](research-sources.md#spire-map).

## Design cues that remain usable

Speech is suitable for names, state, and requested detail; concise audio cues can convey direction or repeated proximity changes. Define whether directions are screen-relative, camera-relative, player-relative, or world-relative. Test turning the camera separately from the character.

Let players adjust cue volume/rate and reduce clutter. Essential danger information should have a usable alternative when stereo localization is unavailable. Test mono output, simultaneous sounds, and masking by dialogue or music. These are design recommendations inferred from the inspected spatial systems, not properties established for a new game.

## Input edge cases

Use semantic actions with clear context ownership rather than scattered key checks. Rebinding should not activate the captured command; ignore keys/buttons already held when listening starts. Clear held state on focus loss/disconnect, and preserve native text entry, IME composition, and platform shortcuts when relevant.

Keyboard and controller bindings should have equivalent named actions when controller support is requested. Test press/release, repeat, modifier release order, hotplug, and cancel during rebinding. Avoid adopting game-specific whitelists or global interception from a case study without tracing the target input pipeline. [Sources: input manager](research-sources.md#spire-input), [controller action inventory](research-sources.md#spire-controller), [Against the Storm input blocker](research-sources.md#ats-input).
