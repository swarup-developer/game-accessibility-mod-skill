# Speech Backends, Capabilities, and Recovery

Read when selecting a bridge, diagnosing silent output, handling multiple readers, or implementing a speech queue. Keep game-state access separate from native speech calls.

## Represent capabilities and state separately

Track library load, selected backend, initialization, runtime availability, supported operations, and last output result. Speech, braille, combined output, cancellation, and speaking-status queries are different capabilities. A system TTS engine being available does not prove a screen reader is running.

The inspected Prism API distinguishes operation support, runtime availability, and screen-reader versus synthesis backends. Availability remains advisory: initialization/output can still fail. Feature queries can perform system probes; avoid polling them for every label. Re-query availability when relevant and invalidate cached capability data after backend replacement. [Source: Prism backend contracts](research-sources.md#prism-backends).

Offer automatic selection and a manual backend override only where useful to the project. Report the actual selected backend. Preserve a documented fallback policy instead of silently falling through to clipboard or multiple voices. Existing mods demonstrate backend selection; their fallback order is an example, not a universal preference. [Source: Say the Spire speech manager](research-sources.md#spire-speech).

## Match the exact native interface

Pin the native library build and binding/header revision together. Check exports, calling convention, string encoding, boolean width, integer widths, `size_t`, configuration layout, pointer ownership, and error enums. Avoid importing configuration structs or error numbers from a different mod's vendored version.

The inspected Prism header uses a C calling convention and UTF-8 text contracts; configuration fields evolve with structure versions. Where supported by the exact binary, default initialization may avoid a handwritten configuration struct. If configuration is needed, use the matching documented initializer/layout. [Sources: Prism header](research-sources.md#prism-header), [configuration](research-sources.md#prism-context), [conventions](research-sources.md#prism-conventions).

Verify Unicode names, accented text, non-Latin text, empty strings, and long text. Do not apply a Tolk UTF-16 binding to a UTF-8 interface. Preserve meaningful punctuation and mathematical signs when cleaning markup.

## Serialize ownership and shutdown

Prism registry thread safety does not imply individual backend thread safety. The inspected contract prohibits concurrent unsynchronized operations on the same backend; cached acquisitions can share the underlying instance across handles. Availability/audio callbacks can run on library threads. [Source: Prism thread-safety contract](research-sources.md#prism-threading).

Choose explicit ownership and dispatch for a project's backend. Callback code should enqueue an event for the appropriate owner rather than reading game objects or shutting down the context directly. Avoid holding locks across foreign callbacks or synchronous speech calls without examining reentrancy.

On shutdown/reload, stop accepting new requests, detach callbacks/subscriptions, quiesce in-flight work, and release each owned handle exactly once using the matching API. The documented Prism free operation is not itself a guarantee that speech stops; stop explicitly when needed. Context and backend lifetimes are separate. [Source: backend lifetime](research-sources.md#prism-backends), [context lifetime](research-sources.md#prism-context).

## NVDA direct integration

NVDA Controller functions return Windows status codes: zero indicates success. These are not Tolk boolean returns. Match DLL architecture to the calling process, and distinguish unavailable NVDA from a missing export or unsupported RPC interface. [Source: controller documentation](research-sources.md#nvda-controller).

The inspected development documentation describes versioned interfaces. Treat newer functions as optional until verified against the installed client and NVDA. Do not make a new status query a startup requirement for readers that support basic speech.

The IDL states that SSML mark callbacks apply to synchronous `speakSsml`; asynchronous mode does not deliver those callbacks. Synchronous speech can wait until completion or cancellation, so keep it off the game's update thread. Retain managed callback delegates for their native lifetime and tear them down safely. [Source: controller IDL](research-sources.md#nvda-controller-idl).

Escape player/game text before embedding it in SSML. A completion callback or speaking-status result is not automatically a signal to advance dialogue, choose an option, or resume gameplay; preserve the player's control.

## Diagnose interrupted or duplicate speech

Correlate requests, backend selection, output status, context changes, and cancellations. Distinguish an application calling stop from the screen reader's own typing/navigation interruption settings. Stardew Access documents reader configuration as one possible source of interruption; reproduce it before changing the user's settings. [Source: Stardew feature notes](research-sources.md#stardew-features).

Test no reader at launch, reader started later, reader restart, backend switch, missing native library, unsupported optional feature, focus loss, and shutdown during pending output as relevant. Keep recovery bounded and intentional. Do not repeatedly replay an old story backlog after a reader reconnects.

Speech delivery, audible output, refreshable braille, and review history need separate acceptance checks. Use [advanced interaction](advanced-interaction.md) for optional information buffers and [regression checks](regression-and-updates.md) for repeatable scenarios.
