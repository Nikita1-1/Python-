import sqlite3


FirstName = input('Enter your First Name: ')
LastName = input('Enter your Last Name: ')
age = int(input('Enter your age: '))
personData = (FirstName, LastName, age)

# execute insrt statements for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES (?,?,?)", personData)
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?,
              (45, 'Luidi','Vercotti'))



"""
For security reasons,
especially when you need to interact with a SQL table based on user-supplied input,
you should always use parameterized SQL statements.
This is because the user could potentially supply a value that looks like SQL code
and causes your SQL statement to behave in unexpected ways.
This is called a “SQL injection” attack and, even if you aren’t dealing
with a malicious user,it can happen completely by accident.

"""
