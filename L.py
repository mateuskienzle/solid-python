''' Here, in this program, i applied the Liskov substitution principle from SOLID. 
    I'm applying this principle from the previous program, the one what i applied the Open–closed principle.
    So, what i did: i removed the "security_code" parameter from the "PaymentProcessor" class, and instead of this parameter
    being passed in the "PaymentProcessor" class, we are passing the parameter into each every function. 
    So, in this way, we can set any type of paramenter, and not necessary a security code as parameter. For exemple, if we include 
    a paypal payment type, it doesn't use security code, but use email adress as a form of verification. And, without put the parameter
    about security into each every class, wouldn't make sense pass an email adress in a parameter called "security_code". 
    And also, to this be possible, is necessary to create an initializer function in each class that would receive the parameter.'''

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

'''Removed the "security_code" from "PaymentProcessor" class'''
class PaymentProcessor(ABC): 
    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    '''Created an initializer function in "DebitPaymentProcessor" class to receive the "security_code" parameter'''
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    '''Created an initializer function in "CreditPaymentProcessor" class to receive the "security_code" parameter'''
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

'''Created a PaypalPaymentProcessor that uses an email adress as a security verification, instead security code'''
class PaypalPaymentProcessor(PaymentProcessor):
    '''Created an initializer function in "PaypalPaymentProcessor" class to receive the "email_address" parameter'''
    def __init__(self, email_address):
            self.email_address = email_address

    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("email@addres.com")
processor.pay(order)