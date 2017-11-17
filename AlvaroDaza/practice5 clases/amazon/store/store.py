from item import item
import log

logger = log.setup_custom_logger(__name__)


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.list_total_items = []
        self.total = 0

    def get_store_name(self):
        return self.store_name

    def add_item(self, item_name, item_price, amount):
        new_item = item.Item(item_name, item_price)
        self.list_item = [new_item, amount]
        logger.info('Append the new Item {}'.format(item_name))
        self.list_total_items.append(self.list_item)

    def sell_item(self, item_name, amount):
        logger.info('Calculating the total sold')
        self.total += amount * self.decrease_amount(amount, item_name)
        return self.total

    def decrease_amount(self, amount, item_name):
        for item_in_list in self.list_total_items:
            if item_in_list[0].get_name() == item_name:
                logger.info('Decreasing the store amount in {}'.format(amount))
                item_in_list[1] -= amount
                return item_in_list[0].get_price()
        print ("That item does not exist in store ")

    def show_total_products(self):
        print ('=====Items in stock=======')
        for item_in_list in self.list_total_items:
            print (str(item_in_list[0].get_name()) + '   Amount : ' + str(
                item_in_list[1]) + '  Price:' + str(item_in_list[0].get_price()))
