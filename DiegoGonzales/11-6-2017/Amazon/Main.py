from Amazon.Catalogo import Catalogo

catalog = Catalogo()

catalog.add_Item("Coca Cola", 8, 50)
catalog.add_Item("Galleta", 1, 20)
catalog.add_Item("Leche", 5, 100)
catalog.add_Item("Pan", 0.5, 30)
catalog.add_Item("Coco", 3, 70)
catalog.add_Item("Picadillo", 5, 150)

print(catalog.get_TotalItems())
catalog.set_Item(2, 1)
catalog.displayCatalogo()