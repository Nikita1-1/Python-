
# The interface for users to transfer files from one directory to another.


import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import time
from datetime import datetime, timedelta
import glob

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        #Sets title of GUI
        self.master.title('File Transfer')
        
        # create the button and entry to select the directory that we want to transfer files from.
        #Create button to select files from source directory
        self.sourceDir_btn = Button(text='Select Source', width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #Create entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI Using tkinter grid padx pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        # Creating button to select destination of file from destination directory
        self.destDir_btn = Button(text='Select Destination', width=20, command=self.destDir)
        # Position destination button in GUI using grid()
        # on th enext row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)# you can insert text via 
        # Positions entry in GUI using tkinter grid() padx and pady are the same as
        # the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))


        #Ceate button to transfer files
        self.transfer_btn = Button(text='Transfer Files', width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0, 15))


        self.exit_btn = Button(text='Exit', width=20, command=self.exitProg)
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget
        # This allows the path to be inserted into th eentry widget properly
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)


    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget
        # this allows the path to be inserted into the entry widget property
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    # Function that will transfer the files from the source to the destination
    def transferFiles(self):
        # Gets source directory
        source = self.source_dir.get()
        #Gets destination
        destination = self.destination_dir.get()
        # Gets a list of files in the source directory
        source_files = os.listdir(source)
        #Runs thorough each file in the source direct
        for i in source_files:# for loop to get files one by one in the folder
            # GETMTIME Return the time of last modification of path. The return value is a floating point number
            # giving the number of seconds since the epoch
            modtime = os.path.getmtime(source + '/'+ i)#full path
            modificationTime = datetime.fromtimestamp(modtime)# converting getmtime into datetime
            todayDate = datetime.now()# getting current time 
            modifyDateLimit = todayDate - timedelta(days=1)# substracting curent time - 1 to get 24 hours 
            if modificationTime > modifyDateLimit:
                shutil.move(source + '/' + i, destination)
                print(i + 'was successfully transferred')

    def exitProg(self):
        root.destroy()
        

if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

