# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from pathlib import Path
import sys


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "msk_cdm"
copyright = "2023, MSK Clinical Data Mining Group"
author = "MSK Clinical Data Mining Group"
release = "0.1.0"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

templates_path = ["_templates"]
exclude_patterns = []

sys.path.append(Path(__file__).parents[2].resolve())


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]


# alabaster customizations

html_theme_options = {
    "github_repo": "clinical-data-mining/msk_cdm",
    "description": "Core MSK CDM code",
    "page_width": "1200px",  # default 940px
    "sidebar_width": "300px",  # default 220px
}
