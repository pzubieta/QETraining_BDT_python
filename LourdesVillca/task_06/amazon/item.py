class Item:
    def __init__(self, item_name, price, amount):
        self.name = item_name
        self.price = price
        self.amount = amount

    def set_amount(self, purchase_amount):
        self.amount -= purchase_amount
