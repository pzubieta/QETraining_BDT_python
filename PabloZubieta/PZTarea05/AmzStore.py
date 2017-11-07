import logging
from AmzItem import AmzItem

logging.basicConfig(filename='example.log', level=logging.INFO)

class AmzStore:
    """This is the class that represents the amazone store"""

    def __init__(self, strName):
        self.amzItemsList = []
        self.strName = strName


    def append(self, intId, strName, fltPrice, intAmount):
        newItem = AmzItem(intId, strName, fltPrice, intAmount)
        self.amzItemsList.append(newItem)
        logging.info('New Item has been added to the store')  # Logging the addition of items

    def add_item (self, intId, strName, fltPrice, intAmount):
        newItem = AmzItem(intId, strName, fltPrice, intAmount)
        self.amzItemsList[int(intId)].append(newItem)
        logging.info('I told you so')  # will not print anything

    def sell_item(self, intId, intAmount):
        print("////////////",self.amzItemsList[int(intId)],"/////////////")
        self.amzItemsList[int(intId)].setAmount(self.amzItemsList[intId].getAmount() - intAmount)
        logging.info("The item with ID= %s has been selled." % (self.id))    # Logging the sell

    def items_list(self):
        return self.amzItemsList
        logging.info("Listing Items.")  # Logging the sell

my_store = AmzStore("tienda test1")
my_store.append(1, "Samsung S8 plus", 750, 5)
my_store.append(3, "Samsung S7", 550, 5)
my_store.append(2, "Huawei Mate 8", 550, 4)

print ("\n")
print ("ITEM: ", my_store.items_list()[0])
for single_item in my_store.items_list():
    print (single_item,"\n" )

my_store.sell_item(2, 1)
