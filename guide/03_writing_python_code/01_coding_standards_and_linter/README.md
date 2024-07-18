Contents
==
- [Contents](#contents)
- [Coding standards?](#coding-standards)
- [PEP-8](#pep-8)
- [Black](#black)
- [Analyse Python file](#analyse-python-file)
- [Fix the violations](#fix-the-violations)

<!--intro-start-->
# Coding standards?
Coding standards help improve code quality and readability. To be successful, everyone needs to follow the standards.

# PEP-8
PEP-8, which stands for Python Enhancement Proposal 8, is a style guide for writing clean, readable, and consistent Python code. Some of the key standards are covered below:

| Area | Standard | 
| ---- | -------------- |
| Indentation | Use 4 spaces per indentation level. |
| Whitespace | Avoid unnessecary whitespace. |
| Imports | Imports should usually be on separate lines, and you should avoid wildcard imports. |
| Comments | Write comments sparingly, and make sure they add value to the code. Avoid inline comments, and prefer using docstrings for documenting functions and modules. |
| Naming conventions | Follow the naming conventions for variables, functions, and classes. Variable and function names should be lowercase, with underscores separating words. Class names should be in CamelCase. |

More info on PEP-8 can be found [here](https://peps.python.org/pep-0008/)

# Black
Black is a PEP-8 compliant python code formatter that will format your code to a standard format automatically.

More info on Black can be found [here](https://pypi.org/project/black/)

# Analyse Python file
Navigate to the location of this markdown file in the terminal and run the following command:

`black --diff messy_script.py`

This will check and print any violations.

# Fix the violations
Navigate to the location of this markdown file in the terminal and run the following command:

`black messy_script.py`

This will fix any violations.

<!--intro-end-->
