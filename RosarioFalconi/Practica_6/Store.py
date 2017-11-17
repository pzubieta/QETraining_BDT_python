from RosarioFalconi.Practica_6.Item import Item
from RosarioFalconi.Practica_6.Product import Product
from RosarioFalconi.Practica_6.ShoppingCar import ShoppingCar
import logging

class Store:

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    def __init__(self,car):
        self.products={'Arroz': 10.5, 'Harina': 5.5, 'Leche':6.3,'Sal':1.0}
        self.scar=car

    def pick_product (self, a_product):
        pass

    def buy_item (self, a_item):
        pass

    def remove_item(self,):
        pass