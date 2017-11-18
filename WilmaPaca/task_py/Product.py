class Product:
    def __init__(self,item = "",price = 0.0,amount = 0):
        self.item_p = item
        self.price_item = price
        self.amount_item = amount

    def getItem(self):
        return self.item_p

    def getPriceItem(self):
        return self.price_item

    def getAmount(self):
        return self.amount_item

    def setItem(self,item_change):
        self.item_p = item_change

    def setPrice(self,price_change):
        self.price_item = price_change

    def setAmount(self,amount_change):
        self.amount_item = amount_change
