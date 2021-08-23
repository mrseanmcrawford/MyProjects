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

#Be sure to import other modules

class base(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Website Creator App")
        self.button1 = Button( self, text = "Click Here", width = 25,
                               command = self.new_window )
        self.button1.grid(row = 0, column = 1, columnspan = 2, sticky = W+E+N+S)
    def new_window(self):
        self.newWindow = base2()

class base2(Frame):
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Website Creator App2")
        new.button = tk.Button(text = "PRESS TO CLOSE", width = 25,
                               command = self.close_window)
        new.button.pack()
    def close_window(self):
        self.destroy()
def main():
    base().mainloop()
if __name__ == '__main__':
    main()
        
    
