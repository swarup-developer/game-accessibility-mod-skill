# How to Approach a Real Video-Game Mod

Read this when starting a game's first useful integration or when a mod loads but does not do the requested job. It combines published modding guides and a creator's detailed account of an accessibility project. These are source-informed procedures, not proof that a particular game's internals match another game's.

## Start with a supported way into the game

Identify the installed version, runtime, existing mod ecosystem, and the exact output the loader expects. Establish a minimal plugin that the loader actually discovers before writing a large accessibility framework. Then implement one real interaction that the player can use.

The BepInEx project tutorial covers plugin metadata, dependency/process declarations, game-library references, compiling, installation, and observing the startup message. Its separate Mono and IL2CPP paths matter. Follow the guide corresponding to the installed loader/runtime rather than copying one framework target or entry class into every game. The startup message establishes loading only; the requested action needs its own runtime check. [BepInEx: creating a plugin](https://docs.bepinex.dev/master/articles/dev_guide/plugin_tutorial/2_plugin_start.html).

The Stardew/SMAPI guide illustrates a different route: a game-specific mod entry point, manifest, subscribed input events, and a world-ready check before accessing a player. Its build configuration and framework target belong to that ecosystem. Transfer the principle of lifecycle-gated integration, not Stardew's classes or dependency versions, to another game. [SMAPI modder guide](https://stardewvalleywiki.com/Modding:Modder_Guide/Get_Started).

For another engine, inspect its official extension API or established loader first. Do not treat a game's genre or executable name as an engine/API contract.

## Trace one complete feature

For the requested behavior, identify the current input, owning screen/controller, real action method/event, eligibility conditions, resulting state, and accessible feedback. Document the evidence for that small path. A useful first menu feature lets the player find a control, read its state, activate it, and cancel/back out without triggering something else.

For movement, trace the player's actual controller and restrictions. A mod-loading example cannot establish safe auto-walk. Use [bindings and movement](bindings-and-movement.md) for action ownership, start/stop behavior, target navigation, and focus-loss cancellation.

Keep development helpers and temporary logs outside the game release. Deploy the intended artifact, check the loader's result, and exercise the interaction in the actual running game. A source file that exists but is never registered is still an unfinished feature.

## When a patch installs but never runs

Inspect the real call path before changing bindings or adding waits. Harmony's managed-runtime edge-case guide describes inlining, shared generic implementations, static initialization, missing IL for external methods, and patching Unity-related code too early. These can affect whether a hook is valid or ever executes. Check the specific method, runtime, and loader's Harmony/HarmonyX/interop version. The guide's standard managed-patching limits should not be blindly applied to an IL2CPP detour implementation. [Harmony edge cases](https://harmony.pardeike.net/v2/articles/patching-edgecases.html).

Use a narrow, debug-gated trace to distinguish registration from execution and execution from a successful game action. Do not patch unrelated callers simply because a broad search found similar names. If timing is the problem, establish the correct lifecycle event instead of adding an unexplained sleep.

## A detailed creator example: reading a game is not playing it

In his May 2026 One Piece TCG technical breakdown, Simon describes a browser accessibility extension whose information-reading side was more successful than its interaction side. He reports fragile DOM-position assumptions, visual-only controls, timing-dependent activation, and focus conflicts. He explicitly says he did not complete a full game using only the extension. This is a useful failure analysis, not a reusable API or a claim that every browser game is unmodifiable. [Technical breakdown](https://andadapt.com/making-one-piece-tcg-accessible-the-technical-breakdown/).

Apply the lesson by separating information access from action access. A board reader, spoken inventory, or dialogue announcement is valuable, but it does not establish that attack, use, confirm, and resolve actions work. Exercise the complete required player journey. Prefer stable semantic identities and actual action handlers over screen halves, positional indices, or fixed delays. Where those are unavailable, explain the limitation and investigate a better-supported integration route.

The companion story explains the motivation and the gap between hearing a game and being able to act in it. Read it for context; use the technical account and the target game's evidence for implementation decisions. [Creator's story](https://andadapt.com/making-one-piece-tcg-accessible-as-a-blind-player-the-story/).

## Speech speed is part of usability

In a separate post, the same creator discusses how punctuation and selectable verbosity changed the listening experience of card announcements. Those observations belong to his setup and project; pronunciation and pauses vary by synthesizer, settings, language, and context. [Verbosity and punctuation post](https://andadapt.com/em-dash-commas-full-stops-oh-my/).

Use a short core announcement and optional detailed review where the game needs it. Measure whether the user can understand and act before a timed decision expires. Do not shorten speech by silently discarding costs, disabled reasons, target identity, or other information needed for the decision. Verify the user's actual reader and voice rather than imposing a punctuation rule from a blog.

## Keep the conclusion proportionate

At each step, state what the evidence establishes: the loader found the mod, the input reached a handler, the action changed game state, speech was delivered, or the player completed the path. These are different milestones. An honest partial result helps the next investigation; an invented successful result sends it in the wrong direction.

Sources were read on 17 November 2026. Only original summaries and links are included here; the articles and third-party implementation code are not reproduced. The guides are version-sensitive, and the creator posts report one project's experience. See [the reading-list records](modding-reading-list.json).
