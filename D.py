''' Here, in this program, i applied the Dependency inversion principle from SOLID. 
    I'm applying this principle from the previous program, the one what i applied the Interface segregation principle.
    So, what i did: i created a generic class that authorize some process of authorization, like SMS, security code, i'm not a robot...
    So, in this way, is possible to put any form of verification in any other class. We just have to pass the parameter with the authorizer
    class type into the classes parameters.
    As mentioned above, now we can to verify any kind o verification, so i can remove the function that uses the "auth_sms" from the 
    clasees that use the SMS authorization, because, now, the class "Authorizer" makes the verification.. '''

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

'''Created a generic "Authorizer" class that just veryfy any process of security'''
class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

''' Passed the "Authorizer" paramer to the classes that make some form of verification'''
class SMSauth(Authorizer):

    authorized = False

    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

''' Created the class "NotARobot", and passed the "Authorizer" paramer to the classes that make some form of verification'''
class NotARobot(Authorizer):

    authorized = False

    def not_a_robot(self):
        print("Are you a robot?")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor(ABC): 

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    '''Passed the "authorizer" parameter with its kind "Authorizer for all the classes that uses any form of verification" '''
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
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

class PaypalPaymentProcessor(PaymentProcessor):
    '''Passed the "authorizer" parameter with its kind "Authorizer for all the classes that uses any form of verification" '''
    def __init__(self, email_address, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = NotARobot() 
processor = PaypalPaymentProcessor("email@addres.com", authorizer)
authorizer.not_a_robot()
processor.pay(order)