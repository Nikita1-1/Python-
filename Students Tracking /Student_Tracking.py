

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import students_gui
import students_func


class Students(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.resizable(width = True, height = True)
        self.master.geometry ('{}x{}'.format(550, 450))


        self.master.title('Students Information')
        self.master.configure(bg = '#463F3A')
        arg = self.master

        students_gui.load_gui(self)


if __name__ == '__main__':
    root = tk.Tk()
    App = Students(root)
    root.mainloop()
