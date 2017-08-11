'''
Assignment: Product
    The owner of a store wants a program to track products. Create a product
    class to fill the following requirements.
Product Class:
    Attributes:
        Price
        Item Name
        Weight
        Brand
        Cost
        Status: default "for sale"
Methods:
    Sell:
        changes status to "sold"
    Add tax:
        takes tax as a decimal amount as a parameter and returns the price of
        the item including sales tax
    Return:
        takes reason for return as a parameter and changes status accordingly.
        If the item is being returned because it is defective change status to
        defective and change price to 0. If it is being returned in the box, like
        new mark it as for sale. If the box has been opened set status to used
        and apply a 20 percent discount.
    Display Info:
        show all product details.

Every method that doesn't have to return something should return self so methods can be chained.
'''

class Product():
    def __init__(self, price, itemName, weight, brand, cost, status="for sale"):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = "sold"
        return self;
    def addTax(self, decimal):
        self.price += (self.price * decimal)
        return self;
    def Return(self, isBoxOpened, isDefective):  # must use upper case, return is a keyword.
        print "inReturn"
        if (isDefective):
            self.price = 0;
            self.status = "defective"
        else:
            if (isBoxOpened):
                self.price *= 0.8
                self.status = "Returned: Opened box"
            else: #box unopened.
                self.status = "for sale"
        return self
    def display(self):
        print self.brand + "  " + self.itemName, ": $" + str(self.price) + "($" + str(self.cost) + ") " + self.weight + " Status: " + self.status
        return self;

shoes = Product(10.00, "red shoes", "1 lb", "nike", 4.50)

print "display product"
shoes.display()

print "Demo sold"
shoes.sell().display()

print "Demo returned in box"
shoes.Return(False, False).display()

print "Demo returned Opened box"
shoes.sell().Return(True, False).display()

print "Demo defective product in Opened box"
shoes.sell().Return(True, True).display()
