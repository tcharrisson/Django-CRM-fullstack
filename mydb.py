# pip installed mysql coonector

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)
# prepare a cursor object
cursorObject = dataBase.cursor()

# creating a database
cursorObject.execute("CREATE DATABASE mydatabasedcrm")
print("database created")