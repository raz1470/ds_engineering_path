Contents
==
- [Contents](#contents)
- [What is exception handling?](#what-is-exception-handling)
- [Why is it important?](#why-is-it-important)
- [Basic components](#basic-components)
- [Running the example](#running-the-example)

<!--intro-start-->
# What is exception handling?
Exceptions are unexpected events or errors that occur during the execution of a program. They can be caused by various factors such as incorrect user input, unexpected data, network issues, or programming errors. 

# Why is it important?
- Exception handling allows you to gracefully deal with errors without crashing the entire program.
- It helps maintain the program's stability and provides a way to recover from unexpected situations.
- Proper exception handling makes your code more robust and user-friendly.

# Basic components
- **Try block:** This is where you place the code that might raise an exception. If an exception occurs within the try block, it's caught by the corresponding except block.
- **Except block:** This block contains the code to handle the exception. It specifies what actions should be taken when a particular exception occurs.
- **Finally block (optional):** This block is used to define code that will be executed whether an exception occurs or not. It is typically used for cleanup operations.
- **Raising an error:** Raising an error will terminate to program - in most cases we will want to do this.

```
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please provide valid numbers for division.")
        raise
    else:
        print("Result of division:", result)
    finally:
        print("This block will always execute, whether there's an exception or not.")

# Example usage:
divide_numbers(10, 2)  # This will print the result of division and the finally block.
divide_numbers(10, 0)  # This will print the division by zero error message and the finally block.
divide_numbers("10", 2)  # This will print the type error message and the finally block and then raise an error.
```
# Running the example
Navigate to the location of this markdown file in the terminal and run the following command:

`python3 exception_handling_example.py`

<!--intro-end-->
