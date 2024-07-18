Contents
==
- [Contents](#contents)
- [What is a virtual environment?](#what-is-a-virtual-environment)
- [Setting up a virtual environment](#setting-up-a-virtual-environment)
- [Activating a virtual environment](#activating-a-virtual-environment)
- [Installing dependencies](#installing-dependencies)
- [Using the virtual environment in Jupyter Notebooks](#using-the-virtual-environment-in-jupyter-notebooks)
- [Using a specific Python version](#using-a-specific-python-version)

<!--intro-start-->
# What is a virtual environment?
A Python virtual environment is a way to create an isolated and self-contained environment for your Python projects. This is particularly useful for data scientists and developers when working on multiple projects that may have different dependencies or require different versions of the same library.

**venv is a built-in module that helps you create isolated environments for your Python projects**

# Setting up a virtual environment
Go to the terminal in VSC, and run: `python -m venv venv`

# Activating a virtual environment
Go to the terminal in VSC, and run: `. venv/Scripts/activate`

# Installing dependencies
After activating the virtual environment, go to the terminal in VSC, and run: `pip install -r requirements.txt`

# Using the virtual environment in Jupyter Notebooks
Pip installing the `jupyter` package should allow you to use the virtual environment for notebooks.

This is already added to the `requirements.txt` file.

# Using a specific Python version
You can use pyenv to help manage python versions. It can be installed via powershell using the following command:

`Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"`

Before creating the vitual environment, make sure the desired version of python is installed:

`pyenv install 3.11.4`

Then set the python version:

`pyenv global 3.11.4`

Then set up your virtual environment as described earlier.