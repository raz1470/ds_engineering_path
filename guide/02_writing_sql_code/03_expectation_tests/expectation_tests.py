
import pandas as pd
import great_expectations as ge

# import sql table
df_sql_table_01 = pd.read_csv("sql_table_01.csv")
ge_sql_table_01 = ge.from_pandas(df_sql_table_01)

#set expectation functions
def expect_table_row_count_to_equal(df, row_count):
    
    temp_result = df.expect_table_row_count_to_equal(row_count)
    
    if temp_result["success"] == False:
        print(f"Failed: row count")
        print(temp_result)
    else:
        print(f"Passed: row count")
        
def expect_table_column_count_to_equal(df, column_count):
    
    temp_result = df.expect_table_column_count_to_equal(column_count)
    
    if temp_result["success"] == False:
        print(f"Failed: column count")
        print(temp_result)
    else:
        print(f"Passed: column count")

def expect_column_values_to_be_unique(df, column):
    
    temp_result = df.expect_column_values_to_be_unique(column)
    
    if temp_result["success"] == False:
        print(f"Failed: {column}")
        print(temp_result)
    else:
        print(f"Passed: {column}")
        
def expect_column_values_to_not_be_null(df, column):
    
    temp_result = df.expect_column_values_to_not_be_null(column)
    
    if temp_result["success"] == False:
        print(f"Failed: {column}")
        print(temp_result)
    else:
        print(f"Passed: {column}")        
        print(column)
        
def expect_column_values_to_be_between(df, column, min, max):
    
    temp_result = df.expect_column_values_to_be_between(column, min, max)
    
    if temp_result["success"] == False:
        print(f"Failed: {column}")
        print(temp_result)
    else:
        print(f"Passed: {column}")
        
def expect_column_distinct_values_to_equal_set(df, column, value_list):
    
    temp_result = df.expect_column_distinct_values_to_equal_set(column, value_list)
    
    if temp_result["success"] == False:
        print(f"Failed: {column}")
        print(temp_result)
    else:
        print(f"Passed: {column}")
        
# run expectations
expect_table_row_count_to_equal(ge_sql_table_01, 10)
expect_table_column_count_to_equal(ge_sql_table_01, 3)
expect_column_values_to_be_unique(ge_sql_table_01, "row_id")
expect_column_values_to_not_be_null(ge_sql_table_01, "row_id")
expect_column_values_to_be_between(ge_sql_table_01, "day_integer", 1, 7)
expect_column_distinct_values_to_equal_set(ge_sql_table_01, "colour", ["Blue", "Red"])
