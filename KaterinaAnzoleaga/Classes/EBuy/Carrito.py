class Carrito:

    def __init__(self):
        self.items = []

    def get_item_index (self, item):
        j = -1
        for i in self.items:
            if i['name'] == item:
                j = self.items.index(i)
                return (j)
                break
        return (j)

    def add_item (self, name, price, amount):
        j = self.get_item_index(name)
        if j < 0:
            anItem = {'name': name, 'price': price, 'amount': amount}
            self.items.append(anItem)
        else:
            self.items[j]['amount'] = self.items[j]['amount'] + amount

    def list_items (self):
        for i in self.items:
            print (i)

    def get_total_price (self):
        total = 0
        for i in self.items:
            total = total+ i['price']*i['amount']
        return total

      



unCarro = Carrito ()
print (unCarro.get_item_index('jeans'))
unCarro.add_item('jeans', 250.5, 2)
unCarro.list_items()
unCarro.add_item('jeans', 250.5, 2)
unCarro.list_items()
print (unCarro.get_item_index('jeans'))
print (unCarro.get_total_price())


