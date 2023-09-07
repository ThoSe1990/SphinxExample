# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import yaml
import os


project = 'SphinxExample'
copyright = '2023, Thomas'
author = 'Thomas'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'breathe',
  'sphinx_js'
]
js_source_path = './../src/'

breathe_projects = {
  "SphinxExample": "./_build/doxygen/xml"
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'display_version': False
}

build_all_docs = os.environ.get("build_all_docs")
pages_root = os.environ.get("pages_root", "")

if build_all_docs is not None:
  current_language = os.environ.get("current_language")
  current_version = os.environ.get("current_version")

  html_context = {
    'current_language' : current_language,
    'languages' : [],
    'current_version' : current_version,
    'versions' : [],
  }

  if (current_version == 'latest'):
    html_context['languages'].append(['en', pages_root])
    html_context['languages'].append(['de', pages_root+'/de'])

  if (current_language == 'en'):
    html_context['versions'].append(['latest', pages_root])
  if (current_language == 'de'):
    html_context['versions'].append(['latest', pages_root+'/de'])

  with open("versions.yaml", "r") as yaml_file:
    docs = yaml.safe_load(yaml_file)

  if (current_version != 'latest'):
    for language in docs[current_version].get('languages', []):
      html_context['languages'].append([language, pages_root+'/'+current_version+'/'+language])

  for version, details in docs.items():
    html_context['versions'].append([version, pages_root+'/'+version+'/'+current_language])