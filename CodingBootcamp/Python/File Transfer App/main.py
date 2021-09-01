import tkinter as tk
from tkinter import *
from tkinter import ttk

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.grid()

        #Define Master Frame Configuration
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        #Creation of ListBox to house files list.
        self.LB = Listbox()
        self.LB.insert(1,"Test", width = 25)
        self.LB.grid(row = 0, column = 0,)

        #Button Widget
        self.button1 = Button(self, text = "check for new files",)
        self.button1.grid(row = 10, column = 5)
        
        

        
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
