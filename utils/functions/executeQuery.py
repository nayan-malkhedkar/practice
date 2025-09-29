from main import conn

# Function to execute the query
def execute_query(query):
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    else:
        print("SQL failed!")
        return None
