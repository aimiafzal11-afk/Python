class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, obj):
        return self.price > obj.price

    def showDetails(self):
        print("Item:", self.item)
        print("Price:", self.price)

o1 = Order("Dress", 9000)
print("--ORDER 1 DETAILS--")
o1.showDetails()
o2 = Order("Watch", 10000)
print("--ORDER 2 DETAILS--")
o2.showDetails()

if o1 > o2:
    print("Order 1 is greater!")
else:
    print("Order 2 is greater!")