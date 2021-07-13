import sqlite3


#created parent class
class Medication:
    name = "Backtrum"
    use = "pain"
    dosage = "tbh"
    form = "pill"
#created getMedication function 
    def getMedication(self):
        entry_name = input("Enter name of the medication: ")
        entry_use = input("Enter use of the medicqtion: ")
        entry_dosage = input("Enter the dosage of the medication: ")
        entry_form = input("Enter the form of medication: ")
        if entry_use == "pain":
            print("Backtrum")
        else:
            print("no other options")
#created child class
class oral(Medication):
    temp = "cold"
    flavor = "Rasberry"
#created parent class
class intravenous(Medication):
    ounces = "5"
    storage_type = "cold"
    use = "immediate relief"
        
    
    



    
