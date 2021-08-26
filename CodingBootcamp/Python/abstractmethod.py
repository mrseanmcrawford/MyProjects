from abc import ABC, abstractmethod
class phone(ABC):
    def paySlip(self,amount):
        print("Your purchase amount: ", amount)
#this function is telling us to pass in an argument,
#but we wont tell you how or what kind
#of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(phone):
    #Herre we've defined how to implement the payment function
    #from its parent pasySlip class.
    def payment(sef,amount):
        print('Your purchase amount of {} exceeded your $500.00 limit'.format(amount))


obj = DebitCardPayment()
obj.paySlip("$750.00")
obj.payment("$750.00")
