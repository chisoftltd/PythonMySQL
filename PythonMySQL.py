# Python MySQL

import pyodbc
conn_str = (r'Driver={SQL Server};'
            r'Server=DESKTOP-CHINWEU;'
            r'Database=Customer;'
            r'Trusted_Connection=yes;')
# cnxn = pyodbc.connect('Driver=SQL Server;Server= .\DESKTOP-CHINWEU;Database=Customer;Trusted_Connection=yes;')
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()
cursor.execute('SELECT name FROM master.dbo.sysdatabases')
for X in cursor:
  print(X)
print()

conn_str = (r'Driver={SQL Server};'
            r'Server=DESKTOP-CHINWEU;'
            r'Database=Customer;'
            r'Trusted_Connection=yes;')
# cnxn = pyodbc.connect('Driver=SQL Server;Server= .\DESKTOP-CHINWEU;Database=Customer;Trusted_Connection=yes;')
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Customer')
print(cursor)
for row in cursor:
  print(row)
print()
cnxn.close()