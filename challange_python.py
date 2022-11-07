

import sqlite3

peopleValues = (('Jean-Baptiste Zorg', 'Human', 122),('Korben Dallas', 'Meat Popsicle', 100), ("Ak'not", "Mangalore", -5))


with sqlite3.connect('db_roaster.db') as connection:
    c = connection.cursor()
    c.execute('DROP TABLE IF EXISTS Roaster')
    c.execute("""CREATE TABLE if not exists Roaster(\
                Name TEXT,\
                Species TEXT,\
                IQ INT \
                )""")

    c.executemany("INSERT INTO Roaster(Name, Species, IQ) VALUES(?,?,?)",peopleValues )

    c.execute("UPDATE Roaster SET Species = 'Human' WHERE Name = 'Korben Dallas' AND IQ<125")

    c.execute('SELECT Name, Species, IQ FROM Roaster WHERE Species = "Human"')


    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
