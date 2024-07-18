Contents
==
- [Contents](#contents)
- [Coding standards?](#coding-standards)
- [What is a linter?](#what-is-a-linter)
- [Analyse SQL file](#analyse-sql-file)
- [Fix the violations](#fix-the-violations)

<!--intro-start-->
# Coding standards?
Coding standards help improve code quality and readability. To be successful, everyone needs to follow the standards. It is worth noting that it is difficult to find one set of coding standards to follow for SQL, therefore devising your own standards following the following areas is suggested:

| Area | Considerations | 
| ---- | -------------- |
| Commenting | Using script headers, block comments, in-line comments help people understand what your code is doing |
| Indentation | Indenting code makes it easier to read |
| CTEs vs Sub-queries | CTEs make code more readable and in some cases are more efficient. |
| Upper case vs lower case | Keeping everything lowercase is a much easier standard to follow than using a mix of upper case and lower case |
| Columns and keywords | Snake-casing is easy to follow, avoid using keywords like date or month as column names |
| Joins and Aliases | Use explicit join statements, use aliases and make them something meaningful and easy to follow |

# What is a linter?
A linter allows us to set some coding standards and help Data Scientists adopt them.

**SQLFluff is an open source, dialect-flexible and configurable SQL linter:**
- Rules can be set in the .sqlfluff file.
- More info on setting up the config file can be found [here](https://docs.sqlfluff.com/en/stable/configuration.html)

# Analyse SQL file
Navigate to the location of this markdown file in the terminal and run the following command:

`sqlfluff lint sql_query.sql`

This will check and print any violations.

# Fix the violations
Navigate to the location of this markdown file in the terminal and run the following command:

`sqlfluff fix sql_query.sql`

This will fix any violations.

<!--intro-end-->
