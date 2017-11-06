class AmzItem:
    """This is the class that holds Items for the store"""

    def __init__(self, intId, strName, fltPrice, intAmount = 0):
        self.intId = intId
        self.intAmount = intAmount
        self.strName = strName
        self.fltPrice = fltPrice

    def __str__(self):
        return "%s %s %s %s" % (self.intId, self.intAmount, self.strName, self.fltPrice)

    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)

    def setId (intId):
        self.intId = intId

    def setAmount (intAmount):
        self.intAmount = intAmount

    def setName(strName):
        self.strname = strName

    def setPrice(fltPrice):
        self.fltPrice = fltPrice

    def getAmount ():
        return self.intAmount

    def getName():
        return self.strName

    def getPrice():
        return self.fltPrice

