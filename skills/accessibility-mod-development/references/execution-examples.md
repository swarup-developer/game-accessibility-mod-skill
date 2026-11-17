# Completion and Research Examples

These are hypothetical work scenarios and acceptance examples. They are not claims that a feature was tested in Green Hell, Naruto, or any other named game. No example key, type, method, or timing is an API to copy into a project.

## 1. One requested control becomes twelve shortcuts

Request: "Add a key to read the current objective."

Apply: locate the game's current objective text, inspect existing controls, reuse or add one named action with a verified simple binding, connect its handler, and update help. Leave unrelated controls alone. If no suitable key is established, implement the action and report the specific binding choice still needed rather than allocating F1-F12 or inventing a chord.

Evidence: the configured key in the installed artifact reads the current objective once in the relevant context and leaves existing gameplay controls working.

## 2. A candidate key is already occupied

Request: "Put the new function on a convenient key." Inspection shows the first candidate already opens the game's map.

Apply: keep the map binding. Check another simple candidate against the actual game/mod controls and relevant OS/reader commands. Use a verified accessible menu if appropriate. Do not automatically substitute Alt+Space, Ctrl+something, or an arbitrary function key.

Evidence: one physical press performs the intended action in its context without opening the map, a system menu, or another mod feature. A candidate listed as free without evidence remains unverified.

## 3. A setting exists but the feature is disconnected

Request: "Enable auto-walk." The configuration flag is saved and help announces it, but no movement handler reads it.

Apply: trace configuration to registered action, active handler, actual movement interface, update/subscription lifecycle, and stop path. Complete the missing connection. Do not add another settings toggle to hide the missing behavior.

Evidence: the actual input starts the requested kind of movement; the chosen stop input and relevant context transitions stop it. "Auto-walk enabled" speech alone does not pass.

## 4. A movement method cannot be found

Request: "Walk to the selected object." Local source establishes the object identity but not a usable player movement/navigation API.

Apply: search the actual controller call sites and relevant mod/navigation API; use a narrow runtime probe if needed. Do not invent `Player.AutoWalkTo`, attach an unverified NPC navigator, or write player coordinates directly. Finish independent target selection or diagnostics where useful, while marking movement integration blocked by the missing interface.

Evidence: document the known target contract, exact missing movement evidence, work completed, and the smallest next investigation. Do not label the entire project impossible or the navigation feature finished.

## 5. Holding the toggle repeatedly flips it

Request: "Press the key once to keep walking." Implementation polls "key held" every frame and alternates active/inactive.

Apply: use the verified input system's appropriate edge/event semantics for a toggle. Check repeat, held-state reset, duplicate subscriptions, and scene lifecycle before adding a debounce timer.

Evidence: one press changes state once; keeping the key held does not flicker the state; a second deliberate press stops movement.

## 6. Movement continues after switching apps

Scenario: auto-walk leaves mod-owned held input active when the game loses focus.

Apply: trace focus loss, scene/menu transitions, shutdown, and input ownership. Cancel the feature and release only its own movement state through the correct interface. Returning to the game should not silently resume travel unless the requested design explicitly calls for it.

Evidence: focus loss and feature disable both stop mod-owned movement, and subsequent manual movement still works. A forward-direction log cannot establish that keys were released.

## 7. A key label changes but dispatch uses the old key

Request: "Change the feature's binding." The settings display changes, but the update loop still checks a hardcoded old key.

Apply: route dispatch and help through the effective binding/action; persist only the intended override. Check reload/restart if persistence is in scope. Preserve unrelated game overrides.

Evidence: the new key works, the old key stops invoking this feature, help names the active key, and settings survive the required restart.

## 8. Research expands without answering the problem

Scenario: one popup reads twice; the source already shows two registrations, but investigation keeps downloading menu frameworks.

Apply: remove or reconcile the evidenced duplicate registration, check its teardown/reopen behavior, then run the affected interaction. Consult external material only if a specific unresolved question remains.

Evidence: one popup occurrence produces one relevant announcement, reopening works, and another required event is not accidentally suppressed. Stop expanding the change after the requested behavior and relevant checks pass.

## 9. An example dependency is imported blindly

Scenario: a linked repository has a useful navigation class.

Apply: identify the exact transferable idea and verify the target's engine, game API, lifecycle, thread requirements, and license. Reuse the target's existing abstraction where it fits. Import code/dependencies only when necessary and compatible, preserving required notices; a link alone is not a reason to add an entire library.

Evidence: dependency resolution and the real requested interaction work in the target build. Another project's successful implementation is research evidence, not a test result for this game.

## 10. Compilation succeeds but installation is stale

Scenario: the build passes; copying the mod reports a locked file, and the old DLL remains installed.

Apply: report that deployment is incomplete, preserve the session, and replace the artifact once the game is safely closed under the existing authorization. Check installed version/hash and loader output. Do not say the new code is running.

Evidence: the installed artifact matches the intended build. Runtime and screen-reader behavior remain separate checks.

## 11. The user asks for "perfect" or "100% working"

Apply: make the acceptance path concrete, investigate actual failures, implement the complete requested behavior, and perform relevant checks. Do not respond with a confidence percentage, a larger unrequested feature list, or an endless investigation of hypothetical issues.

Evidence: state what changed, what was tested, and any material gap. For example, "Built and installed; the runtime trace confirms start and stop. Audible NVDA feedback still needs checking" is appropriate only when those observations actually occurred.

## 12. Only runtime access is missing

Scenario: source integration and build checks can be completed, but no game session is available.

Apply: finish the authorized code, integration review, build, documentation, and safe preparation that do not depend on that session. Give the exact small runtime test and expected outcome. Keep runtime validation outstanding; do not invent results or stop all independent work merely because one test needs the user.

Evidence: distinguish implemented, built, installed if applicable, runtime-observed, and user-confirmed stages. Never promote an untested stage to success.

For technical input and movement contracts, use [bindings and movement](bindings-and-movement.md). For deeper test selection, use [regression checks](regression-and-updates.md). These examples guide decisions; adapt them to the actual requested scope and evidence.
