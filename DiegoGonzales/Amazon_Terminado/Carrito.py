from Amazon.Catalogo import Catalogo

class Carrito(Catalogo):

    def __init__(self):
        self.catalogo = Catalogo()
        self.listCarrito = []

    def length_Carrito(self):
        return len(self.listCarrito)

    def add_Carrito(self, producto):
        self.listCarrito.append(producto)

    def delete_ProductoCarrito(self, index):
        self.listCarrito.remove(self.listCarrito[index])

    def clear_Carrito(self):
        self.listCarrito.clear()

    def display_Carrito(self):
        for i in range(self.length_Carrito()):
            print(self.listCarrito[i])

    def comprar_Productos(self):
        return self.listCarrito

    def cancelar_Compra(self):
        return "Compra cancelado:" + self.clear_Carrito()