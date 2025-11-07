changelog
=========

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
