

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

import phonebook_main
import phonebook_gui


def center_window(self, w, h):# w500 by h300 px
    screen_width = self.master.winfo_screenwidth()#sel.master is to get to primary window,
    # winfo_screenwidth()'tkinter method' is for to get actual user width(user screen dementions) to center window app on the screen
    screen_height = self.master.winfo_screenheight()
    #calculate x and y coordinates to paint the app centered on the users screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2)- (h/2))

    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))# get dementions to the form (on top of the screen)
    return centerGeo


#catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):#yse to close app
    if messagebox.askokcancel('Close Window', 'Okay to exite application?'):
        # This close app
        self.master.destroy()#if user clicked close window and said yes, the app will close
        os.exit(0)# after pp is closed this method maked sure that it is freez up the app, and theres no memory leaked


#============================================================

def create_db(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );')
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)#we passing this function into cur(permission) to make sure it continues do what is doing
        if count < 1:# if count is less than one, then create values in rows
            cur.execute("""INSERT INTO tbl_phonebook(col_fname, col_lname, col_fullname, col_phone, col_email) VALUES(?,?,?,?,?)""",('Nikita', 'Sazonov', 'Nikita Sazonov', '970-452-9902','sazonovn@gmail.com')) #col_fname, col_lname, col_year_of_birth, col_phone, col_email that related to selected textbox
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")# count all rows and then
    count = cur.fetchone()[0]# call first index of the tuple and send it to the count
    return cur,count#return it  to first run function

#Select Item in ListBox
def onSelect(self,event):
    #calling the event is the self.lstlist1 widget
    varList = event.widget# what ever is triggering the event  
    select = varList.curselection()[0]# it comes here as a tuple and catches a index that user clicked on
    value = varList.get(select)#values gets the parametr of select(values gets info that user clicked on in a tuple) # our list box get text of what ever is the index number above  
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT col_fname, col_lname, col_fullname, col_phone, col_email FROM tbl_phonebook WHERE col_fullname = (?)''',[value])#
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data [] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])# when user click on textbox, it is going to place fname (before delete previous info)
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])#this indexes is a part of tuple(col_lname, col_fullname, col_phone, col_email) that we want to access and put the info that user click on
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])


def addToList(self):
    var_fname = self.txt_fname.get()#get user input
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent in the database
    var_fname = var_fname.strip()## This will remove any blank spaces before and after the user's entry(.strip)
    var_lname = var_lname.strip()# This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()# .title is ging to create a Capital letter in the beginning of user input Name
    var_fullname = ('{} {}'.format(var_fname, var_lname))# combine our normailzed names into a fullname
    print('var_fullname:{}'.format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not '@' or not ',' in var_email:
        print('Incorrect email format!!!')
    if(len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):#inforce user to input data in otherwise cannot pass it to the  next step
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existance of the fullname, if so it will alert user and diregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))#checking if name is already exists, if not then user can add it
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:# if this is 0 then there is no existance of the fullname and we can add new data
                print('chkName: {}'.format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook(col_fname, col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))# updating databse
                self.lstList1.insert(END, var_fullname)# update listbox with the new fullname
                onClear(self)#call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self)# call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())# Listbox's selected value
    conn =sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.sursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROMtbl_phonebok""")
        count = cur.fetchone()[0]
        if count > 1: # if count more than 1 meaning there is more than 1 row (user) in the database
            confirm = mesagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permanently deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDelete(self)# call the function to clear all of the textboxes and the selected index of listbox
######             onRefresh(self) # update the listbox of the changes
                conn.commit()
        else:
            confirm = mesagebox.showerror('Last Record Error', '({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete({}).'.format(var_select,var_select))
    conn.close()


def onDeleted(self):
    #clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

##    onRefresh(self) # update the listbox of the changes

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


def onRefresh(self):
     # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT (*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()




def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0]# index of the list selection
        var_value = self.lstList1.get(var_select)# list selection's text value
    except:
        messagebox.showinfo("Missing selection", "No name was selected from the list box. \nCnceling the Update request.")
        return
    # The user will only be alowed to update changes for phone and emails.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() #normalize data to maintain database intregrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): # ensure that there is data present
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var-phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".fromat(var_email))
            count2 =cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request", "The following changes ({}) and ({}) will be implemented for ({}), \n\nProceed with update request?".fromat(var_phone, var_email, var_value))
                print(response)
                if response:
                    #conn = sqlite3.connect('db_phonebook.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}', col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone, var_email,var_value))#updating the info
                        onClear(self)# clears the text box because no info needs to be resented in there because it is updated
                        conn.commit()
                else:
                    messagebox.showinfo('Cancel request', 'No changes have been made to ({}).'.fromat(var_value))
            else:
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone, var_email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)


if __name__ == "__main__":
    pass
                        
                
        
