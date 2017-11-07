class item:
    def __init__(self):
        self.inventory = []

    def get_items_list(self):
        return self.inventory

    def set_new_item(self, item_name, item_price, item_qty):
        if not self.item_exists(item_name, item_price):
            new_item = [item_name, item_price, item_qty]
            self.inventory.append(new_item)
        else:
            self.add_quantity(item_name, item_price, item_qty)

    def item_exists(self, item_name, item_price):
        for item in self.inventory:
            if item[0] == item_name and item[1] == item_price:
                return True
            else:
                return False

    def add_quantity(self, item_name, item_price, item_quantity):
        for item in self.inventory:
            if item[0] == item_name and item[1] == item_price:
                item[2] += item_quantity
                break

    def take_item(self, item_name, item_price, item_qty):
        for item in self.inventory:
            if item[0] == item_name and item[1] == item_price:
                item[2] -= item_qty
                break




