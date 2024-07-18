Contents
==
- [Contents](#contents)
- [Auto-generating Documentation](#auto-generating-documentation)
- [MkDocs](#mkdocs)
- [Setting up MkDocs](#setting-up-mkdocs)
- [Configuring MkDocs](#configuring-mkdocs)

<!--intro-start-->
# Auto-generating Documentation
There are several tools available that can automatically generate documentation from:
- Docstrings
- Markdown files
- Jupyter notebooks

# MkDocs
MkDocs is a static site generator that can be used to create professional-looking documentation for Python projects.

# Setting up MkDocs

Installation: `pip install mkdocs`

Setup new project: `mkdocs new .`

Start a server and opens a browser window with the documentation: `mkdocs serve`

Shutdown server: `Ctrl + C`

Build a static site from the documentation files: `mkdocs build`

# Configuring MkDocs
The mkdocs.yml file which was created at setup can be configured to render the desired documentation. See the example file to get an idea.

- Docstrings: You need to create a markdown file specifying the path to the python script containing docstrings
- Markdown files: You need to move to the docs folder
- Jupyter notebooks: You need to move to the docs folder

<!--intro-end-->
