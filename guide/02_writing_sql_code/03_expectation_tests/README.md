Contents
==
- [Contents](#contents)
- [What are Expectation Tests?](#what-are-expectation-tests)
- [Run expectations](#run-expectations)

<!--intro-start-->
# What are Expectation Tests?
Unit testing is testing small pieces of code in a pipeline. It is very common to see unit tests for Python code but not so common to see them for SQL code. In SQL, one way of "unit testing" is to run expectation tests on the table which a SQL script creates. This isn't strictly speaking unit testing, but you will often find people referring to it as unit testing.

**great_expectations is a Python library that provides a framework for describing the acceptable state of data and then validating that the data meets those criteria:**

| Expectation test |
| -----------------|
| expect_table_row_count_to_equal |
| expect_table_column_count_to_equal |
| expect_column_values_to_be_unique |
| expect_column_values_to_not_be_null |
| expect_column_values_to_be_between |
| expect_column_distinct_values_to_equal_set |

More info can be found [here](https://github.com/great-expectations/great_expectations)

# Run expectations
Navigate to the location of this markdown file in the terminal and run the following command:

`python3 expectation_tests.py`

This will check expectations and print the results.

<!--intro-end-->
