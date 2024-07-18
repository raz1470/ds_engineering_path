
import pandas as pd
import ydata_profiling

# import sql table
df1 = pd.read_csv("sample_data_01.csv")

# create data quality report
report_name = 'data_quality_report'
report = df1.profile_report(title=f'{report_name}', interactions=None, correlations=None, missing_diagrams=None, samples=None)
report.to_file(output_file=f'{report_name}') 
