Contents
==
- [Contents](#contents)
- [SQL programming](#sql-programming)

<!--intro-start-->
# SQL programming
SQL (structured query language) is a programming language used to manage data stored in relational databases.

Below you can find some useful functions for Big Query:

| SQL Function           | Description                                                                                      | Example                                                      |
|------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **Aggregate Functions**|                                                                                                  |                                                              |
| `SUM(column)`          | Calculates the sum of values in a column.                                                         | `SUM(sales_amount) OVER(PARTITION BY region)`                 |
| `AVG(column)`          | Calculates the average of values in a column.                                                     | `AVG(sales_amount) OVER(PARTITION BY region)`                 |
| `COUNT(*)`             | Counts the number of rows in a result set or a group.                                              | `COUNT(*) OVER(PARTITION BY region)`                         |
| **Ranking Functions**  |                                                                                                  |                                                              |
| `ROW_NUMBER()`         | Assigns a unique sequential integer to each row within a partition of a result set.               | `ROW_NUMBER() OVER(PARTITION BY region ORDER BY month)`       |
| `RANK()`               | Assigns a unique rank to each row within a partition of a result set, with gaps allowed.          | `RANK() OVER(PARTITION BY department ORDER BY sales_amount DESC)` |
| `DENSE_RANK()`         | Assigns a unique rank to each row within a partition of a result set, without gaps.               | `DENSE_RANK() OVER(PARTITION BY department ORDER BY sales_amount DESC)` |
| `PERCENT_RANK()`       | Calculates the relative rank of each row within a partition as a percentage.                     | `PERCENT_RANK() OVER(PARTITION BY department ORDER BY sales_amount DESC)` |
| `CUME_DIST()`          | Calculates the cumulative distribution of rows within a partition, as a percentage.              | `CUME_DIST() OVER(ORDER BY sales_amount DESC)`                |
| **Window Frame Functions** |                                                                                              |                                                              |
| `LAG(column)`          | Retrieves data from a previous row in the result set.                                             | `LAG(sales_amount) OVER(PARTITION BY region ORDER BY month)`  |
| `LEAD(column)`         | Retrieves data from a subsequent row in the result set.                                            | `LEAD(sales_amount) OVER(PARTITION BY region ORDER BY month)` |
| **Date/Time Functions**|                                                                                                  |                                                              |
| `DATE_TRUNC(unit, date)`| Truncates a date/time value to a specified unit (e.g., DAY, MONTH).                              | `DATE_TRUNC(MONTH, order_date)`                               |
| `DATE_ADD(date, INTERVAL)` | Adds an interval to a date or datetime value.                                                   | `DATE_ADD(order_date, INTERVAL 7 DAY)`                        |
| `DATE_DIFF(end_date, start_date, unit)` | Calculates the difference between two dates in units such as DAY, WEEK, MONTH, etc.         | `DATE_DIFF(end_date, start_date, DAY)`                        |
| **Other Useful Functions** |                                                                                               |                                                              |
| `COALESCE(expr1, expr2, ...)` | Returns the first non-null expression among the arguments.                                     | `COALESCE(sales_amount, 0)`                                   |
| `QUALIFY`              | Filters rows based on a condition evaluated after window functions.                               | `QUALIFY ROW_NUMBER() OVER(PARTITION BY category_id ORDER BY sales_amount DESC) = 1` |
| `FIRST_VALUE(column)`  | Returns the value of the specified column from the first row in a window frame.                   | `FIRST_VALUE(sales_amount) OVER(PARTITION BY region ORDER BY month)` |
| `LAST_VALUE(column)`   | Returns the value of the specified column from the last row in a window frame.                    | `LAST_VALUE(sales_amount) OVER(PARTITION BY region ORDER BY month)`  |
| `NTH_VALUE(column, n)` | Returns the value of the specified column from the nth row in a window frame.                     | `NTH_VALUE(sales_amount, 3) OVER(PARTITION BY region ORDER BY month)` |

For a full list of functions you can check out the Big Query documentation: [here](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)