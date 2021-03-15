# Python MySQL
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost"
)

print(mydb)