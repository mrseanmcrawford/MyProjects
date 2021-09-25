import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os
import time

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.grid()

        #Define Master Frame Configuration
        self.master = master
        self.master.title("File Mover App")
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        
        
        #Enrtry Widget
        self.master.E1 = tk.Entry(self)
        self.master.E1.grid(row = 1, column = 2)

        
        
        #Entry Widget
        self.master.E2 = tk.Entry(self, )
        self.master.E2.grid(row = 2, column = 2)
        

        #Button 1
        self.master.b1 = Button(self, text = "Choose Source", command = lambda:Getsource(self))
        self.master.b1.grid(row = 1, column = 0)
        #Button 2
        self.master.b2 = Button(self, text = "Choose Destination", command = lambda:GetDest(self))
        self.master.b2.grid(row = 2, column = 0)
        #Button 3
        self.master.b3 = Button(self, text = "Move", command = lambda:MoveFiles(self))
        self.master.b3.grid(row = 3, column = 0)

        def Getsource(self):
            path = filedialog.askdirectory(title="Select folder")
            self.master.E1.delete(0,END)
            self.master.E1.insert(0, path)

        def GetDest(self):
            path = filedialog.askdirectory(title="Select folder")
            self.master.E2.delete(0, END)
            self.master.E2.insert(0,path)
        
        def MoveFiles(self):

        #Gets the text from the E! entry widget and saves it to the variable named source
            source = self.master.E1.get()

         #set the destinaton path to folder b
            destination = self.master.E2.get()

         #Compiles a list of files in the source folder and saves it to a variable names files
            files = os.listdir(source)

            now = time.time()
            day = 24 * 60 * 60
            past = now - day

        # Getting modification time of a specific file
            def last_modified (file):
                    return os.path.getmtime(file)

        #itterates through the list of files         
            for file in files:
        #Gets the absolute path of each file 
                source_file = os.path.join(source,file)
                if last_modified(source_file) > past:
                    f_destination = os.path.join(destination,file)    
        #We are saying move the files represented by 'i' to their new destination
                    shutil.move(source_file, f_destination)
                    
        
        
        
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
