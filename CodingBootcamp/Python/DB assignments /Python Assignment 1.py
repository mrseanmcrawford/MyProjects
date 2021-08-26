import sqlite3

conn = sqlite3.connect('Roster.db')
c = conn.cursor()
c.execute('''CREATE TABLE CLIENTS ([Person_ID] INTEGER PRIMARY KEY, [Name] text,  [Species] text, [IQ] text)''')
c.execute(''' INSERT INTO TABLE Clients ('Jean-Baptiste Zorg','Human', '122'), ('Korben Dallas', 'Meat Popsicle', '100'), ('Aknot', 'Mangalore', '5')



