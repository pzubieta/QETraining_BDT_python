class Catalog:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.items = []

    def add_item (self, item, price, amount):
        aItem = {'name': item, 'price': price, 'amount': amount, 'sold':0} # When adding items to the catalog the number of items sold is 0
        self.items.append(aItem)

    def get_item (self, item):
        for i in self.items:
            if i['name'] == item:
                return (i)
                break
        else: return (None)

    def purchase_item (self, item):
        for i in self.items:
            j = 0
            if i['name'] == item:
                j = self.items.index(i)
                if self.items[j]['amount'] >= 1:
                    self.items[j]['amount'] = self.items[j]['amount'] - 1
                    self.items[j]['sold'] = self.items[j]['sold'] + 1
                else:
                    print ("Sorry there are not more '", item,"' in our store" )
                    break
        if j == 0:
           print("Sorry, the item '", item, "' is not in the catalog")

    def list_items (self):
        for i in self.items:
            print (i)



myCatalog = Catalog ('Ropa', '001')
myCatalog.add_item('blusa', 235.5, 250)
myCatalog.add_item('chompa', 135.5, 320)
myCatalog.add_item('jeans', 280.99, 1)

myCatalog.purchase_item('jeans')
myCatalog.purchase_item('jeans')
myCatalog.purchase_item('jDSGeans')

print ("Final Catalog: ")
myCatalog.list_items()




