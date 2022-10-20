

import sqlite3



conn = sqlite3.connect('challange.db')# creating db in sqlite

with conn:
    cur = conn.cursor()# cursor needs for execution
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_challenge (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        COL_FILES TEXT)')# created table and clumn
    conn.commit()#commit to create
    

conn = sqlite3.connect('challange.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'myMovie.npg', 'Word.txt', 'data.pdf', 'myPhoto.jpg')# created tuple with file names

for x in fileList:# loop for that will go through all names in the tuple and
    # will find the ones that i need
    if x.endswith('.txt'): # method that will find files with .txt extensions
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_challenge(COL_FILES) VALUES(?)',(x,))#insert found files inside the column 
            print(x)

conn.close()
