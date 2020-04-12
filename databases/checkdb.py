import sqlite3

db = sqlite3.connect('contacts.sqlite')

name = input("enter the name of da person: ")

# statement = "SELECT * FROM contacts WHERE name = ?"
statement = "SELECT * FROM contacts WHERE name LIKE ?"

for row in db.execute(statement, (name,)):
    print(row)

db.close()
