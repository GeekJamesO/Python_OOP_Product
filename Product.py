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
        print "    " + self.brand + " " + self.itemName +  " : $" + str(self.price) + "($" + str(self.cost) + ")  #" + self.weight + "  Status: " + self.status
        return self;

# shoes = Product(10.00, "red shoes", "1 lb", "nike", 4.50)
#
# print "display product"
# shoes.display()
#
# print "Demo sold"
# shoes.sell().display()
#
# print "Demo returned in box"
# shoes.Return(False, False).display()
#
# print "Demo returned Opened box"
# shoes.sell().Return(True, False).display()
#
# print "Demo defective product in Opened box"
# shoes.sell().Return(True, True).display()

"""
Optional Assignment: Store
    Now, let's build a store to contain our products by making a store class and
    putting our products into an array.
Store class:
    Attributes:
        products:
            an array of products objects
        location:
            store address
        owner:
            store owner's name
    Methods:
        add_product:
            add a product to the store's product list
        remove_product:
            should remove a product according to the product name
        inventory:
            print relevant information about each product in the store
    You should be able to test your classes by instantiating new objects of each
    class and using the outlined methods to demonstrate that they work.
"""

#Product must support itemName as a value.
class Store():
    def __init__(self, location, owner):
        self.products = []
        self.location = location
        self.owner = owner
    def changeOwner(self, newOwner):
        self.owner = newOwner
        return self
    def changeLocation(self, newLocation):
        self.location = newLocation
        return self
    def add_product(self, aProduct):
        self.products.append(aProduct)
        print "  Product {0} has been added.".format(aProduct.itemName)
        return self;
    def remove_product(self, name):
        for item in self.products:
            if item.itemName == name :
                print "  Product {0} has been removed.".format(item.itemName)
                self.products.remove(item)
                break;
        return self;
    def inventory(self):
        print "  Store Inventory:"
        for item in self.products:
            item.display()

        return self;
    def display(self):
        print "Store Location: '" + self.location + "'  Owner: " + self.owner
        self.inventory();
        return self;

aStore =  Store("boston commons", "Bob bobville")
aStore.add_product(Product(10.00, "red shoes", "1 lb", "nike", 3.50))
aStore.add_product(Product(12.00, "blue shoes", "1 lb", "nike", 6.50))
aStore.add_product(Product(14.00, "old shoes", "1 lb", "nike", 1.90))
aStore.add_product(Product(5.00, "new shoes", "1 lb", "nike", 1.50))
aStore.display()

aStore.changeOwner("Frank Franks")
aStore.changeLocation("Across the street")
aStore.remove_product("old shoes")
aStore.display()
