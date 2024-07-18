Contents
==
- [Contents](#contents)
- [Data Quality reports](#data-quality-reports)
- [Run data quality report](#run-data-quality-report)

<!--intro-start-->
# Data Quality reports
To validate a SQL script meets the requirement we should carry out a data quality step based on the table created by the script. Rather than each Data Scientist writing their own bespoke data validation code, it is more efficient and effective to use a consistent approach.

**ydata-profiling is a python package which can profile data in one line of code, it allows us to check things like:**
- Is there a column with unique values?
- Is there a column with some NULL values?
- Is there a column with a constant value?
- Does the distribution of a column match our expectation?
- Do min and max values of a column match our expectations?

More info can be found [here](https://docs.profiling.ydata.ai/4.6/)

# Run data quality report
Navigate to the location of this markdown file in the terminal and run the following command:

`python3 data_quality_report.py`

This will create a html file with the data quality results.

<!--intro-end-->
