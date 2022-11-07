

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import Student_Tracking
import students_func

def load_gui(self):


    self.lbl_fname = tk.Label(self.master, text = 'First Name: ')
    self.lbl_fname.grid(row=0, column=0, padx=(30,0), pady=(10,0), sticky=N+W)
    self.lbl_lname = tk.Label(self.master, text = 'Last Name: ')
    self.lbl_lname.grid(row = 2, column = 0, padx=(30,0), pady=(10,8), sticky = N+W)
    self.lbl_phone = tk.Label(self.master, text = 'Phone Number: ')
    self.lbl_phone.grid(row = 4, column = 0, padx=(30,0), pady=(10,8), sticky=N+W)
    self.lbl_email = tk.Label(self.master, text = 'Email Address: ')
    self.lbl_email.grid(row = 6, column = 0, padx=(30,0), pady=(10,8), sticky=N+W)
    self.lbl_current = tk.Label(self.master, text = 'Current Course: ')
    self.lbl_current.grid(row = 8, column = 0, padx=(30,0), pady=(10,8), sticky=N+W)
    self.lbl_information = tk.Label(self.master, text = 'Info: ')
    self.lbl_information.grid(row = 10, column = 0, padx=(30,0), pady=(10,8), sticky=N+W)
    self.lbl_info = tk.Label(self.master, text = 'Students: ')
    self.lbl_info.grid(row = 0, column = 2, padx=(0,0), pady=(20,2), sticky=N+W)


    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text ='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_current = tk.Entry(self.master, text='')
    self.txt_current.grid(row = 9, column=0, rowspan=1, columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_information = tk.Entry(self.master, text='')
    self.txt_information.grid(row = 11, column=0, rowspan=1, columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
   

    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=0)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: students_func.onSelect(self,event))
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)


    self.btn_add = tk.Button(self.master, width = 12, height = 2, text ='Add', command=lambda: students_func.addToList(self))
    self.btn_add.grid(row = 12, column = 0, padx=(25,0), pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master, width =12, height=2, text='Delete', command=lambda: students_func.onDelete(self))
    self.btn_delete.grid(row = 12, column = 2, padx=(15,0), pady=(45,10), sticky=W)


    students_func.create_db(self)

if __name__ == '__main__':
    pass
