import AmzItem;


class amStore:
    """This is the class that represents the amazone store"""

    def __init__(self, strName):
        self.amzItemsList = []
        self.strName = strName

    def append(self, intId, strName, fltPrice, intAmount):
        newItem = AmzItem(intId, strName, fltPrice, intAmount)
        self.amzItemsList.append(newItem)

    def addItem (intId, strName, fltPrice, intAmount):
        newItem = AmzItem(strName, fltPrice, intAmount)
        self.amzItems[intId].append(newItem)

    def buyItem(intId, intAmount):
        self.amzItemsList[intId].setAmount(self.amzItems[intId].getAmount() - intAmount)

bm = amStore('tienda test1')
bm.append("001", "Samsung S8 plus", 750, 5)
bm.addItem("002", "Huawei Mate 8", 550, 4)