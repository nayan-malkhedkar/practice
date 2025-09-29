from database.connect import get_connection

# Function to execute the query
def execute_query(query):
    # Initiate database connection
    conn = get_connection()

    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    else:
        print("SQL failed!")
        return None
