import sqlite3

connection = sqlite3.connect("pets.db")

cursor = connection.cursor()

rows = cursor.execute("select name, kind from pet, species where species_id = species.id")

print(rows) # Rows is an Cursor object(here object is an iterator, which gives values over, over and over again)

# we are converting them to a list

rows = list(rows)

for row in rows:
    (name,kind)=row # row is a tuple
    print(f"my {kind} is named {name}")

cursor.execute("delete from pet where species_id == 3")

connection.commit()

print("updated")

rows = cursor.execute("select name, kind from pet, species where species_id = species.id")

print(rows) # Rows is an Cursor object(here object is an iterator, which gives values over, over and over again)

# we are converting them to a list

rows = list(rows)

for row in rows:
    (name,kind)=row # row is a tuple
    print(f"my {kind} is named {name}")

