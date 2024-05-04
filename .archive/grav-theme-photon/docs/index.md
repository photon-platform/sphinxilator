<a href="https://photon-platform.net/">
    <img src="https://photon-platform.net/user/images/photon-logo-banner.png" alt="photon" title="photon" align="right" height="120" />
</a>


# photon ✴ THEME

## 0.1.1

---


> Foundation theme for the photon PLATFORM within Grav CMS

- [configuration](#configuration)
- [templates](#templates)
- [scaffolds](#scaffolds)
- [scss](#scss)
- [assets](#assets)
- [languages](#languages)

- [Getting Started](#getting-started)
- [Articles in Pages](#articles-in-pages)
- [License](#license)


# configuration
blueprints.yaml

fields:
- columns

Before configuring this theme, you should copy the `user/themes/photon/photon.yaml` to `user/config/themes/photon.yaml` and only edit that copy.

Here is the default configuration and an explanation of available options:

```yaml
enabled: true
dropdown:
  enabled: true
```

Note that if you use the admin theme, a file with your configuration, and named photon.yaml will be saved in the `user/config/themes/` folder once the configuration is saved in the admin.


# blueprints

```sh
blueprints
├── asset
│   └── file.yaml
├── article.yaml
└── default.yaml
```

### Article
article.yaml
extends: default
fields:
- content
  - columns
    - _content
      - header.title
      - header.subtitle
      - content
      - header.media_order
      - _ordering
        - ordering
        - order
    - _meta
      - _main
        - folder
        - route
        - name
        - header.author
        - header.collection.name
        - header.collection.showCount
        - header.collection.showMenu
        - header.content.items
        - header.child_type
      - _figure
        - header.figure.image
        - header.figure.title
        - header.figure.alt
        - header.figure.caption
        - header.figure.youtube
      - _gallery
        - header.gallery.show
        - header.gallery.images
          - .image
          - .title
      - _attachments
        - header.attachments
          - .file
          - .title
- options
  - _publishing
    - header.published
    - header.date
    - header.publish_date
    - header.unpublish_date
    - header.metadata
- advanced
  - columns
    - column1
      - overrides
        - header.dateformat
        - header.menu
        - header.slug
        - header.redirect
        - header.process
        - header.twig_first
        - header.never_cache_twig
        - header.routable
        - header.cache_enable
        - header.visible
        - header.debugger
        - header.template
        - header.append_url_extension
    - column2
      - routes_only
        - header.routes.default
        - header.routes.canonical
        - header.routes.aliases
      - admin_only
        - header.admin.children_display_order
        - header.order_by
        - header.order_manual
        - blueprint

### PLUGIN_ADMIN.DEFAULT
default.yaml
extends: 
fields:
- content
  - header.title
  - content
  - header.media_order
- options
  - publishing
    - header.published
    - header.date
    - header.publish_date
    - header.unpublish_date
    - header.metadata
  - taxonomies
    - header.taxonomy
- advanced
  - columns
    - column1
      - settings
      - folder
      - route
      - name
      - header.body_classes
    - column2
      - order_title
      - ordering
      - order
  - overrides
    - header.dateformat
    - header.menu
    - header.slug
    - header.redirect
    - header.process
    - header.twig_first
    - header.never_cache_twig
    - header.child_type
    - header.routable
    - header.cache_enable
    - header.visible
    - header.debugger
    - header.template
    - header.append_url_extension
  - routes_only
    - header.routes.default
    - header.routes.canonical
    - header.routes.aliases
  - admin_only
    - header.admin.children_display_order
    - header.order_by
    - header.order_manual
    - blueprint

# templates

```sh
templates
├── _articles
│   ├── _block
│   │   ├── article_footer
│   │   │   ├── aside_categories.html.twig
│   │   │   ├── aside_details.html.twig
│   │   │   ├── aside_members.html.twig
│   │   │   ├── aside_share.html.twig
│   │   │   ├── aside_tags.html.twig
│   │   │   └── list-featured-descendants.html.twig
│   │   ├── article_collection.html.twig
│   │   ├── article_data.html.twig
│   │   ├── article_figure_excerpt.html.twig
│   │   ├── article_figure.html.twig
│   │   ├── article_footer_excerpt.html.twig
│   │   ├── article_footer.html.twig
│   │   ├── article_gallery.html.twig
│   │   ├── article_header_excerpt.html.twig
│   │   ├── article_header.html.twig
│   │   ├── article_main_excerpt.html.twig
│   │   ├── article_main.html.twig
│   │   ├── article_nav.html.twig
│   │   └── breadcrumbs.html.twig
│   ├── article-excerpt.html.twig
│   └── article.html.twig
├── _asides
│   ├── contact.html.twig
│   ├── copyright.html.twig
│   ├── follow.html.twig
│   ├── list-categories.html.twig
│   ├── list-featured.html.twig
│   ├── list-recent.html.twig
│   ├── list-tags.html.twig
│   ├── list-taxonomy.html.twig
│   ├── motto.html.twig
│   └── org.html.twig
├── _json-ld
│   ├── article.html.twig
│   └── restaurant.html.twig
├── _macros
│   ├── collection.html.twig
│   └── figure.html.twig
├── modular
│   └── article.html.twig
├── _sections
│   ├── asides.html.twig
│   ├── footer.html.twig
│   ├── header.html.twig
│   ├── nav.html.twig
│   ├── nav-loop.html.twig
│   └── pagination.html.twig
├── _site
│   ├── analytics.html.twig
│   ├── css_vars.html.twig
│   ├── fonts.html.twig
│   ├── head-base.html.twig
│   ├── head.html.twig
│   └── meta.html.twig
├── article.html.twig
├── default.html.twig
├── error.html.twig
├── formdata.html.twig
├── form.html.twig
├── login.html.twig
└── README.md
```
<a href="https://photon-platform.net/">
    <img src="https://photon-platform.net/images/photon-logo-bg.png" alt="photon" title="photon" align="right" height="120" />
</a>

# photon ✴ THEME: templates

photon templates are created in TWIG - a templating language for Grav / Symfony / PHP platform.

There is great documentation on the TWIG website
https://twig.symfony.com/


## Files and Folders

- [`templates`]()
  root folder contains the page level templates
  - [`_site`](_site)
    partials for the head section of the templates
  - [`json-ld`](json-ld)
    partials for including JSOM Linked Data in head of template
  - [`_sections`](_sections)
    partials for the body sections of the templates
  - [`_articles`](_articles)
    partials for the structuring article content - full and excerpt
  - [`_asides`](_asides)
    partials for sidebar components

# scaffolds

```sh
scaffolds
└── article.md
```

# scss

```sh
scss
├── articles
│   ├── article
│   │   ├── _content.scss
│   │   ├── _data.scss
│   │   ├── _figure.scss
│   │   ├── _footer.scss
│   │   ├── _gallery.scss
│   │   ├── _header.scss
│   │   ├── _index.scss
│   │   └── _nav.scss
│   ├── _blocks
│   │   └── _gallery.scss
│   ├── mixins
│   │   ├── _article-banner.scss
│   │   ├── _article-card.scss
│   │   ├── _article-panel.scss
│   │   └── _index.scss
│   ├── _article-excerpt.scss
│   └── _index.scss
├── asides
│   ├── _aside.scss
│   ├── _index.scss
│   ├── _nav.scss
│   └── _search.scss
├── color
│   ├── _index.scss
│   ├── _mixins.scss
│   └── _social.scss
├── elements
│   ├── _a.scss
│   ├── _a-tooltip.scss
│   ├── _blockquotes.scss
│   ├── _blocks.scss
│   ├── _code.scss
│   ├── _figure.scss
│   ├── _forms.scss
│   ├── _headings.scss
│   ├── _html.scss
│   ├── _index.scss
│   ├── _inline.scss
│   ├── _lists.scss
│   ├── _reset.scss
│   └── _tables.scss
├── fonts
│   ├── _index.scss
│   └── _photon-icon.scss
├── media
│   ├── _functions.scss
│   ├── _index.scss
│   ├── _mixins.scss
│   └── _var-18em.scss
├── sections
│   ├── _asides.scss
│   ├── _footer.scss
│   ├── _header.scss
│   ├── _index.scss
│   └── _main.scss
├── templates
│   ├── article
│   │   ├── _article-roman.scss
│   │   └── _index.scss
│   ├── default
│   │   ├── _asides.scss
│   │   ├── _footer.scss
│   │   ├── _header.scss
│   │   ├── _index.scss
│   │   └── _main.scss
│   └── _index.scss
├── photon-print.scss
├── photon.scss
└── README.md
```
<a href="https://photon-platform.net/">
    <img src="https://photon-platform.net/images/photon-logo-bg.png" alt="photon" title="photon" align="right" height="120" />
</a>

# photon ✴ THEME: styles

styles are highly aligned with templates

plugins have their own source files

- default styling for all fundamental elements
- page level sections
- section componenents
- articles


## SCSS

component based styling

### master doc `photon.scss`
imports smaller compoenents


## Generating SCSS

photon projects can use the `swatch` alias to call `scss --watch` on all the scss source files

swatch will locate photon scss folders in themes and plugins and watch each for changes.

on photon SITE actions, type `s`

## Aligning Templates and Styles at each level

-

# assets

```sh
assets
├── fontello-6848bbf6
│   ├── css
│   │   ├── animation.css
│   │   ├── photon-icon-codes.css
│   │   ├── photon-icon.css
│   │   ├── photon-icon-embedded.css
│   │   ├── photon-icon-ie7-codes.css
│   │   └── photon-icon-ie7.css
│   ├── font
│   │   ├── photon-icon.eot
│   │   ├── photon-icon.svg
│   │   ├── photon-icon.ttf
│   │   ├── photon-icon.woff
│   │   └── photon-icon.woff2
│   ├── config.json
│   ├── demo.html
│   ├── LICENSE.txt
│   └── README.txt
└── highlight.css
```

# css

```sh
css
├── photon.css
├── photon.css.map
├── photon-print.css
└── photon-print.css.map
```

# js

```sh
js
├── article.js
└── pan-zoom.js
```

# languages

```sh
languages
└── en.yaml
```

# font

```sh
font
├── photon-icon.eot
├── photon-icon.svg
├── photon-icon.ttf
├── photon-icon.woff
└── photon-icon.woff2
```

## Installation

- all photon themes are installed as git submodules. More on that later.

## Usage

Select template type when creating a new page

## Credits


## To Do

- [ ] Future plans, if any




**TOC**
<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->


<!-- /code_chunk_output -->

![](screenshot.jpg)

## Getting Started
The best way to start with photon THEME is with a photon STARTER project. Checkout the repo here:

https://github.com/photon-platform/photon

Current version of this theme has some dependencies on  site level configurations. This will be resolved in a future version.

See the theme configuration section for more on the STARTER project:
https://github.com/photon-platform/photon#theme-configuration

I highly recommend reviewing the excellent material on GRAV Documentation site:
https://learn.getgrav.org/themes


## Articles in Pages

Photon takes a content first approach to development.

We develop our content as a set of hierarchical data.

An **Article** is a node in our dataset.

A **Page** is the template document that structures the content of one or more articles along with components to provide context and navigation.





## Templates
see README in templates folder for more about the concpets for the TWIG template files:

[`templates`](templates)


## Styles
see README in scss folder for more on the stylesheet development:

[`scss`](scss)



## License

See [LICENSE](LICENSE)


copyright &copy; 2020
