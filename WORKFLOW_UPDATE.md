# Plan for Updating the GitHub Pages Deployment Workflow

This document outlines the plan to update the GitHub Actions workflow for deploying documentation to GitHub Pages. The goal is to replace the generic `photon-platform/action-deploy-sphinx-gh-pages` action with a dedicated CLI within `publish`. This will allow us to dogfood our own tooling and create a more streamlined, project-specific deployment process.

## 1. Create a `publish` CLI with `click`

We will build a command-line interface for `publish` using the `click` library, which is consistent with other projects in the `photon-platform`.

The CLI will be implemented in `src/photon_platform/publish/cli.py`.

The entry point in `pyproject.toml` will be updated to point to the `click` application.

## 2. Implement `build` and `deploy` Commands

The CLI will have two main subcommands:

### `publish build`

-   **Purpose:** To build the Sphinx documentation.
-   **Functionality:**
    -   Takes the path to the `docsrc` directory as an argument.
    -   Executes the Sphinx build process.
    -   Places the output in a specified build directory (e.g., `docs`).

### `publish deploy`

-   **Purpose:** To deploy the built documentation to GitHub Pages.
-   **Functionality:**
    -   This command will likely wrap the `ghp-import` tool or a similar library.
    -   It will take the path to the built documentation as an argument.
    -   It will push the contents of the build directory to the `gh-pages` branch of the repository.

## 3. Update the GitHub Actions Workflow

The `.github/workflows/action.yml` file will be modified to use the new `publish` CLI.

The updated workflow will look something like this:

```yaml
name: Build and Deploy Sphinx

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install .

    - name: Build documentation
      run: publish build docsrc

    - name: Deploy to GitHub Pages
      run: publish deploy docs
```

This approach will make the deployment process more transparent and easier to maintain, as the logic will be contained within the `publish` project itself.
