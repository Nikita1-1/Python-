
'''

Python Ver : 3.10.8


Author: Nikita Sazonov



Purpose: Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
         Using Tkinter Parent and Child relationships.



Tested OS: This code as written and tested to work with macOS Monterey Version 12.6


'''


from tkinter import *
import tkinter as tk


import phonebook_gui
import phonebook_func


class ParentWindow(Frame): #Frame is tkinter frame that our class will inherit
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(500, 300)#(Height & Width)
        self.master.maxsize(500, 300)

        #CenterWindow method will center the app on the user's screen
        # And if you dont pass the attribute SELF it means you can use this parametrs for W and H
        phonebook_func.center_window(self,500, 300)# we want to access this phonebook_func from another file thats why we imported it
        self.master.configure(bg = '#f0f0f0')
        #this protocol method is a tkinter build-in method to catch if
        #the user clicks the upper corner, "x" on on OS.
        self.master.protoccol('WN_DELETE_WINDOW', lambda:phonebook_fun.ask_quit(self))
        arg = self.master


        #load in the GUI widgets from a separate module
        #keep the code comparmentalized and clutter free
        phonebook_gui.load_gui(self)



if __name__=='__main__':
    root = tk.TK()# syntax to open the window from tkinter
    App = ParentWindow(root)
    root.mainloop()# the app is firing itself in case to stay open.
