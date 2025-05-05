# Notify_not_updated() ➤ Notify user if no records were updated.

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
code=int(input("Enter the Employee code to made changes : "))
salary=int(input("Enter the Employee salary to be updated : "))

query="update emp set salary={} where code={}".format(salary,code)
cursor.execute(query)
con.commit()

if cursor.rowcount>0:
    print("Updated  Successfully")
else:
    print("No record found with the given code")


  
   
