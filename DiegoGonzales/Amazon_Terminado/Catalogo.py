from Amazon.Item import Item
from Amazon.Log import Log

class Catalogo(Item):

    def __init__(self):
        super().__init__()
        self.logger = Log()
        self.itemObj = Item()
        self.catalog = []

    def add_Item(self, item, precio, cantidad):
        self.itemObj = Item(item, precio, cantidad)
        self.catalog.append(self.itemObj)
        self.logger.log_info(self.itemObj)

    def get_TotalItems(self):
        return len(self.catalog)

    def pedir_Item(self, index, newCantidad):
        itemx    = self.catalog[index]
        cantidad = itemx.getCantidad()-newCantidad
        total    = itemx.getPrecio() * newCantidad
        itemx.setCantidad(cantidad)
        str = itemx.getItem(),itemx.getPrecio(),newCantidad,"=",total
        return str

    def delete_Item(self, index):
        itemName = self.catalog[index]
        self.catalog.remove(self.catalog[index])
        return "Eliminado: ", itemName.toStringItem()

    def clear_Catalog(self):
        return "Catalogo limpio.", self.catalog.clear()

    def displayCatalogo(self):
        itemx = ""
        for i in range(self.get_TotalItems()):
            itemx = self.catalog[i]
            print(itemx.toStringItem())