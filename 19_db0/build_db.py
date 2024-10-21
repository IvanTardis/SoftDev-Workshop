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
students = csv.DictReader(file)

# for row in students:
#     print(row["name"])

c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")
for row in students:
    x = row["name"]
    y = row["age"]
    z = row["id"]
    c.execute(f"INSERT INTO students VALUES ('{x}', {y}, {z})")

# print(students)
command = "SELECT * FROM students"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement
result = c.fetchall()

print("STUDENTS:")
for row in result:
    print(row)


# HERE ARE THE COURSES

file2 = open('courses.csv', newline='')
courses = csv.DictReader(file2)

# for row in courses:
#     print(row["name"])

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
for row in courses:
    x = row["code"]
    y = row["mark"]
    z = row["id"]
    c.execute(f"INSERT INTO courses VALUES ('{x}', {y}, {z})")

# print(courses)
command2 = "SELECT * FROM courses"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command2)    # run SQL statement
result2 = c.fetchall()

print("\n\nCOURSES:")
for row in result2:
    print(row)


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


#==========================================================

db.commit() #save changes
db.close()  #close database
