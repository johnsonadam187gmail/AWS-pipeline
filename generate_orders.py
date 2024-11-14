from dotenv import load_dotenv
import os
import logging
import sys
import random
import datetime
import decimal
from db_functions.queries import execute_query

logging.basicConfig(level=logging.INFO)

load_dotenv()
host = os.getenv("ENDPOINT")
dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("CREDS")
schema = os.getenv("SCHEMA")
table1 = "PRODUCTS"
table2 = "ORDERS"
port = 5432

# Generate random cutomer id and random product id
cust_id = random.randint(1, 10)
prod_id = random.randint(1, 10)
quantity = random.randint(1, 10)

# Get today's date (current date without time)
today = datetime.date.today()

# Generate a random time
random_hour = random.randint(0, 23) 
random_minute = random.randint(0, 59)  
random_second = random.randint(0, 59)  

# Create a datetime object for today with the random time
random_time = datetime.datetime.combine(today, datetime.time(random_hour, random_minute, random_second))


# Create query for customer
query1 = f"""SELECT price FROM {schema}.{table1} WHERE product_id = {prod_id};"""

result = execute_query(query1, user, password, host, port, dbname)

if isinstance(result[0][0], decimal.Decimal):
  result = float(result[0][0])
  print(result, type(result))
else:
  raise Exception(f"Incorrect value recieved for for price from query \n {query1}")



# Step 1: Generate the correct number of %s placeholders
placeholders = ', '.join(['%s'] * len(column_list))  # Creates '%s, %s, %s, ...' based on column_list length

# Check the length of column and value lists
if len(column_list) == len(value_list):
  query = f"""INSERT INTO {schema}.{table} ({', '.join(column_list)}) VALUES ({placeholders});"""
else:
  logging.error("Error: Number of columns does not match the number of values")





