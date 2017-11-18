class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def name(self):
        return self.name

    def price(self):
        return self.price

    def __set_name__(self, name):
        self.name=name

    def set_price(self, price):
        self.price=price
