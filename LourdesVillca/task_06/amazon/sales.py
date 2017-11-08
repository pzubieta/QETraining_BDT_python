class Sales:
    def __init__(self, item, quantity, total_price):
        self.item = item
        self.quantity = quantity
        self.total_price = total_price

    def set_total_price(self, total):
        self.total_price = total