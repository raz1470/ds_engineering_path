Contents
==
- [Contents](#contents)
- [Test-driven development](#test-driven-development)
- [Unit testing](#unit-testing)
- [Running the example](#running-the-example)

<!--intro-start-->
# Test-driven development
Test-driven development is when developers build tests to check the functional requirements of a piece of software before they build the full code itself. 

**There are 3 main groups of testing:**
- Unit tests - Focus on testing individual components or units of code in isolation
- Integration tests - Focus on verifying that multiple components or units of code work correctly together
- End-to-end tests - Examine the entire pipelines functionality from start to finish

# Unit testing
A popular testing framework in Python that covers unit testing is pytest.

```
# Function to tests
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Tests
def test_calculate_mean():
    # Test case 1: Basic test with positive numbers
    assert calculate_mean([1, 2, 3, 4, 5]) == 3.0

    # Test case 2: Test with a single number
    assert calculate_mean([10]) == 10.0

    # Test case 3: Test with a mix of positive and negative numbers
    assert calculate_mean([-2, 0, 2]) == 0.0
```

In most cases, for simple scenarios like the one demonstrated above, Pytest can discover and run your tests without requiring an explicit import of the pytest module.

# Running the example
Navigate to the location of this markdown file in the terminal and run the following command:

`pytest`

This will execute all tests in all files whose names follow the form test_*.py or \*_test.py in the current directory and its subdirectories.

<!--intro-end-->
