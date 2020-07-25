import sqlite3

first_name = 'f3'
last_name = 'l3'
age = '3'
gender = 'men'



db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS person_info (
         first_name TEXT,
         last_name TEXT,
         gender TEXT,
         age INTEGER
)""")

db.commit()

cursor.execute(
    f"INSERT INTO person_info VALUES(?,?,?,?)",
    (first_name, last_name, age, gender)
)

db.commit()

