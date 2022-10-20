

import os # The OS module provides the necessary functions
# To write Python code that correctly interacts with
# the OS on the  user's computer.




def write_data():
    data = 'Hello World'
    with open('d.py', 'a') as f:
        f.write(data)# so here is we are trying to write and add what we wrote in data variable
        #to the document d.py as f file. we make special instructions as 'a' which means
        # a - is write in the existing document and not overwrite next function
        f.close()

def open_file() :
    with open('d.py', 'r') as f:# here we are opening file within current directory with p/i.py file
        # and giving permision only to read the file 'r' and we want to call this operation as f
        # then we crete new variable with file f(d.py) and put if into data variable
        data = f.read()
        print(data)
        f.close()# close the f(d.py) file.




if __name__ == '__main__':
    write_data()
    open_file()
