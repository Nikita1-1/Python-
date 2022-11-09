
'''

Python Ver : 3.10.8


Author: Nikita Sazonov



Purpose: Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
         Using Tkinter Parent and Child relationships.



Tested OS: This code as written and tested to work with macOS Monterey Version 12.6


'''


from tkinter import *
import tkinter as tk
from tkinter import messagebox

import phonebook_gui
import phonebook_func


class ParentWindow(Frame): #Frame is tkinter frame that our class will inherit
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500, 300)#(Height & Width)
        self.master.maxsize(500, 300)

        #CenterWindow method will center the app on the user's screen
        # And if you dont pass the attribute SELF it means you can use this parametrs for W and H
        phonebook_func.center_window(self,500,300)# we want to access this phonebook_func from another file thats why we imported it
        self.master.title('The Tkinter Phonebook')
        self.master.configure(bg = '#F0F0F0')
        #this protocol method is a tkinter build-in method to catch if
        #the user clicks the upper corner, "x" on on OS.
        self.master.protocol('WN_DELETE_WINDOW', lambda:phonebook_func.ask_quit(self))
        arg = self.master


        #load in the GUI widgets from a separate module
        #keep the code comparmentalized and clutter free
        phonebook_gui.load_gui(self)#self is the ParentWindow func that is actually giving us permission to access the info that is in the function 


        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)


        self.master.config(menu=menubar, borderwidth='1')

         

if __name__=='__main__':
    root = tk.Tk()# syntax to open the window from tkinter
    App = ParentWindow(root)
    root.mainloop()# the app is firing itself in case to stay open.
