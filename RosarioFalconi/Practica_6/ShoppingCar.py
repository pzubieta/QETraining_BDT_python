import logging

class ShoppingCar:

    def __init__(self, items):
        self.items=[]

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_Total(self):
        total=0
