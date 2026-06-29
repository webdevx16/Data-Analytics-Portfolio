# import pandas as pd
# import pymysql
# connection = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='sriii2005',
#     database='internprep'
# )
# query = "SELECT * FROM RegionalData;"

# df = pd.read_sql_query(query, connection)
# print(df)

# df.to_csv('my_first_pipeline_output.csv', index=False)
# connection.close()

import pandas as pd
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='sriii2005',
    database='internprep'
)

query = "SELECT * FROM SalesStaff;"
df = pd.read_sql_query(query, connection)

total_sales = df['TotalRevenueGenerated'].sum()
avg_sales = df['TotalRevenueGenerated'].mean()
highest_sales = df['TotalRevenueGenerated'].max()

print("EXECUTIVE SALES ANALYTICS REPORT")
print(df)
print(f"Total Corporate Revenue: ${total_sales:,.2f}")
print(f"Average Revenue Per Manager: ${avg_sales:,.2f}")
print(f"Highest Corporate Revenue: ${highest_sales:,.2f}")

df.to_csv('sales_staff_analytics.csv', index=False)

connection.close()