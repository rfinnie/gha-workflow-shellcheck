# GitHub Actions workflow shellcheck

This script picks apart `run` job steps in GitHub Actions workflow files and runs `shellcheck` on them.
It honors the `shell` attribute and will pass it along to `shellcheck`.
It also turns [GitHub context variables](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs) such as `${{ matrix.version }}` into placeholders such as `${GITHUB_CONTEXT}{{ matrix.version }}`.
This is so `shellcheck` doesn't interpret it literally as a shell variable, but still sees *a* shell variable and hence will detect if, for example, it's within proper shell quoting.

It may be pulled in as a [pre-commit](https://pre-commit.com/) hook.
It should be tolerant of any YAML file passed to it, not just GitHub Actions workflow files, so it is safe to be registered as `types: [yaml]` with pre-commit.

```yaml
repos:
  - repo: "https://github.com/rfinnie/gha-workflow-shellcheck"
    rev: "v0.0.2"
    hooks:
      - id: "gha-workflow-shellcheck"
```

## License

This package is licensed under the terms of the Mozilla Public License v2.0.

This document is provided under the following license:

    SPDX-PackageSummary: gha-workflow-shellcheck
    SPDX-FileCopyrightText: Copyright (C) 2025 Ryan Finnie
    SPDX-License-Identifier: CC-BY-SA-4.0
