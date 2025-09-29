import pandas as pd

df = pd.read_csv('utils/data/employees.csv')
employeeRole = df.filter(items=['Designation'])
print(employeeRole)