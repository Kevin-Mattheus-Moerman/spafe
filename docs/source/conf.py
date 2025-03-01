# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../spafe/"))

# -- Project information -----------------------------------------------------

project = "🧠 SuperKogito/Spafe"
copyright = "2019-%s, Ayoub Malek" % datetime.now().year
author = "Ayoub Malek"
html_favicon = "_static/favicon_io/favicon.ico"

# The short X.Y version
version = "0.2.0"
# The full version, including alpha/beta/rc tags
release = "0.2.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.napoleon",
    "nbsphinx",
    "matplotlib.sphinxext.plot_directive",  # docstring examples
    "sphinx.ext.mathjax",
]

todo_include_todos = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"


html_theme_options = {
    "github_url": "https://github.com/superkogito/",
    "search_bar_text": "Search this site...",
    "google_analytics_id": "UA-133660046-1",
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field.html", "version-switcher", "navbar-icon-links"],
    "switcher": {
        "json_url": "_static/switcher.json",
        "version_match": version,
    },
    "external_links": [
        {"name": "Home", "url": "https://superkogito.github.io/index.html"},
        {"name": "Projects", "url": "https://superkogito.github.io/projects.html"},
        {"name": "Blog", "url": "https://superkogito.github.io/blog.html"},
        {"name": "About Me", "url": "https://superkogito.github.io/about.html"},
    ],
}

html_sidebars = {
    # "index.html": ["sidebar-nav-bs.html"],
    "**": [
        "sidebar-nav-bs.html",
    ],
}


blog_baseurl = "https://superkogito.github.io"
blog_title = "SuperKogito"
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "blog/*/*"
post_redirect_refresh = 1
post_auto_image = 0
post_auto_excerpt = 1

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
    "css/tree_graph.css",
    "css/social_media_sharing.css",
]


# intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "np": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "matplotlib": ("https://matplotlib.org/", None),
}

# nbsphinx
nbsphinx_execute = "never"

# extensions: matplotlib.sphinxext.plot_directive
plot_rcparams = {"figure.autolayout": True}
plot_formats = [("png", 75)]
plot_include_source = True
plot_template = """
{{ source_code }}

{%- for image in images %}
.. figure:: {{ build_dir }}/{{ image.basename }}.{{ default_fmt }}
{%- endfor %}
"""
