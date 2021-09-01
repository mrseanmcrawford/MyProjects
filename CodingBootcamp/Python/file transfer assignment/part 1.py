import shutil
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk


class frame(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("file mover app")
        self.frame1 = tk.Frame(master= frame, width=100, height=100, bg="red")
        frame1.pack()
        

        #set where the source of the files are
source = '/Users/seancrawford/Desktop/folder b/'

        #set the destinaton path to folder b
destination = '/Users/seancrawford/Desktop/folder a/'
files = os.listdir(source)

now = time.time()
day = 24 * 60 * 60
past = now - day

def last_modified (file):
            return os.path.getmtime(file)

for file in os.listdir(source):
    source_file = os.path.join(source,file)
    if last_modified(source_file) > past:
        f_destination = os.path.join(destination,file)    
        #We are saying move the files represented by 'i' to their new destination
        shutil.move(source_file, f_destination)


if __name__ == "__main__":
    root = tk.Tk()
    App = frame(root)
    root.mainloop()
