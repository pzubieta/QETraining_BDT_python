import logging

class Item_store:
    def __init__(self, id_item, name_item,unit_price, quantity):
        self.id_item = id_item
        self.name_item= name_item
        self.unit_price = unit_price
        self.quantity=quantity
        self.create_logger()

    def get_unit_price(self):
        self.logger.info('get_unit_price action')
        return self.unit_price

    def set_unit_price(self,unit_price):
        self.logger.info('set_unit_price action')
        self.unit_price = unit_price

    def get_name_item(self):
        self.logger.info('get_name_item action')
        return self.name_item
    def set_name_item(self,name_item):
        self.logger.info('set_name_item action')
        self.name_item = name_item


    def get_id_item(self):
        self.logger.info('get_id_item action')
        return self.id_item
    def set_id_item(self,id_item):
        self.logger.info('set_id_item action')
        self.id_item = id_item

    def set_quantity(self,quantity):
        self.logger.info('set_quantity action')
        self.quantity = quantity
    def get_quantity(self):
        self.logger.info('get_quantity action')
        return self.quantity

    def print_item(self):
        self.logger.info('Start print a Item')
        self.logger.debug(
            "Item Id: {}; Item Name: {} ; Item Price: {} ;Item Stock: {}".format(self.id_item, self.name_item, self.unit_price,self.quantity))
        return "Item Id: {}; Item Name: {} ; Item Price: {} ;Item Stock: {}".format(self.id_item, self.name_item, self.unit_price, self.quantity)

    def create_logger(self):
        self.logging = logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.handler = logging.FileHandler('Test_Log_Item_store.log')
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)