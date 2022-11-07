

import tkinter as tk
from tkinter import *
# The webbrowser module is a python library
# that allows you to create web documents and display them in the browser. 
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title('Web Page Generator')


        self.btn = Button(self.master, text='Default HTML page', width = 30, height = 2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10), pady=(10,10))
            
    def defaultHTML(self):
        htmlText = 'Stay tuned for our amazing summer sale!'
        htmlFile = open('index.html', 'w')
        htmlContent = '<html>\n<body>\n<h1>' + htmlText + '</h1>\n</body>\n</html>'
        # creating tag html, body, h1 inside the doc 
        htmlFile.write(htmlContent)
        htmlFile.close()
        # tab name 
        webbrowser.open_new_tab('index.html')
        
        

    

if __name__ =='__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
