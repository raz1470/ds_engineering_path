/*---------------------------------------------------------------------------------------------------------------------
 Script Name: sql_query_backup.sql
 Description: This script is for testing SQLFluff
 Parameters:
- param_01 = xxx
- param_02 = yyy
- param_03 = zzz
 ----------------------------------------------------------------------------------------------------------------------
 Date:          Changed by:     Version:        Description:
 ----------------------------------------------------------------------------------------------------------------------
 30/10/2023     Ryan OS         1.0             Initial script created
*/---------------------------------------------------------------------------------------------------------------------

select customer_id,
Time_Since_Last_Purchase
    ,SUM(CONVERSION) conversions
 FROM database_01.table_01
Where 1=1
 and PreviousPurchases >= 10
AND Previous_SPEND < 10000
        and AGe < 90
group by
customer_ID;