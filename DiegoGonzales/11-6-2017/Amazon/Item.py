class Item:

    def __init__(self, item="", precio=0, cantidad=0):
        self.addItem(item, precio, cantidad)

    def addItem(self, item="", precio=0, cantidad=0):
        self.setItem(item)
        self.setPrecio(precio)
        self.setCantidad(cantidad)

    def getItem(self):
        return self.item

    def setItem(self, newItem):
        self.item = newItem

    def getPrecio(self):
        return self.precio

    def setPrecio(self, newPrecio):
        self.precio = newPrecio

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, newCantidad):
        self.cantidad = newCantidad

    def toStringItem(self):
         string = self.getItem(), self.getPrecio(), self.getCantidad()
         return string