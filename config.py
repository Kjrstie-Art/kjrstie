# The theme to use for HTML and HTML Help pages. 

html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]



# -- Options for HTML output ---------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "default"
try:
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"
    del sphinx_rtd_theme
except ModuleNotFoundError:
    pass

