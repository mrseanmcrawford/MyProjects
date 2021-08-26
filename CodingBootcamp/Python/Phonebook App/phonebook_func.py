import os
from tkinter import *
import tkinter as tk
import sqlite3


# Be sure to import our other modules
# so we can have access to them
import phonebook_main
import phonebook_gui

def center_window(self, w, h):# pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the usere's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo


# catch if the user clicks on the upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel1('Exit program', 'Okay to exit application?'):
        # This closes the app
        self.master.destroy()
        cs._exit(0)



#=================================================================================

def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exist tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TDXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            ):')
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data = ('John', 'Doe','John Doe','123-456-7890','Jdoey@gmail.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur_execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", (data))
            conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count

# Select item in ListBox
def onSelect(self,event):
    # Calling the event is the self.1stList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt._fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(o,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt.lname.get()
    #nomalize the data to keep itconsistant in the database
    var_fname = var_fname.strip() # This will remove ant blank spaces before and after the user's entry
    var_fname = var_lname.strip() # This will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) # combine our nomalized names into a fullname
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email: # will use this soon
        print("Incorrect email format")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): # enforce the user to provide both 
        conn - sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existence of the fullname, if so we will alert user and disregard request
            cursor = conn.cursor()
            # check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is zero than there is no existance of the fullname and we can add new data
                print('chkName: {}'.format(chkName))
                cursor.exectute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES ((?,?,?,?,?)""")
                self.1stList1.insert(END, var_Fullname) # update ListBox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exist in the database! Please choose a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing text Error", "Please ensure that there is data in all four fields.")

def onDelete(self):
    var_select = self.1stList1.get(self.1stList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM rtbl_phoneboojk""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Conformatgion
        if confirm:
            conn = sqlite3.connect('phonebook.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute("""DELETE Confirmation", "All information associated with (()) \n will be permenantly deleted""")
                if confirm:
                    conn = sqlite3.connect('phonebook.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '()'""".format(var_select))
                    onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
                    ##### onRefresh(self) # update the listbox of the changes
                    conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the kast record in the database and cannot be deleted at this time.")
    conn.close()

def onDeleted(self):
    # clear th text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
## onRefresh(self) # update the listbox of the changes
    try:
        index = self.1stList1.curseselection()[0]
        self.1stList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in those textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.1stList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        1 = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item is varList:
                self.1stList1.insert(0,str(item))
                i = 1 + 1
    conn.close()

def onUpdate(self):
    try:
        var_select = self.1stList1.curselection()[0] # index of the list selection
        var_value = self.1stList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing selection", "No name was selected from the list box. \nCancelling the Update request.")
        return
    # The user will only be showed to update changed for phone and emails.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain database integrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) abd (len(var_email) > 0): # ensure that there is data present
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT (col_phone) FROM tbl_phonebook WHERE col_phone = '()'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            our.execute(""" SELECT COUNT (col_email) FROM tbl_phonebook WHERE col_email = '()'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("update Reqwuest","the following changes ({}) and ({}) will be implemented for ({}).")
                print(response)
                if resopnse:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""update Request", "The following changes ({}) and ({}) will be implemented for ({}).""")
                        onClear(self)
                        conn.commit()
                    else:
                        messagebox.showinfo("Cancel request","No changes have been made to ({]).".format( var_value))
                else:
                    messagebox.showinfo("No changes deteccted", "Both ({}) and ({}) \nalready exist in the database for this name. \nYour update
                onClear(self)
            conn.close()
        else:
            messagebox.showerror("Missing information","Please select a name for the list. \nThen edit the phone or email information.")
        onClear(self)
                
            
                
                    
                
                           



















    
            
                                         
        

                           
                           
                           
    

