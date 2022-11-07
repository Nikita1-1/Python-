

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

import Student_Tracking
import students_gui



def center_window(self,w,h):
    screen_width = self.master_winfo_screenwidth()
    screen_height = self.master_hinfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo


def create_db(self):
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            c_fname TEXT, \
            c_lname TEXT, \
            c_phone TEXT, \
            c_email TEXT, \
            c_current_course TEXT, \
            c_information TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students(c_fname, c_lname, c_phone, c_email, c_current_course) VALUES (?,?,?,?,?)""", ('Alex', 'Mercer', '111-111-1111', 'alex@google.com', 'C#'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur,count

def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT c_fname, c_lname, c_phone, c_email, c_current_course FROM tbl_students WHERE c_information = (?)""", [value])
        varBody = cur.fetchall()
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_current.delete(0,END)
            self.txt_current.insert(0,data[4])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_current = self.txt_current.get().strip()
    var_information = ('{}, {}, {}, {}'.format(var_fname, var_lname, var_phone, var_current))
    if not "@" or not "." in var_email:
        print("Incorrect email format!!!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_current) > 0):
        conn = sqlite3.connect('db_students.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(c_information) FROM tbl_students WHERE c_information = '{}'""".format(var_information))
            count = cursor.fetchone()[0]
            chkInformation = count
            if chkInformation == 0:
                cursor.execute("""INSERT INTO tbl_students(c_fname,c_lname,c_phone,c_email,c_current_course,c_information) VALUES (?,?,?,?,?,?)""",(var_fname, var_lname, var_phone,var_email, var_current, var_information))
                self.lstList1.insert(END, var_information)
                onClear(self)
            else:
                messagebox.showerror("Information Error","'{}' already exists in the database! Please choose a different info.".format(var_information))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror('Missing Text Error', 'Please ensure that there is data in all fields.')


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_students.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_students WHERE c_information = '{}'""".format(var_select))
                onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()


def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_current.delete(0,END)
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_current.delete(0,END)



if __name__ == "__main__":
    pass
