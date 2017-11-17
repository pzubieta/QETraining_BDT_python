import logging
from Item_store import *
class Pickup_items:
    def __init__(self):
        self.total_amount_buy=0
        self.list_item_a = {Item_store(1, "item 1",0.5, 10),Item_store(2, "item 2", 0.8, 5),Item_store(3, "item 3", 0.9, 3), Item_store(4, "item 4", 1, 2) }
        self.create_logger()

    def print_balance(self):
        self.logger.info('print_balance Action')
        for value in self.list_item_a:
            print(value.print_item())

    def get_item(self, id):
        self.logger.info('get_item Action')
        result = None
        #count_a=0
 #       while(count_a< len(self.list_item_a)):
#          if(self.list_item_a[count_a].get_id_item() == id):
#               return  self.list_item_a[count_a]
        for value in self.list_item_a:
            if(value.get_id_item()== id):
                string_value=value.print_item()
                self.logger.debug("return value: {} ".format(string_value) )
                result = value
        if(result== None):
            self.logger.debug("return None ")
            return None
            #count_a += 1
        return value

    def set_quantity_item(self, id, quantity):
        self.logger.info('set_quantity_item Action')
        result_action_void = False
        for value in self.list_item_a:
            if (value.get_id_item() == id):
                string_value = value.print_item()
                self.logger.debug("Set quantity item value: {} ".format(string_value))
                value.set_quantity(quantity)
                result_action_void = True


        if (result_action_void == False):
            self.logger.debug("Return set_quantity_item Action is false ")

        return result_action_void

    def calculate_total(quantity, price):
        total = quantity * price
        return total

    def showlistItems(self):
        listitems = ["tv", "radio", "laptop", "cargador"]
        listprices = [10, 15, 20, 25]
        listStock = [50, 50, 50, 50]
        print("Quantity : items : Price")
        for i in range(len(listitems)):
            print(listStock[i], ":", listitems[i], ":", listprices[i])


    def create_logger(self):
        self.logging = logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.handler = logging.FileHandler('Test_Log_Pickup_items.log')
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

