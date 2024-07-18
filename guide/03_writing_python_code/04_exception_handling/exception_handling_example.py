
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