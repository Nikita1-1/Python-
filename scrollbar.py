
from tkinter import *


"""
Our last widget in the project
will let us have a menu of items to choose from.
A listbox is created with the following command (after opening a window).
The "height" parameter limits how many lines will show
The fourth entry doesn't show since the listbox is set to just three lines.
"""


win = Tk()
lb = Listbox(win,height=3)
lb.pack()
lb.insert(END,'first entry')
lb.insert(END, 'second entry')
lb.insert(END, 'third entry')
lb.insert(END, 'fourth entry')



"""
Items in the listbox may be also inserted not only at the end (END)
but also at the beginning or even the middle. They may also be deleted.
In fact we'll use the command “lb.delete(0,END)” later to clear the listbox.

A listbox may be used in conjunction with a scroll bar. Let's start by making
a scroll bar and packing it next to the list box.
"""


sb = Scrollbar(win,orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)

"""
The scroll bar and the list box need to know about each other.
This is done in a manner similar to how we tied buttons to call back functions.
Two calls are needed, one to tell each about the other.

"""

sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

"""
If you have selected an item in the listbox, the method "curselection"
will return the selected item for you. Actually,
it returns a tuple of items selected. It is possible to configure the listbox
to allow multiple items to be selected together.
An empty tuple is returned if no item is selected.
"""

lb.curselection()
