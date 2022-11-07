
from tkinter import *


win = Tk()

b1 = Button(win,text='One')
b2 = Button(win, text='Two')

"""
# pack makes buttons uppear and sides just placing button in the row
b1.pack(side=LEFT, padx=(10)#padx is to move buttons from each other(padding)
b2.pack(side=LEFT), padx=(10)
"""
b1 =Button(win,text="One")
i = Label(win,text='This is label')
i.grid(row=1, column=0)
b2 =Button(win,text='Two')
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

