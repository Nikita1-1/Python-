

import sqlite3
connections = sqlite3.connect('test_database.db')

c = connections.cursor()#communication, instantiates a Cursor object.

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT")#This line creates a new table named People and inserts three new columns into the table


connections = sqlite3.connect(':memory:')#one-time-use database while you’re testing code or playing around with table structures,

with sqlite3.connect('test_database.db') as connection: # use the "with" keyword to simplify your code

#this will benefit you in a few important ways.
##no longer need to commit() changes you make; they’re automatically saved.
# Using "with" also helps to handle potential errors and frees up resources
# that are no longer needed - much like how we can open (and automatically
# close) files using the "with" keyword.


# you will still need to commit() a change if you want to see the result of that change immediately (before closing the connection).



# To run more than one line of SQL code at a time, there are a couple possible options. One simple option is to use the executescript() method and give it a string that represents a full script

import sqlite3
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(\
                    FirstName TEXT,\
                    LastName TEXT, \
                    Age INT \
                    );
                    INSERT INTO People (FirstName, LastName, Age) VALUES ('Ron', 'Obvious', '42');""")
    

# We can also execute many similar statements by using the executemany() method and supplying a tuple of tuples where each inner tuple supplies the information for a single command.

peopleValues = (('Luiqi','Veronica',43), ('Arthur', 'Belling', 26))

# We could then insert all of these people at once (after preparing our connection and our People table) by using the single line. Write and execute this code in IDLE:

c.executemany("INSERT INTO People(FirstName, LastName, Age) VALUES (?,?,?)", peopleValues)






