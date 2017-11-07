import AlejandroAlcocer.practices.catalog as catalog
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler("Test_Log.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)



class Purchate_Item():


    def __init__(self):
        self.item = 0
        self.amount = 0
        self.catalog = catalog.items
        self.cart = []


    def get_cart(self): return self.cart

    def add_to_cart(self, item, amount, price): self.cart.append([item, amount, price])

    def get_price(self, item, amount): return int(self.catalog[item]["price"]) * amount

    def print_catalog(self):
        for item in self.catalog:
            print(item, catalog.items[item])


    def ask_for_items(self):
        more_items = True
        while more_items == True:
            self.print_catalog()
            logger.debug("print_catalog: %s", "catalog was printed")
            item = input("which item would you like to buy: ")
            logger.debug("item: %s", item)
            amount = int(input("how many items would you like to purchase "))
            logger.debug("amount: %s", amount)
            price = self.get_price(item, amount)
            logger.debug("price: %s", price)
            self.update_catalog(item, amount)
            logger.debug("catalog: %s", "catalog was updated")
            self.add_to_cart(item, amount, price)
            logger.debug("cart: %s", "cart was updated")
            more_items = self.ask_more_items()


    def ask_more_items(self):
        ask_for_more_items = input("would you like to add more items to your cart (y/n): ").lower().strip()
        more_items = True
        if ask_for_more_items == "y":
            more_items = True
            logger.debug("ask_for_more_items: %s", ask_for_more_items)
        elif ask_for_more_items == "n":
            more_items = False
            logger.debug("ask_for_more_items: %s", ask_for_more_items)
        return more_items


    def update_catalog(self, item, amount):
        new_amount = int(self.catalog[item]["amount"]) - amount
        self.catalog[item]["amount"] = new_amount
        logger.debug("update_catalog: %s", "catalog amount was updated with {}".format(new_amount))


def flow():
    p = Purchate_Item()
    p.ask_for_items()
    print(p.get_cart())

flow()