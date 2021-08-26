class User:
    # Define the attributes of the class
    name = "No Name Provided"
    email = ""
    Password = "1234abcd"
    account = 0

    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("?Enter your password: ")
        if  (entry_email == self.email and entry_password == self.password):
            print("Welcome back, ()".format(self.name))
        else:
            print("You are not authorized for this page.")
#User Class
new_user = User()
#Call the login method using the new object
new_user.login()

def __init__(self, name, email, password, account):
    self.name = name
    self.email = email
    self.password = password
    self.accpunt = account

new_user = User("Sean Crawford", "Smcrawford@hi.com", "12345", "0")

#Defining child classes
class Employee(User):
    base_pay = 11.00
    department = 'general'

class Customer(User):
    mailing_address = " "
    mailing_list = True


