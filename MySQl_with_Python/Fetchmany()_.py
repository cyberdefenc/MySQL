# Fetch_many()  ➤ Fetch specific number of records.

import mysql.connector as c
import os
from dotenv import load_dotenv

# 🔐 Load environment variables from .env file
load_dotenv()

# ✅ Establishing connection to MySQL using secure credentials
con = c.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Checking the connection
if con.is_connected():
    print("Successfully Connected...")
else:
  print("Connection Failed")


cursor=con.cursor()
cursor.execute("select * from emp")
data=cursor.fetchmany(5)
print(data)
print("Total nummber of rows- ",cursor.rowcount)

