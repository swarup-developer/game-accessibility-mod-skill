# Sources, Versions, and Reuse

Checked and bundled on 2026-11-17. These are reference snapshots; current releases and game internals still require verification when relevant.

## Licensed template library

- [VIPPotato/Accessibility-mod-template-Codex-edition](https://github.com/VIPPotato/Accessibility-mod-template-Codex-edition), commit `920da60f33b88addf3e665be5b1aab9f1a94a0e5`: complete English documentation, supplied German documentation, project-instruction snapshots, code starters, mod helper scripts, README, changelog, contribution document, and license.
- [HappyStarfish/Accessibility-mod-template](https://github.com/HappyStarfish/Accessibility-mod-template), commit `d75a087114b1f9a4b99d38d1e03c05e253a400f1`: differing documentation and extra German localization/menu checklists retained separately.
- Copyright (c) 2026 Happy Starfish. Attribution: Happy Starfish / Plueschyoda, the original template contributors, and VIPPotato for the Codex edition. The repository states [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); original notices are preserved in [the bundled license](template/LICENSE).
- Changes in this skill: new routing, workflow synthesis, narrative and runtime acceptance checks, technical cautions, indexed archival layout, and separately preserved local working copies. Renamed archived assistant-instruction filenames avoid making them active instructions for this skill's own files. Downloaded GitHub snapshots were verified against original blob IDs, including their original formatting.
- `references/local-project/` and `assets/local-project/` contain the current workspace versions, including uncommitted changes. They preserve the user's work; inclusion does not certify compilation or gameplay behavior. Paths in the inventory identify these local copies separately from downloaded sources.

The [source manifest](source-manifest.json) records repository, immutable ref, source path, blob ID, bundled path, and source URL for each GitHub file. The inventory records hashes of bundled files so an installation can be compared with this package.

## Linked external book

[The Book of Accessibility Modding by blal1 / Accessibility Modding Community](https://github.com/blal1/BOOK_OF_ACCESSIBILITY_MODING/blob/ef8e256559f53d740f5309dca6531d1f052a7639/BOOK_OF_ACCESSIBILITY.md), commit `ef8e256559f53d740f5309dca6531d1f052a7639`.

The inspected repository lists English/French books and a README without a license file. The template also flags its reuse status. The full book and its code are not bundled here. Reading and linking the book does not establish permission to republish it.

Concise technical takeaways: IL2CPP metadata establishes API shape without reconstructing method bodies. A focused context should own input. Speech needs an interruption policy and stale-output cancellation. Platform output benefits from a backend interface. These concepts still need implementation and testing against the target game and speech bridge. The skill's detailed guidance comes from the licensed template and independently checked primary interfaces; it does not reproduce the book's chapters.

## Primary technical checks

- [Tolk C header](https://github.com/dkager/tolk/blob/master/src/Tolk.h), inspected blob `354618c0fbbd20c533ebc1333cd297cd129b8550`: ABI, lifecycle, output, and speech-status contracts. The header identifies LGPLv3; no Tolk code or binary is bundled by this skill.
- [BepInEx installation documentation](https://docs.bepinex.dev/master/articles/user_guide/installation/index.html): engine/backend-specific installation routing and compatibility caveats.
- [BepInEx plugin guide](https://docs.bepinex.dev/master/articles/dev_guide/plugin_tutorial/index.html): route for plugin development tied to its documentation version.
- [Harmony prefix documentation](https://harmony.pardeike.net/v2/articles/patching-prefix.html): prefix skip behavior and observation/interception distinctions.

## Additional GitHub implementation research

The [research source register](research-sources.md) and [research manifest](research-manifest.json) cover targeted source/API inspection in Stardew Access, Say the Spire 2, Against the Storm Accessibility, Ren'Py, Godot documentation, Il2CppInterop, NVDA, Prism, and the official Unity Input System. Each cited GitHub file has an immutable source ref and blob ID. The expansion stores original guidance and source metadata, rather than copies of these projects' implementation code.

The [binding and movement guide](bindings-and-movement.md) adds eight inspected Unity Input System documents/sample files on current bindings, overrides, conflict scope, capture cleanup, persistence, and focus changes. It also cites the primary Windows menu, NVDA keyboard, and Unity destination-request contracts directly. These inform the workflow; they do not establish controls, player APIs, or working navigation in Green Hell, Naruto, or another uninspected game. The [twelve execution examples](execution-examples.md) are hypothetical acceptance scenarios, not fabricated runtime results.

The advanced guides separate observed source behavior from recommended adaptations and installed-version uncertainties. Development documentation is not a guarantee that an API exists in a released game or on the user's machine. No game from these case studies was installed or gameplay-tested as part of this research.

Revisit these sources for current compatibility or an exact API question. Do not download unrelated game code or dependencies merely because their links appear in a reference.
