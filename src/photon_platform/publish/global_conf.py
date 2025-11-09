"""
"""
import os
import sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'directives')))


def setup_globals(org, org_name, repo, repo_name):
    globals().update(
        {
            "org": org,
            "org_name": org_name,
            "repo": repo,
            "repo_name": repo_name,
            "blog_title": f"{org_name} • {repo_name}",
            "html_title": f"{org_name} • {repo_name}",
            "project": f"{org_name} • {repo_name}",
            "version": "",  # The short X.Y version.
            "release": "",  # The full version, including alpha/beta/rc tags.
            "copyright": f"{year}, {org_name}",
            "author": org_name,
            "blog_baseurl": f"https://{org}.github.io/{repo}",
            "html_base_url": f"https://{org}.github.io/{repo}",
            "html_baseurl": f"https://{org}.github.io/{repo}",
            "blog_authors": {"phi": ("phi ARCHITECT", None)},
            "html_context": {
                "display_github": True,
                "github_user": org,
                "github_repo": repo,
                "github_version": "main",
                "conf_py_path": "/docsrc/",
            },
            # Add other global settings that should be the same across all projects here.
        }
    )


year = datetime.now().year

#  blog_path = 'log'
#  blog_title = "PHOTON platform • ablog"

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
blog_baseurl = ""

#  html_base_url = 'https://phiarchitect.com'
#  html_baseurl = 'phiarchitect.com'

# Choose to archive only post titles. Archiving only titles can speed
# up project building.
# blog_archive_titles = False

#  blog_authors = {
#  "phi ARCHITECT": ("phi ARCHITECT", None),
#  }
# blog_languages = {
#    'en': ('English', None),
# }
# blog_locations = {
#    'Earth': ('The Blue Planet', 'https://en.wikipedia.org/wiki/Earth),
# }

# post_auto_excerpt = 1
# post_auto_image = 0
# post_redirect_refresh = 5
# post_show_prev_next = True

html_sidebars = {
    "**": [
        "about.html",
        "postcard.html",
        "navigation.html",
        "recentposts.html",
        "tagcloud.html",
        "categories.html",
        "archives.html",
        "searchbox.html",
    ],
}

# blog_feed_archives = False
# blog_feed_fulltext = False
# blog_feed_subtitle = None
# blog_feed_titles = False

# Specify custom Jinja2 templates for feed entry elements:
#     `title`, `summary`, or `content`
# For example, to add an additional feed for posting to social media:
# blog_feed_templates = {
#     # Use defaults, no templates
#     "atom": {},
#     # Create content text suitable posting to social media
#     "social": {
#         # Format tags as hashtags and append to the content
#         "content": "{ title }{% for tag in post.tags %}"
#         " #{ tag.name|trim()|replace(' ', '') }"
#         "{% endfor %}",
#     },
# }
# Default: Create one `atom.xml` feed without any templates
# blog_feed_templates = {"atom": {} }

# Specify number of recent posts to include in feeds, default is ``None``
# for all posts.
# blog_feed_length = None

# -- Font-Awesome Options -----------------------------------------------------

# ABlog templates will use of Font Awesome icons if one of the following
# is ``True``

# Link to `Font Awesome`_ at `Bootstrap CDN`_ and use icons in sidebars
# and post footers.  Default: ``None``
# fontawesome_link_cdn = None

# Sphinx_ theme already links to `Font Awesome`_.  Default: ``False``
# fontawesome_included = False

# Alternatively, you can provide the path to `Font Awesome`_ :file:`.css`
# with the configuration option: fontawesome_css_file
# Path to `Font Awesome`_ :file:`.css` (default is ``None``) that will
# be linked to in HTML output by ABlog.
# fontawesome_css_file = None

# -- Disqus Integration -------------------------------------------------------

# You can enable Disqus_ by setting ``disqus_shortname`` variable.
# Disqus_ short name for the blog.
# disqus_shortname = None

# Choose to disqus pages that are not posts, default is ``False``.
# disqus_pages = False

# Choose to disqus posts that are drafts (without a published date),
# default is ``False``.
# disqus_drafts = False

# -- Sphinx Options -----------------------------------------------------------

# If your project needs a minimal Sphinx version, state it here.
#  needs_sphinx = '1.2'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
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
    #  "sphinxcontrib.bibtex",
    "myst_parser",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.footnotes",
    #  "sphinx_revealjs.ext.screenshot",
    #  "sphinxcontrib.budoux",
    #  "sphinxcontrib.gtagjs",
    #  "sphinxcontrib.oembed",
    "sphinxcontrib.sass",
    "sphinxext.opengraph",
    "sphinx_carousel.carousel",
    "sphinxcontrib.jquery",
    "photon_platform.publish.directives.collection",
]

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
#  project = "PHOTON platform<br/>•<br/>logger"
#  copyright = "2022, phi ARCHITECT"
#  author = "phi ARCHITECT"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ""
# The full version, including alpha/beta/rc tags.
release = ""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%%B %%d, %%Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [".archive", ".docs", "tests", "*.egg-info"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "gruvbox-dark"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "photon"


# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'themes'))]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%%b %%d, %%Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "help_doc"


html_theme_options = {
    "display_version": False,
    "navigation_depth": -1,
    "prev_next_buttons_location": "both",
    "collapse_navigation": False,
    "includehidden": True,
    "titles_only": False,
    "sticky_navigation": True,
}

ablog_website = "../docs"
post_date_format = "%y.%j-%H%M%S"
post_date_format_short = "%y.%j"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.9", None),
    "sympy": ("https://docs.sympy.org/latest", None),
}

html_logo = "_static/logo.png"

#  html_context = {
#  "display_github": True, # Integrate GitHub
#  "github_user": org, # Username
#  "github_repo": repo, # Repo name
#  "github_version": "main", # Version
#  "conf_py_path": "/docsrc/", # Path in the checkout to the docs root
#  }

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    #  'special-members': '__init__',
    "undoc-members": True,
    #  'exclude-members': '__weakref__'
    "show-inheritance": True,
}

html_permalinks = True

#  bibtex_bibfiles = ['refs.bib']

# SASS options
sass_src_dir = 'themes/photon/static/scss'
sass_out_dir = 'themes/photon/static/css'
sass_filename = 'photon.scss'
sass_args = ['--style', 'expanded']
