import psycopg2
from psycopg2 import sql
import logging



def update_db(host, dbname, dbuser, dbcredentials, port, schema, column, value):
  logging.basicConfig(level=logging.INFO)
  try:
    conn = psycopg2.connect(host=host, dbname = dbname, user = dbuser, password=dbcredentials, port=port)
    cursor = conn.cursor()

    query = """
    UPDATE """
  except:
    pass
