changelog
=========

0.2.2
-----
*2025-11-08*

**changed**

+ Refined theme styles and templates, removing unused files and streamlining the overall structure.
+ Implemented new breadcrumbs in article headers for improved navigation.
+ Pared down font weights to reduce load times and improve performance.
+ Replaced the aggressive CSS reset with a more modern, targeted approach.

0.2.1
-----
*2025-11-08*

**changed**

+ The SCSS compilation now generates expanded, readable CSS instead of compressed CSS. This improves debuggability of the styles.

0.2.0
-----
*2025-11-08*

**changed**

+ Refactored the Sphinx theme to align with the design and functionality of the original Grav theme.
+ Replaced the `ablog` extension with a custom `collection` directive to provide more flexible, time-based content listings for any page type.
+ Introduced a hierarchical content model, allowing pages to manage and display subordinate items.
+ Updated the theme templates to use a more semantic and modular HTML structure.
+ Integrated SASS for more maintainable and flexible styling.

0.1.2
-----
*2025-11-07*

**changed**

+ Refactored the `publish` tool to use a `click`-based command-line interface with `build` and `test` commands.
+ Standardized the theme name to `photon` and the main SASS file to `styles.scss`.
+ Consolidated all theme and Sphinx configurations into `global_conf.py` to simplify project-level `conf.py` files.
+ Made the build process context-aware, allowing it to be run from any directory within a git repository.
+ Integrated SASS compilation into the build process.
+ Removed the old, unused `theme` directory.

0.1.1
-----
*2025-11-07*

**fixed**

+ Resolved build issues with the Sphinx documentation by removing outdated and conflicting files from the `docsrc/modules` directory. This ensures a clean and successful build process.

0.1.0
-----
*2025-11-07*

**removed**

+ Removed the `sphinxilator_theme` and all its associated SCSS files, streamlining the project to focus on a single, unified theme provided by the `publish` tool. This change simplifies the theming architecture and removes legacy code.

0.0.4
-----
*2025-10-26*

**changed**

+ ...

0.0.3
-----
*2025-10-26*

**added**

+ Integrated `sphinx_rtd_theme` navigation, including toctree and sticky navigation.
+ Integrated `sphinx_rtd_theme` search functionality with a custom search page.
+ Added breadcrumbs and previous/next buttons for improved navigation.

0.0.2
-----
*2025-10-26*

**added**

+ Created a new, unified `publish_theme` to consolidate documentation styling.
+ Ported the basic HTML structure and templates from `sphinx_rtd_theme`.
+ Integrated the SASS styles and structure from `grav-theme-photon`.
+ Implemented a new semantic HTML layout (`<header>`, `<main>`, `<asides>`).
+ Established a simplified, dark-theme-first color palette.
+ Added a SASS build system to compile theme assets.
