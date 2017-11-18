from Amazon.Catalogo import Catalogo
from Amazon.Carrito import Carrito
from Amazon.ImprimirFactura import ImprimirFactura
from Amazon.Log import Log

catalog = Catalogo()
carrito = Carrito()
carrito2 = Carrito()
factura = ImprimirFactura()
logger = Log()

catalog.add_Item("Coca Cola", 8, 50)
catalog.add_Item("Galleta", 2, 20)
catalog.add_Item("Leche", 5, 100)
catalog.add_Item("Pan", 1, 30)
catalog.add_Item("Coco", 3, 70)
catalog.add_Item("Picadillo", 5, 150)

logger.log_info("Hola")

#print(catalog.pedir_Item(2, 3))
#catalog.displayCatalogo()

#print(catalog.delete_Item(1))
#catalog.displayCatalogo()
#print(catalog.clear_Catalog())
#catalog.displayCatalogo()

carrito.add_Carrito(catalog.pedir_Item(2, 3))
carrito.add_Carrito(catalog.pedir_Item(4, 5))
carrito.add_Carrito(catalog.pedir_Item(1, 10))
carrito.add_Carrito(catalog.pedir_Item(5, 3))
carrito.add_Carrito(catalog.pedir_Item(0, 3))
#carrito.delete_ProductoCarrito(1)
#carrito.display_Carrito()

factura.add_Producto_to_Factura(carrito.comprar_Productos())
factura.print_Factura("Diego Gonzales")


carrito2.add_Carrito(catalog.pedir_Item(0, 2))
carrito2.add_Carrito(catalog.pedir_Item(1, 2))
carrito2.add_Carrito(catalog.pedir_Item(2, 3))
carrito2.add_Carrito(catalog.pedir_Item(3, 4))

factura.add_Producto_to_Factura(carrito2.comprar_Productos())
factura.print_Factura("Bilma Balderrama")
#print(factura.length_Factura())
#print(factura.get_FacturaByIndex(1))