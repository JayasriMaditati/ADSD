import sqlite3

#DB-API

# Connection - ability to communicate with particular Database
connection = sqlite3.connect("pets.db")

# Cursor represents both connection and context( what we are doing, what kind of authority we managed to temporarily establish

cursor = connection.cursor()
# Cursor can maintain the status of what is going on DB, so cursor where can we can implement a transaction

try:
    cursor.execute("drop table pet") # Generally we name table with singular word
    cursor.execute("drop table species")

except:
    pass

cursor.execute("create table pet(id integer primary key, name text, species_id int)")

cursor.execute("create table species(id integer primary key, kind text)")

cursor.execute("insert into species (kind) values('dog')")
cursor.execute("insert into species (kind) values('cat')")
cursor.execute("insert into species (kind) values('fish')")

cursor.execute("insert into pet (name,species_id) values('dorothy','1')")
cursor.execute("insert into pet (name,species_id) values('muffin','2')")
cursor.execute("insert into pet (name,species_id) values('suzy','1')")
cursor.execute("insert into pet (name,species_id) values('angel','3')")

connection.commit()
connection.close()
print("Done")




