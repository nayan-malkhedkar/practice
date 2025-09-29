# Write all re-usable queries here

# Read all data from table <table_name>
table_name = "employees"
fetchAll = f"SELECT * FROM {table_name}"

# Fetch row with given name
def fetchEmployeeData(name):
    employee_data = f'SELECT * FROM employees WHERE employees."Name" LIKE \'{name}\';'
    return employee_data
