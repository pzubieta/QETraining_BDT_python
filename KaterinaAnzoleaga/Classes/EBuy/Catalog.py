class Catalog:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.items = []

        self.id = id
    def add_item (self, item, price, amount):
        aItem = {'name': item, 'price': price, 'amount': amount}
        self.items.append(aItem)

    def get_item (self, item):
        for i in self.items:
            if i['name'] == item: return (i)
            break
        else: return (None)

class Carrito:
    def __init__(self, customerID):
        self.items = []
    def add_item (self, name, amount)


myCatalog = Catalog ('Ropa', '001')
myCatalog.add_item('blusa', '235.5', '250')
myCatalog.add_item('chompa', '135.5', '320')
myCatalog.add_item('jeans', '280.99', '520')
print (myCatalog.get_item('jeans'))



