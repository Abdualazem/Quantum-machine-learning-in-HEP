project = 'Quantum Machine Learning'
author = 'Abdualazem Fadol'
copyright = '2023, Abdualazem Fadol'

exclude_patterns = [
    "_build",
    "featureMap.ipynb",
    "PrepareData.ipynb",
    "README.md",
    "Variables.ipynb",
]
extensions = [
    "myst_nb",
    "sphinx.ext.githubpages",
]
html_theme = "sphinx_book_theme"
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "html_image",
]
nb_execution_mode = "cache"
