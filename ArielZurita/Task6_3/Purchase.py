from Task6_3.PickupItem import *
from Task6_3.setInitialData import setAmount as setAmount
from Task6_3.setInitialData import setItems as setItems
from Task6_3.setInitialData import setPrices as setPrices

class Purchase:
    def __init__(self):
        self.purchase = []
        self.items = []
        self.prices = []
        self.amount = []

    def create_purchase(self, item, amount):
        self.item = item
        self.items = setItems()
        self.amount = amount
        self.amounts = setAmount()
        if self.item in self.items:
            index = self.items.index(item)
            amount = self.amounts[index]
            if amount > 0:
                pass

a = Purchase
a.create_purchase(a, "item A", 2)


