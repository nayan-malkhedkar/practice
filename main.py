import pandas as pd
from database.connect import get_connection
from database.queries import fetchAll

# Initiate database connection
conn = get_connection()

# Read excel data
df = pd.read_csv('utils/data/employees.csv')

# Filter based on first rows or headers of Excel sheet
employeeRole = df.filter(items=['Name','Designation'])

# Filter based on values of cells and display rows
employeeNoOffice = df[df['Office'].isna()]
employeeEngineer = df[df['Designation'].str.contains('Engineer')]
print(employeeEngineer)

# Pull data from database
if conn:
    cursor = conn.cursor()
    cursor.execute(fetchAll)
    rows = cursor.fetchall()
    print(rows)
else:
    print("SQL failed!")

if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees where Name = 'Nidhish';")
    rows = cursor.fetchall()
    print(rows)
else:
    print("SQL failed!")

# Always keep this line at the end of the code
conn.close()
