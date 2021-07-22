from pathlib import Path

project = 'sphinx_test'
copyright = 'Public Domain'
author = 'Stefan Profanter'

release = '2.2.0'
version = '2.2'

extensions = [
    'breathe',
    'exhale',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
]

breathe_projects = { 'sphinx_test': '../doc_output/xml' }
breathe_default_project = 'sphinx_test'
exhale_args = {
    # These arguments are required
    "containmentFolder":     "./api",
    "rootFileName":          "library_root.rst",
    "rootFileTitle":         "Library API",
    "doxygenStripFromPath":  "..",
    # Suggested optional arguments
    "createTreeView":        True,
    "exhaleExecutesDoxygen": False,
}

exclude_patterns = []
master_doc = 'index'

source_suffix = {
    '.rst': 'restructuredtext',
}

root_doc = 'index'
highlight_language = 'cpp'
primary_domain = 'cpp'
