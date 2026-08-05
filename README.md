# Anki binary RPM

Unofficial Fedora RPM repository for stable [Anki](https://github.com/ankitects/anki)
releases. The package uses the official binaries published by Anki upstream and is
available for Fedora 44 on `x86_64` and `aarch64`.

## Install

```bash
sudo dnf copr enable ponesicek/anki-bin
sudo dnf install anki-bin
```

The package provides `anki` and conflicts with an installed `anki` RPM because both
packages install the same application files.

## Updates

The `Update from upstream` GitHub Actions workflow checks the latest non-prerelease Anki
release every six hours. When the version changes, it verifies that both Linux
architecture archives exist, updates the spec, submits both architecture builds to
[COPR](https://copr.fedorainfracloud.org/coprs/ponesicek/anki-bin/), waits for them to
succeed, and commits the version bump.

A push that changes the workflow, or a manual workflow run, rebuilds the current release.
This makes the first COPR build possible even when the spec already contains the latest Anki
version. Scheduled runs do nothing when the packaged version is current.

The workflow requires a repository secret named `COPR_CONFIG` containing the configuration
from the [COPR API page](https://copr.fedorainfracloud.org/api/).
