import psycopg2 # type: ignore
from psycopg2 import sql # type: ignore

def execute_query(query, user, password, host, port, dbname=None, params=None):
    # Set up the connection parameters
    conn_params = {
        'dbname': dbname,
        'user': user,
        'password': password,
        'host': host,
        'port': port
    }
    try:
        # Establish the connection
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(query, params)

        # Fetch the results if it's a SELECT query
        if query.strip().upper().startswith('SELECT'):
            result = cursor.fetchall()
            return result
        else:
            # Commit if it's an INSERT/UPDATE/DELETE
            conn.commit()
            return None
    except Exception as e:
        print(f"Error executing query: {e}")
        raise
    finally:
       if conn is not None:
        # close connection
        cursor.close()
        conn.close()
        print("Connection closed")
      
#TODO create query loop for execution without connect and close each time
    


def close_connection(conn, cursor):
  # Function to close connections requires conn and cursor
  if conn is not None:
    cursor.close()
    conn.close()
    print("Connection closed")
