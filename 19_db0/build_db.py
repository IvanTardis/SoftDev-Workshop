#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

file = open('students.csv', newline='')
xyz = csv.DictReader(file)

# for row in xyz:
#     print(row["name"])

c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")
for row in xyz:
    x = row["name"]
    y = row["age"]
    z = row["id"]
c.execute("INSERT INTO students VALUES (\"john\", 1, 2)")

# print(xyz)

result = c.fetchall()

# loop through the rows
for row in result:
    print(row)
    print("\n")

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

command = "SELECT * FROM students"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
