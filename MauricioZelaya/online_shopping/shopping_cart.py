from MauricioZelaya.online_shopping.items import item


class shopping_cart(item):


    def __init__(self):
        item.__init__(self)
        self.sc_items = []

    def get_items_into_cart_list(self):
        return self.sc_items

    def get_items_list(self):
        return super().get_items_list()

    def set_list_of_items(self, item_name, item_price, item_qty):
        super().set_new_item(item_name, item_price, item_qty)

    def add_item_to_cart(self, item_name, item_price, item_qty):
        new_item = [item_name, item_price, item_qty]
        # print(self.sc_items)
        self.sc_items.append(new_item)
        super().take_item(item_name, item_price, item_qty)

    def get_total_amount_to_pay(self):
        total_amount = 0
        for item in self.sc_items:
            total_amount += item[1]
        return total_amount

    def get_total_items_to_buy(self):
        pass

