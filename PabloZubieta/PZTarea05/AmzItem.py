import logging

logging.basicConfig(filename='example.log', level=logging.INFO)

class AmzItem:
    """This is the class that holds Items for the store"""

    def __init__(self, intId, strName, fltPrice, intAmount = 0):
        logging.info('***************Starting.')
        self.id = intId
        self.amount = intAmount
        self.name = strName
        self.price = fltPrice

    def __str__(self):
        return "%s %s %s %s" % (self.id, self.amount, self.name, self.price)

    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)

    def sellItem(self, intAmount):
        self.amount = self.amount - intAmount
        logging.info('Selling ITEM')  # Logging the sell of items

    def pickupItem(self, intAmount):
        self.amount = self.amount + intAmount

    def setId (self, intId):
        self.id = intId

    def setAmount(self, intAmount):
        logging.info('ITEM ammount updated.')  # Logging the sell of items
        self.amount = intAmount


    def setName(self, strName):
        self.name = strName

    def setPrice(self, fltPrice):
        self.price = fltPrice

    def getAmount (self):
        return self.amount

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price
