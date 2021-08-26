

f = open("myfile3.html", "a")
f.write("Stay tuned for our amazing summer sale!")
f.close()

#open and read file after apedning
f = open("myfile3.html","r")
print(f.read())

if __name__=="_main_":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
