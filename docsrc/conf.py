import os
import sys
from datetime import datetime
import ablog
import photon_platform.sphinxilator as sphinxilator

# -- Project information -----------------------------------------------------

project = "sphinxilator"
copyright = f"{datetime.now().year}, phi ARCHITECT"
author = "phi ARCHITECT"

version = sphinxilator.__version__
release = sphinxilator.__version__

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
]

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

html_theme = "sphinxilator_theme"
html_theme_path = [sphinxilator.get_path()]
html_static_path = ["_static"]

html_context = {
    "display_github": True,
    "github_user": "photon-platform",
    "github_repo": "sphinxilator",
    "github_version": "main",
    "conf_py_path": "/docsrc/",
    "theme_navigation_depth": -1,
    "theme_display_version": False,
    "theme_prev_next_buttons_location": "both",
    "theme_collapse_navigation": False,
    "theme_includehidden": True,
    "theme_titles_only": False,
}

# -- ABlog Options -----------------------------------------------------------

blog_path = "log"
blog_title = "sphinxilator • Blog"
blog_baseurl = "https://photon-platform.github.io/sphinxilator"
post_date_format = "%y.%j-%H%M%S"
post_date_format_short = "%y.%j"

# -- Intersphinx -------------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.9", None),
    "sympy": ("https://docs.sympy.org/latest", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
}