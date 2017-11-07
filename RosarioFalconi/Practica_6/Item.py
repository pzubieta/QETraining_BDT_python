from RosarioFalconi.Practica_6.Product import Product


class Item(Product):
    def __init__(self, name, price, amount):
        Product.__init__(self,name,price)
        self.amount=amount

    def getBalance(self):
        return self.price*self.amount
