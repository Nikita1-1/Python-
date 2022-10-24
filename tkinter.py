
import tkinter
from tkinter import *  



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = True)# you can resize the window tht program is open in
        self.master.geometry ('{}x{}'.format(700, 400))# 700 height, 400 width
        self.master.title('Learning Tkinter')
        self.master.config(bg = 'lightgray')

        self.varfName = StringVar()
        self.varlName = StringVar()
        self.varfName.set('Nikita')
        self.varlName.set('Sazonov')

##        print(self.varfName.get()) print the names in the holder 
##        print(self.varlName.get())

        self.txtfName = Entry(self.master,text = self.varfName, font = ('Helvetica', 16), fg = 'black', bg = 'lightblue')
        self.txtfName.pack()#pack means paint
        

        self.txtlName = Entry(self.master,text = self.varlName, font = ('Helvetica', 16), fg = 'black', bg = 'lightblue')
        self.txtlName.pack()








if __name__ == '__main__':
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()# we need main loop to keep app alive otherwise it will close 
    
