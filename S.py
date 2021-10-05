''' Here, in this program, i started applying the Single-responsibility principle from SOLID. 
    I'm applying this principle from the initial program.
    So, what i did: i created another class called "PaymentProcessor" to separete the both operations that the
    initial program had, wich are the both forms of payment: credit and debit'''

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

'''This is the class that i created to separate the both forms of payment into two classes, which each one has their own form of payment'''
class PaymentProcessor: 
    '''Function responsible for the debit payment'''
    def pay_debit(self, order, security_code):
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"
    '''Function responsible for the credit payment'''
    def pay_credit(self, order, security_code):
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"



order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "0372846")