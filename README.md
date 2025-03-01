# GitHub Actions workflow shellcheck

This script picks apart `run` job steps in GitHub Actions workflow files and runs `shellcheck` on them.
It honors the `shell` attribute and will pass it along to `shellcheck`, and turns GitHub context variables such as `${{ matrix.version }}` into a placeholder such as `[GITHUB CONTEXT]{{ matrix.version }}` so `shellcheck` doesn't interpret it as a shell variable.

It may be pulled in as a [pre-commit](https://pre-commit.com/) hook.
