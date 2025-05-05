# Connect_db() ➤ Establish connection to the MySQL database using credentials from .env

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

# ✅ Checking the connection
if con.is_connected():
    print("✅ Successfully Connected...")
else:
    print("❌ Connection Failed")

cursor = con.cursor()

# 🧾 Insert employee records in a loop
while True:
    code = int(input("Enter the Employee code: "))
    name = input("Enter the Employee name: ")
    salary = int(input("Enter the Employee salary: "))

    query = "INSERT INTO emp (code, name, salary) VALUES (%s, %s, %s)"
    cursor.execute(query, (code, name, salary))
    con.commit()
    print("✅ Record Inserted Successfully")

    print("1 -> To exit")
    print("2 -> To add more")
    x = int(input("Enter your choice: "))
    if x == 1:
        print("👋 Exiting...")
        break

