Contents
==
- [Contents](#contents)
- [What are docstrings?](#what-are-docstrings)
- [Auto-generate docstrings](#auto-generate-docstrings)

<!--intro-start-->
# What are docstrings?
In Python docstrings are used to document functions or classes. Google is the most common docstring convention to follow. There are several tools which can be used to automatically generate documentation from docstrings - MKDocs is one option which is covered later in this project.

```
def add_numbers(a, b):
    '''
    Sum two numbers together

    Args:
        a (int): First input number
        b (int): Second input number

    Returns:
        int: The sumn of the inputs numbers
    '''
    return a + b
```

# Auto-generate docstrings 
Using the autoDocstring extension in VSC we can auto-generate docstrings.

To use this feature, place the cursor on the line right after the definition of a function, class, or method, then press Enter to create a new line.

On the new line, type ''' and press Enter again to generate the docstring.

<!--intro-end-->
