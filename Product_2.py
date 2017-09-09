class Product(object):
    def __init__(self, price, itemName, weight, brand, costs, status= "for sale"):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.costs = costs
        self.status = status

    def Sell(self):
        if (self.status.lower() == "sold"):
            raise Exception("Sold product that is already marked as 'sold'.")
        else:
            self.status = "sold"
        return self

        #takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def AddTax(self, taxDecimal ):
        return self.price + (self.price * taxDecimal)

    def Return(self, isBoxOpened, defectReason):
        if defectReason == "defective":
            self.price = 0
            self.status = "defective"
        elif not isBoxOpened:
            self.status = "for sale"
        else:
            self.price *= 0.8
            self.status = "box opened"
        return self

    def DisplayInfo(self):
        print "Price: {}, Item Name {}, Weight {}, Brand {}, Cost{}, Status: {}".format(self.price, self.itemName, self.weight, self.brand, self.costs, self.status)
        return self

    def __str__(self):
        return "Price: {}, Item Name {}, Weight {}, Brand {}, Cost{}, Status {}".format(self.price, self.itemName, self.weight, self.brand, self.costs, self.status)

pa = Product(60.00, "Instant Camera", 8, "PhotoMaster", 48.00)
print 'Create a new item with the following stats: 60.00, "Instant Camera", 8, "PhotoMaster", 48.00'

pa.DisplayInfo()

print "Show the price with a 10 percent tax.", pa.AddTax(0.10)
print ""
print "Show that the price was not affected by tax."
pa.DisplayInfo()

print ""
print "Sell the product"
pa.Sell()
pa.DisplayInfo()

print ""
print "return the product with the box opened."
pa.Return(True, "box opened").DisplayInfo()
