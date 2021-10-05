''' Here, in this program, i applied the Interface segregation principle from SOLID. 
    I'm applying this principle from the previous program, the one what i applied the Liskov substitution principle.
    So, what i did: considering a real problem that would have another form of verification, besides security code or email adress.
    For include a SMS authorization, for example, in cases that have to do this kind o verification, like debit and paypal payment types,
    is necessary to create another class which makes this SMS authorization and include this class in the other classes with the payments
    types that use this. So, i created "PaymentProcessor_SMS" class which receives "PaymentProcessor" as a parameter. Then, all i have
    to do when is necessary to have the SMS authorization is pass the "PaymentProcessor_SMS" as a parameter to the class that needs to use it.
    
    Instead of just create a function that make the SMS authorization inside the class "PaymentProcessor", is necessary to create another
    class to do this, because using a whole class, i can set where i want to use the authorization function or not. If i used the PaymentProcessor
    class to create the authorization SMS funcion, i would have to verify this function in every other classes of paymente, even the one that
    don't use the SMS authorization, like credit payment.'''

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


class PaymentProcessor(ABC): 

    @abstractmethod
    def pay(self, order):
        pass

'''Created the "PaymentProcessor_SMS" class'''
class PaymentProcessor_SMS(PaymentProcessor):

    @abstractmethod
    def auth_sms(self, order):
        pass

'''Passed the "PaymentProcessor_SMS" parameter, instead of "PaymentProcessor" '''
class DebitPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False
    '''Created a function that uses the "auth_sms" (which is inside of "PaymentProcessor_SMS"), to verify the SMS code'''
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        '''Created a if-else statment that verify if the conditions of verifying are authorized or not'''
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

'''Passed the "PaymentProcessor_SMS" parameter, instead of "PaymentProcessor" '''
class PaypalPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False
    '''Created a function that uses the "auth_sms" (which is inside of "PaymentProcessor_SMS"), to verify the SMS code'''
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        '''Created a if-else statment that verify if the conditions of verifying are authorized or not'''
        if not self.verified: 
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("email@addres.com")
processor.auth_sms(465839)
processor.pay(order)