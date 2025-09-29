import pandas as pd
from database.queries import fetchAll, fetchEmployeeData
from utils.functions.execute import execute_query

# Read excel data
df = pd.read_csv('utils/data/employees.csv')

# Filter based on first rows or headers of Excel sheet
employeeRole = df.filter(items=['Name','Designation'])

# Filter based on values of cells and display rows
employeeNoOffice = df[df['Office'].isna()]
employeeEngineer = df[df['Designation'].str.contains('Engineer')]
print(employeeEngineer)

# Pull data from database
all_data = execute_query(fetchAll)
employee_data = execute_query(fetchEmployeeData("Nidhish"))

print(all_data)
print(employee_data)
