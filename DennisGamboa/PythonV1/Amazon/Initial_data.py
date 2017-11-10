class Amazon:

    def __init__(self):
        self.store = {}

    def add_new_arrival(self, item, price, amount):
        self.store.setdefault(item, [price, amount])
        for key, val in self.store.items():
            ValZ = val[0]
            return ValZ


my_store = Amazon()
print(my_store.add_new_arrival("box", 4.95, 20))
my_store.add_new_arrival("paper", 1.99, 50)
my_store.add_new_arrival("staples", 1.00, 200)

