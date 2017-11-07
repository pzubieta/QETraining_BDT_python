class Item:
    def __init__(self, item, price):
        self.item_name = item
        self.item_price = price

    def get_name(self):
        return self.item_name

    def get_price(self):
        return self.item_price

    def get_item(self):
        print (
            'the item is: {}  his price is : {} '.format(self.item_name, self.item_price))
