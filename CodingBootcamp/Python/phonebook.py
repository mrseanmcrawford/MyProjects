# Python Ver:   3.5.1

#
# Author:       Mr. Sean M Crawford
#
# Purpose:      Phonebook Demo:  Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with MacOS BigSur and Windows 10!

from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access to them
import phonebook_gui.py
import phonebook_func

# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame._init_(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500, 300)
        # This CenterWindow method will cengter our app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("Seans Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is Tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on windows OS and MacOS OS
        self.master.protocol("WM_DELETE_WINDOW", lambda:phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets dfrom a seperate module,
        # keppin your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)






if _name_=="__main__":
    root = tk.tk()
    App = ParentWindow(root)
    root.mainloop()
       
