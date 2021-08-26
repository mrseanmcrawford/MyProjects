import sqlite3

# get poersonal data drom user
firstName = input("Enter yuour first name: ")
LastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

# execute insert statement fdor supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)
    
