from setuptools import setup


# gha-workflow-shellcheck
# Copyright (C) 2025 Ryan Finnie <ryan@finnie.org>
# SPDX-License-Identifier: MPL-2.0

__version__ = "0.0.1"


setup(
    name="gha-workflow-shellcheck",
    description="Runs shellcheck on GitHub Actions workflow steps",
    version=__version__,
    license="MPL-2.0",
    platforms=["Unix"],
    author="Ryan Finnie",
    author_email="ryan@finnie.org",
    scripts=["gha-workflow-shellcheck"],
    install_requires=["PyYAML"],
)
