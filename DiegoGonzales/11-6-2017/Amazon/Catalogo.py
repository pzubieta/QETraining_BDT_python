from Amazon.Item import Item

class Catalogo(Item):

    def __init__(self):
        super().__init__()
        self.itemObj = Item()
        self.catalog = []

    def add_Item(self, item, precio, cantidad):
        self.itemObj = Item(item, precio, cantidad)
        self.catalog.append(self.itemObj)

    def get_TotalItems(self):
        return len(self.catalog)

    def set_Item(self, index, newCantidad):
        itemx = self.catalog[index]
        itemx.setCantidad(newCantidad)

    def displayCatalogo(self):
        itemx = ""
        for i in range(self.get_TotalItems()):
            itemx = self.catalog[i]
            print(itemx.toStringItem())

