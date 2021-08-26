import sqlite3
connection = sqlite3.connect("/Users/seancrawford/MyProjects/Coding Bootcamp/Python/Databases/test_database.db")

c = connection.cursor()

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()

