from Task6_3.setInitialData import setAmount as setAmount
from Task6_3.setInitialData import setItems as setItems
from Task6_3.setInitialData import setPrices as setPrices

class PickupItems:
    def __init__(self):
        self.items = []
        self.prices = []
        self.amount = []

    def itemsAndPrices(self):
        self.items = setItems()
        self.prices = setPrices()
        itemAndPrices = []
        itemAndPrice = ()
        for item in self.items:
            i = self.items.index(item)
            itemAndPrice = (item, self.prices[i])
            itemAndPrices.append(itemAndPrice)
        return itemAndPrices

    def itemsAndAmount(self):
        self.items = setItems()
        self.amounts = setAmount()
        itemAndAmounts = []
        itemAndAmount = ()
        for item in self.items:
            i = self.items.index(item)
            itemAndAmount = (item, self.amounts[i])
            itemAndAmounts.append(itemAndAmount)
        return itemAndAmounts


a = PickupItems
a.itemsAndPrices(a)
a.itemsAndAmount(a)





