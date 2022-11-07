

import sqlite3

peopleValues = (('Ron', 'Obvious', 32), ('Euginio', 'Bennachi', 39), ('Arthur', 'Koin', 19))


with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute('DROP TABLE IF EXISTS People')
    c.execute("CREATE TABLE People(FirstName TEXT,LastName TEXT, Age INT)")
    c.executemany('INSERT INTO People VALUES(?,?,?)',
                  peopleValues)


# select all first and last names from people over age 30

    c.execute('SELECT FirstName, LastName FROM People WHERE Age > 30')
    #for row in c.fetchall():#catching 30> it will catch al the names

    while True:
        row = c.fetchone()#catch one result at the time 
        if row is None:# The None keyword is the way that Python represents the absence of any value for an object.
            break
        print(row)


#This checks each time whether our fetchone() returns another row from the cursor, displaying the row
        #(if the data exists) and breaking out of the loop once we run out of results.
