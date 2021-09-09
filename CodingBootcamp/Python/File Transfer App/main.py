import tkinter as tk
from tkinter import *
from tkinter import ttk

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.grid()

        #Define Master Frame Configuration
        self.master = master
        self.master.title("File Checker App")
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        
        
        #Enrtry Widget
        self.master.E1 = tk.Entry(self, insertbackground = "green")
        self.master.E1.grid(row = 1, column = 2)
        
        #Entry Widget
        self.master.E2 = tk.Entry(self, )
        self.master.E2.grid(row = 2, column = 2)

        #Button 1
        self.master.b1 = Button(self, text = "test.....", fg="green", bg="azure")
        self.master.b1.grid(row = 1, column = 0)
        #Button 2
        self.master.b2 = Button(self, text = "test")
        self.master.b2.grid(row = 2, column = 0)
        #Button 3
        self.master.b3 = Button(self, text = "test")
        self.master.b3.grid(row = 3, column = 0)
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
