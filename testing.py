from db_functions import table_values
from dotenv import load_dotenv
import os
import logging
import psycopg2
import sys

logging.basicConfig(level=logging.INFO)

load_dotenv()
host = os.getenv("ENDPOINT")
dbname = os.getenv("DBNAME")
dbuser = os.getenv("USER")
dbcreds = os.getenv("CREDS")
schema = os.getenv("SCHEMA")
table = os.getenv("TABLE")
port = 5432

column_list = table_values.call_cust_table()
value_list = ["Adam", "Johnson", "adam.johnson@test.test", "20120652159",  "SylvanAve", "Auckland", "Auckland", "0627"]

# Step 1: Generate the correct number of %s placeholders
placeholders = ', '.join(['%s'] * len(column_list))  # Creates '%s, %s, %s, ...' based on column_list length

# Check the length of column and value lists
if len(column_list) == len(value_list):
  query = f"""INSERT INTO {schema}.{table} ({', '.join(column_list)}) VALUES ({placeholders});"""
else:
  logging.error("Error: Numbner of columns does not match the number of values")

print(query)

try:
  conn = psycopg2.connect(host=host, dbname = dbname, user=dbuser, password=dbcreds, port=port)
  cursor = conn.cursor()
  cursor.execute(query, value_list)
  conn.commit()
  logging.info(f"The query was committed to the database: \n {query} ")
except Exception as error:
    print("Error while connecting to PostgreSQL:", error)
    sys.exit(1)
finally:
    # Close the cursor and the connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Connection closed.")


