#!/usr/bin/env python
#
# esm_tools documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))




# PG: Here, we grab the main yaml for each model stated in configs, and get a metadata chapter:
import yaml

config_blacklist = ["batch_system", "machines", "vcs", "esm_master", "esm_runscripts", "general_yaml"]
configs = [f for f in os.listdir(os.path.abspath("../configs")) if f not in config_blacklist]
with open(os.path.join("../configs/esm_master/setups2models.yaml")) as setups2models:
    d = yaml.load(setups2models, Loader=yaml.FullLoader)
    components = d.get("components")
    configs = []
    for comp in components:
        if os.path.exists("../configs/"+comp+"/"+comp+".yaml"):
            configs.append(comp)
with open("Supported_Models.rst", "w") as rst:
    rst.write("================\n")
    rst.write("Supported Models\n")
    rst.write("================\n")
for config in configs:
    with open(os.path.join("../configs/", config, config+".yaml")) as f:
        d = yaml.load(f, Loader=yaml.FullLoader)
        metadata = d.get("metadata")
        with open("metadata/"+config+".csv", "w") as table:
            if metadata:
                for key in metadata:
                    if key=="Publications":
                        table.write("%s; `%s`_\n" % (key, metadata[key]))
                    else:
                        table.write("%s; %s\n" % (key, metadata[key]))
        with open("Supported_Models.rst", "a") as rst:
            rst.write("%s\n" % config)
            rst.write("-"*len(config) + "\n")
            rst.write(".. csv-table::\n")
            rst.write("   :file: %s\n" % ("metadata/"+config+".csv"))
            rst.write("   :delim: ;\n")
            rst.write("   :stub-columns: 1\n")
# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', "sphinx.ext.napoleon",
    'sphinx.ext.autosectionlabel'] 

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'ESM Tools'
copyright = "2020, Dirk Barbi"
author = "Dirk Barbi, Nadine Wieters, Paul Gierz, Fatemeh Chegini"
version = "3.1"
# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
#version = esm_tools.__version__
# The full version, including alpha/beta/rc tags.
#release = esm_tools.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "style_nav_header_background": "white",
    "logo_only": True,
    "prev_next_buttons_location": "both",
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "_static/ESM-TOOLS_LOGO_RGB_72dpi.jpg"

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'esm_toolsdoc'


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'esm_tools.tex',
     'ESM Tools r3 UserManual',
     'Dirk Barbi, Nadine Wieters, Paul Gierz, Fatemeh Chegini', 'manual'),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'esm_tools',
     'ESM Tools Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'esm_tools',
     'ESM Tools Documentation',
     author,
     'esm_tools',
     'One line description of project.',
     'Miscellaneous'),
]


# -- Options for labelling ---------------------------------------------

# This allows referencing different sections of the document by using 
# :ref:`rst_file_name:title of the section` avoiding problems with 
# duplicated sections across different rst files.
autosectionlabel_prefix_document = True



