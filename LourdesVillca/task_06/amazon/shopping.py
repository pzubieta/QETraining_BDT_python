from prettytable import PrettyTable
from task_06.amazon.item import Item
from task_06.amazon.logs import shopping_log
from task_06.amazon.sales import Sales


class Shopping:
    def __init__(self):
        self.items = []
        self.sales = []

    def pick_up_items(self):
        shopping_log.LOG.info("Inserting Items to the Store")
        name = input("Insert Item: ")
        amount = input("Insert amount: ")
        price = input("Insert price: ")
        shopping_log.LOG.debug("Item to insert: name: {}, amount: {}, price: {}".format(name, amount, price))
        self.items.append(Item(name, price, amount))

    def display_items(self):
        shopping_log.LOG.info("Available Items into the store")

        table = PrettyTable(['Index', 'Item', 'Amount', 'Price'])
        for index, item in enumerate(self.items):
            table.add_row([index, item.name, item.amount, item.price])
        print(table)

    def purchase_items(self, item_index, quantity):
        item = self.items[item_index]
        total_price = item.price * quantity
        self.sales.append(Sales(item, item.set_amount(quantity), total_price))

    def print_shopping_cart(self):
        shopping_log.LOG.info("Shopping cart")

        table = PrettyTable(['Item', 'Quantity', 'PU', 'Total Price'])
        for sale in self.sales:
            table.add_row([sale.item.name, sale.quantity, sale.item.price, sale.total_price])
        print(table)


x = Shopping()
x.items.append(Item("item01", 24, 100))
x.items.append(Item("item02", 10, 20))
x.items.append(Item("item03", 100, 50))
x.display_items()
x.purchase_items(0, 5)
x.print_shopping_cart()

x.display_items()
