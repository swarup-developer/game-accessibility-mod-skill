# Technical Cautions for the Archived Library

Read before applying sample code or compatibility claims. These cautions qualify the historical examples; retain the archives for traceability.

## Loader and engine compatibility

Do not treat a fixed Unity-version cutoff in `known-issues.md` or `legacy-unity-modding.md` as a current support matrix. The inspected BepInEx installation documentation lists separate Mono, IL2CPP, and .NET Framework paths and advertises Unity 3 or newer, which conflicts with the template's blanket exclusion of Unity 4 and older. This does not establish support for every old title: verify the particular game, loader build, architecture, and runtime with primary documentation and logs.

Source: [BepInEx installation documentation](https://docs.bepinex.dev/master/articles/user_guide/installation/index.html), checked 2026-11-17. Its master documentation can describe a different release from a user's installation.

Do not infer x86/x64 solely from `Mono` versus `MonoBleedingEdge` directory names. Confirm binary headers and logs. Loader runtime labels, C# compiler language version, target framework, and Unity's runtime are related but distinct. A newer compiler does not make unavailable runtime APIs available.

The supplied project files are starting points with placeholders. Inspect references, available engine modules, loader major version, backend, and native dependencies. An absent TextMeshPro assembly should not break support for a legacy-text game. An IL2CPP plugin needs the appropriate interop references and entry point, rather than an unchanged Mono `Assembly-CSharp.dll` project.

## Native speech bindings

The inspected [Tolk header](https://github.com/dkager/tolk/blob/master/src/Tolk.h), blob `354618c0fbbd20c533ebc1333cd297cd129b8550`, declares a C ABI with `__cdecl`, native `bool`, and wide strings. Match calling convention, boolean marshalling, and Unicode strings in managed imports. In particular, one-byte boolean returns and parameters need the corresponding marshalling; a Windows four-byte BOOL declaration is a different ABI. Inspect the exact library version being distributed.

Tolk output is asynchronous. Success means the request was accepted, not that speech finished or was audible. `Tolk_IsSpeaking` is conditional on backend support, so false is not a universal completion signal. Avoid timers based on character count as a correctness mechanism for queued story text.

`Tolk_Load` and `Tolk_Unload` also affect COM on the calling thread. Keep lifecycle ownership deliberate and balanced. Reader detection, loaded state, speech capability, and successful output are separate checks. Do not promise Narrator, braille, SAPI fallback, or another backend unless that integration is configured and tested.

Local speech templates include changes around boolean marshalling, diagnostics, and reconnection, but the bundled copies have not been runtime-certified by creating this skill. Inspect them before reuse, including calling convention and thread behavior. Do not assume a fixed reprobe interval is required in a new project.

## Harmony and reflection

In Harmony, a false-returning prefix can skip the original method; observation patches should not accidentally change the game. Source: [Harmony prefix documentation](https://harmony.pardeike.net/v2/articles/patching-prefix.html), checked 2026-11-17. Validate behavior against the Harmony/HarmonyX version shipped by the actual loader.

For private base-class fields, inspect the declaring type and walk the hierarchy when needed. Cache metadata with a key that distinguishes declaring/runtime types and exact members. Check for ambiguous overloads and version changes. A missing field must remain distinguishable from an actual game value of zero or false.

Do not copy a helper's permissive null/default fallback into an announcement path that would present invented state. Use diagnostics and an honest unavailable message where state cannot be established. Reflection miss caching is appropriate only while the relevant type identity and assembly remain valid.

## Input and speech design disagreements

The archived documents disagree about mandatory position counters, repeat hotkeys, and other conventions. Derive these from the player's needs and actual interface. Native accessible controls and injected speech do not automatically expose identical review/history behavior.

Verify mod key availability rather than adopting sample F1/F12 bindings. A custom context stack should close the real game screen and track its result, not merely hide the mod's own context. Timed choices, slowing the game, or automatic movement are separate assists to discuss only when relevant to the requested scope.

## Build, scripts, and distribution

Some project templates copy the DLL directly into a game folder after building, retry locked copies, and downgrade copy failures to warnings. Remove or adapt that behavior when a project uses explicit staged deployment. Confirm the installed hash; build success does not prove replacement succeeded.

Bundled helpers can install Git hooks or inspect platform-specific paths. Review them before execution. The package does not grant permission to install loaders, overwrite game files, publish repositories, or release dependencies without the user's applicable authorization.

The original author's personal DLL paths are historical examples. Resolve dependencies on the current machine. Preserve attribution and each dependency's license; the template's documentation license is not a blanket license for Tolk, NVDA binaries, game assemblies, or the externally linked book.
