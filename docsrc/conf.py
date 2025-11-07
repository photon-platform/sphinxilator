import os
import sys
from datetime import datetime
import ablog
import photon_platform.publish as publish

# -- Project information -----------------------------------------------------

project = "publish"
copyright = f"{datetime.now().year}, phi ARCHITECT"
author = "phi ARCHITECT"

version = publish.__version__
# The full version, including alpha/beta/rc tags
release = publish.__version__

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.graphviz",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.youtube",
    "ablog",
    "myst_parser",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.footnotes",
    "sphinxext.opengraph",
    "sphinx_carousel.carousel",
    "sphinxcontrib.jquery",
]

autosummary_generate = True

templates_path = ["_templates", ablog.get_html_templates_path()]
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
master_doc = "index"
language = "en"
exclude_patterns = [".archive", ".docs", "tests", "*.egg-info"]
pygments_style = "gruvbox-dark"
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

html_theme = "publish_theme"
html_theme_path = [publish.get_path()]
html_static_path = ["_static"]

html_context = {
    "display_github": True,
    "github_user": "photon-platform",
    "github_repo": "publish",
    "github_version": "main",
    "conf_py_path": "/docsrc/",
    "theme_navigation_depth": -1,
    "theme_display_version": False,
    "theme_prev_next_buttons_location": "both",
    "theme_collapse_navigation": False,
    "theme_includehidden": True,
    "theme_titles_only": False,
    "theme_sticky_navigation": True,
}

ogp_site_url = "https://photon-platform.github.io/publish"
ogp_image = "https://photon-platform.github.io/publish/_static/logo.png"
ogp_social_cards = {
    "enable": True,
    "image_paths": ["_static/social_previews"],
}
ogp_custom_meta_tags = [
    '<meta property="og:description" content="A tool to streamline and enhance the Sphinx documentation framework." />',
]
ogp_github_url = "https://github.com/photon-platform/publish"
ogp_github_user = "phiarchitect"
ogp_github_repo = "publish"


# -- ABlog settings ----------------------------------------------------------
blog_path = "log"
blog_post_pattern = "log/**/index.rst"
blog_title = "publish • Blog"
blog_baseurl = "https://photon-platform.github.io/publish"

# -- Intersphinx -------------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.9", None),
    "sympy": ("https://docs.sympy.org/latest", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
}