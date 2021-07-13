# import Sqlite3
import sqlite3

# Establish dsa as DB name 
conn = sqlite3.connect('dsa.db')

# Establish DB layout/tables 
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_FileName)")
    conn.commit()
conn.close()

conn = sqlite3.connect('dsa.db')

# Insert data into table
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_Files(col_FileName) VALUES (?)", \
               ('myPhoto.jpg',))
    conn.commit()
conn.close()


conn = sqlite3.connect('dsa.db')


# tuple of documents
fileList_tuple = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
                
for x in fileList_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # The value doer each row will be one name out of the tuple therefore (x,)
            # wil denote a one element tuple for each name ending with txt
            cur.execute("INSERT INTO tbl_Files (col_FileName) VALUES (?)", (x,))
            print(x)
conn.close()
    
