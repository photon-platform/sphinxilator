# ROADMAP

This document outlines the development plan for `sphinxilator`, a centralized platform for building and managing documentation websites for the PHOTON platform.

## Phase 1: Create the Unified Theme

-   **[x] Initialize New Theme:** Create a new theme within `sphinxilator` that will serve as the foundation for the unified documentation platform.
-   **[x] Integrate `sphinx_rtd_theme`:**
    -   **[x] HTML Structure:** Use the HTML structure from `sphinx_rtd_theme` as the base for the new theme's templates (`layout.html`, `footer.html`, etc.).
    -   **[ ] Navigation:** Port the navigation logic from `sphinx_rtd_theme` to the new theme, ensuring it is robust and customizable.
    -   **[x] Search:** Integrate the search functionality from `sphinx_rtd_theme`, including its templates and JavaScript.
-   **[x] Integrate `grav-theme-photon` Styling:**
    -   **[x] SASS Build:** Set up a SASS build process for the new theme.
    -   **[x] Port Styles:** Port the SASS files from `grav-theme-photon` to the new theme, adapting them to the Sphinx HTML structure.
    -   **[x] Dark Theme:** Implement a high-quality dark theme based on the `grav-theme-photon` styles.
-   **[x] Integrate `photon-ablog`:**
    -   **[x] Post Lists:** Integrate `ablog`'s post list generation directly into the theme's navigation.
    -   **[ ] Search Integration:** Ensure that blog posts are indexed and searchable through the theme's search functionality.

## Phase 2: Extend Functionality & CLI

-   **[ ] Enhance Ablog:** Integrate the extended Ablog functionality to support different content types (e.g., events, tasks, updates).
-   **[ ] Create a CLI:** Develop a command-line interface for `sphinxilator` to manage documentation projects.
    -   **[ ] `new`:** Create a new documentation project.
    -   **[ ] `build`:** Build the documentation for a project.
    -   **[ ] `deploy`:** Deploy the documentation to GitHub Pages.
    -   **[ ] `organize`:** A tool to organize content, especially for code documentation.
        -   **[ ] Scan `src`:** Scan the `src` directory for Python modules and packages.
        -   **[ ] Generate RST stubs:** Automatically generate RST files for each module, using `sphinx.ext.autosummary`.
        -   **[ ] Enforce Standards:** Enforce documentation standards in both Python docstrings and RST files.
-   **[ ] Improve Theme:** Add more features to the Sphinx theme, such as:
    -   **[ ] Responsive Design:** Ensure the theme is fully responsive and works well on all devices.
    -   **[ ] Accessibility:** Improve the accessibility of the theme.

## Phase 3: Integration and Deployment

-   **[ ] Update `progenitor`:** Update the `progenitor` templates to use the latest `sphinxilator` features.
-   **[ ] Update Projects:** Update all PHOTON platform projects to use the new `sphinxilator` platform for their documentation.
-   **[ ] Update Deployment Workflow:** Update the `action-deploy-sphinx-gh-pages` GitHub Action to use the `sphinxilator` CLI.
-   **[ ] Documentation:** Create comprehensive documentation for `sphinxilator`, including tutorials and examples.