
import sqlite3

conn = sqlite3.connect('test.db')


with conn: #while its connected to test.db and open we can add code(create tables etc) to it
    cur = conn.cursor()#accessing cursor object and call it cur so it is going to opperate when we give it any commnds
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_persons (\
        PersonID INTEGER PRIMARY KEY AUTOINCREMENT,\
        COL_Fname TEXT,\
        COL_Lname TEXT,\
        Col_Email TEXT)')
    conn.commit()
    
conn.close()


conn = sqlite3.connect('test.db')


with conn: #while its connected to test.db and open we can add code(create tables etc) to it
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_persons(COL_Fname, COL_Lname, Col_Email) VALUES(?,?,?)', \
                ('Bob', 'Smith', 'bob@gmail.com'))
    cur.execute('INSERT INTO tbl_persons(COL_Fname, COL_Lname, Col_Email) VALUES(?,?,?)', \
                ('Mary', 'Smith', 'mary@gmail.com'))
    cur.execute('INSERT INTO tbl_persons(COL_Fname, COL_Lname, Col_Email) VALUES(?,?,?)', \
                ('Greg', 'Smith', 'greg@gmail.com'))
    cur.execute('INSERT INTO tbl_persons(COL_Fname, COL_Lname, Col_Email) VALUES(?,?,?)', \
                ('Bill', 'Smith', 'bill@gmail.com'))
    cur.execute('INSERT INTO tbl_persons(COL_Fname, COL_Lname, Col_Email) VALUES(?,?,?)', \
                ('Andrew', 'Smith', 'adrew@gmail.com'))
    conn.commit()

conn.close()




conn = sqlite3.connect('test.db')

with conn: #while its connected to test.db and open we can add code(create tables etc) to it
    cur = conn.cursor()
    cur.execute('SELECT COL_Fname, COL_Lname, Col_Email FROM tbl_persons WHERE COL_Fname = "Mary"')
    varPerson = cur.fetchall()# takes all data and moves it into a variable because as sson as you exucute this and if you dont have variable the data will be gone
    for i in varPerson:
        msg = ('First Name: {}, \nLast Name: {}, \nEmail: {}'.format(i[0], i[1], i[2]))
    print(msg)
