''' Here, in this program, i applied the Open–closed principle from SOLID. 
    I'm applying this principle from the previous program, the one what i applied the Single-responsibility principle.
    So, what i did: i separeted the both forms of payment into two classes now. And also modified the "PaymentProcessor" class,
    giving to this class a generic value, that i can set to the other classes in my program.
    So i can use this classe to pass itself as a parameter to the other two classes of payments types (debit and credit).
    And, to do that, i had to import ABC method from abc library, so i could set the "PaymentProcessor" class as a generic class
    
    In this way, now i can create any extension for my application, without modifying any of others classes and functions that already exist.
    For example, now i can create another form of payment, without change anything in the classes or functions from the others payments types'''

'''Imported the abc from ABC library '''
from abc import ABC, abstractclassmethod, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = []

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

'''Set the PaymentProcessor class as a generic class'''
class PaymentProcessor(ABC): 
    @abstractmethod
    def pay(self, order, security_code):
        pass

'''Creted a class only for the debit payment type'''
class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

''' Creted a class only for the credit payment type'''
class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order, "0372846")