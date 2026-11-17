# Maintaining this package

The `skills/accessibility-mod-development` folder is the source of the shipped skill. Keep the short entry point focused and load detailed references only when the task needs them. Preserve attribution and source versions when adding research.

After changing a skill file, run:

```powershell
python scripts/package.py refresh
python scripts/package.py validate
python scripts/package.py build
```

`refresh` updates the inventory; it does not verify that a change is correct. `validate` checks the resulting package and its original-source hashes. The build writes a full installer ZIP, a skill-only ZIP, and checksums under `dist`.

Development tests exercised helpers, Windows installation/update/removal, and reproducible archives. The test harness and fixtures are maintained outside this public repository and are not included in the ZIPs. CI validates/builds on Windows and Linux and previews the Windows installer without changing the runner's skill folders. These checks are not live assistant or game tests. Completion examples are guidance for future model evaluations, not passing model-evaluation results.

## First publication

The repository includes `scripts/publish.ps1` for a new personal GitHub repository named `game-accessibility-mod-skill`. It checks GitHub CLI authentication, validates and builds the package, creates an isolated local Git repository, commits the package, creates the public repository, pushes it, and uploads the release ZIPs. Run it only when you intend to publish this package publicly.

```powershell
gh auth login
.\scripts\publish.ps1
```

Do not put passwords or tokens in files or command examples. The script uses the CLI's normal authentication. It stops if a remote already exists rather than guessing whether it can overwrite a repository. If creation succeeds but a later step fails, inspect the existing remote/release and complete the missing step manually.

For subsequent versions, update `VERSION` and `RELEASE_NOTES.md`, refresh and test the package, review the exact source being published, then push a matching `vX.Y.Z` tag. The release workflow validates the version/tag match and publishes the ZIPs using GitHub Actions' built-in repository token. No extra personal token is required by that workflow.

The workflow files are supplied but cannot be called verified remote runs until they have actually executed in GitHub Actions. Keep local checks, remote checks, agent evaluations, and real-game tests distinct in release notes.
