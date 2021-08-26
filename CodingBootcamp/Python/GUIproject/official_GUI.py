# -*- coding: utf-8 -*-
#
# Python Ver: 3.5.1
#
# Author: Sean M. Crawford
#
# Purpose: Web page generator app.
#
# Tested OS: This code was written and tested to work with Windows 10.


import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser

#Be sure to import other modules
class base(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("Website Generator App")
#Entry Widget
        self.entry1 = Entry(width=25)
        self.entry1.grid(row = 0, column= 1, columnspan= 25 )
#Button Widget
        self.button1 = Button( text = "Click Here", width = 25 )
        self.button1.grid(row = 1, column = 1, columnspan = 2)
#Retreiving text from Entry Widget
    def submit(self):
        UserText = self.entry1.get()
        HTMLCode = "<html><head><title>Python HTML</title></head><body>"+UserText+"</body></html>"
        
open("submit", "w")

webbrowser.open_new("seancrawford/MyProjects/CodingBootcamp/Python/GUIproject")
    
        

if __name__ == "__main__":
    root = tk.Tk()
    App = base(root)
    root.mainloop()
    


