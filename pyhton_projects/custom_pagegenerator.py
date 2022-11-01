



import tkinter as tk
from tkinter import *
# The webbrowser module is a python library
# that allows you to create web documents and display them in the browser. 
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title('Web Page Generator')

        self.custom_txt = Entry(width= 75)
        self.custom_txt.grid(row=0, column=0, columnspan=2, padx=(20,10), pady=(30,0))
        self.txt = tk.Label(self.master, text='Enter custom text or click the default HTML')
        self.txt.grid(row = 0, column = 0,padx=(20,0), pady=(0,0), sticky =N+W)
        self.btn = Button(self.master, text='Default HTML page', width = 15, height = 2, command=self.defaultHTML)
        self.btn.grid(row=1, column=0, padx=(15,0), pady=(0,15))
        self.submit = Button(self.master, text='Submit Custom Text', width =15, height=2, command=self.submitCustom)
        self.submit.grid(row=1, column=1, padx=(0,0), pady=(0,15))
        
            
    def defaultHTML(self):
        htmlText = 'Stay tuned for our amazing summer sale!'
        htmlFile = open('index.html', 'w')
        htmlContent = '<html>\n<body>\n<h1>' + htmlText + '</h1>\n</body>\n</html>'
        # creating tag html, body, h1 inside the doc 
        htmlFile.write(htmlContent)
        htmlFile.close()
        # tab name 
        webbrowser.open_new_tab('index.html')


        
    def submitCustom(self):
        var_text = self.custom_txt.get()
        var_text = var_text.strip()
        File = open('index.html', 'w')
        Content = '<html>\n<body>\n<h1>' + var_text + '</h1>\n</body>\n</html>'
        File.write(Content)
        File.close()
        webbrowser.open_new_tab('index.html')

        
if __name__ =='__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
