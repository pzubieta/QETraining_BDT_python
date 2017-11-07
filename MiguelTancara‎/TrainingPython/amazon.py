import logging

class product:

    logging.basicConfig(filename="product.log", level=logging.INFO)
    logging.info("Program started")

    def __init__(self):
        #self.Amount = 0
        logging.info("initializing parameters")
        self.prodItems = {"mp3": 10}
        self.prodPrices = {"mp3": 30}


    def getPrice(self, item):
        #message = "Product does not exist"
        logging.debug("Checking if the item exists")
        if item in self.prodPrices:
            logging.info("returning the price")
            return self.prodPrices[item]
        else:
            return False

    def getAmount(self, item):
        #message = "Product does not exist"
        logging.debug("Checking if the item exists")
        if item in self.prodItems:
            logging.info("returning the amount")
            return self.prodItems[item]
        else:
            return False


    def addItems(self, name, price, items):
        if name in self.prodItems:
            logging.info("Updating an existent item")
            self.prodItems[name] += items
        else:
            logging.info("Adding a new item")
            self.prodItems[name] = items
        self.prodPrices[name] = price


class shopping:

    logging.basicConfig(filename="shopping.log", level=logging.INFO)

    #purchaseProducts = {}

    def __init__(self):
        self.amount = 0
        self.product = product()


    def doPurchase(self):
        band = 1
        amount = 0
        purchaseProducts = {}
        totalItems = {}

        logging.info("Starting the shopping")
        while band == 1:
            item = str(input("Please enter the item that you want to buy: "))
            logging.info("adding the itme to the list of things to buy")
            price = int(product.getPrice(item))
            itemAmount = product.getAmount(item)
            logging.info("checking if theitme exists")
            if (price != False and itemAmount > 0):
                print("The price of the selected item is: ", price)
                logging.info("adding the numebr of itmes to buy ")
                numberItems = int(input("Please introduce the numbers of item to buy: "))
                amount = numberItems * price
                if item in purchaseProducts:
                    logging.info("updating the list of itmes to buy")
                    purchaseProducts[item] += amount
                    totalItems[item] += numberItems
                else:
                    logging.info("Adding the new item to the  the list of itmes to buy")
                    purchaseProducts[item] = amount
                    totalItems[item] = numberItems
                print(purchaseProducts)
            else:
                print("The item that you are trying to buy does not exist")
            continueBuy = input("Do you want continue buying? yes/no :")
            if continueBuy == 'no':
                logging.info("Shopping is end ")
                band = 0
        print ("below is the list of products that you bought")
        for key,total in totalItems.items():
            logging.info("updating the list of items")
            product.prodItems[key] -= total
        for key,value in purchaseProducts.items():
            logging.info("Printing the list of items bought")
            print("Product:", key, " Total Amount: ", value)


    def addproduct(self):
        value = 1
        while (value == 1):
            name = str(input ("Introduce the name of the product that you want to add: "))
            logging.info("Introducing  the item name")
            numItems = int(input ("Introduce the amont of items to save: "))
            logging.info("Introducing  the item number")
            price = int(input("Introduce the price of the item: "))
            logging.info("Introducing  the item price")
            print(name, price, numItems)
            logging.info("Adding to new item")
            product.addItems(self, name,price,numItems)
            addingItmes = input("Do you want continue adding more items? yes/no :")
            if addingItmes == 'no':
                print("Thanks for add items to the store")
                logging.info("Adding products is end")
                band = 0


product = product()
product.addItems("laptop", 1500, 3)
product.addItems("mp4", 15, 14)
product.addItems("mp4", 30, 6)
product.addItems("portatil", 1300, 5)
product.addItems("pc", 500, 10)

print("The price for mp3 is: ", product.getPrice("mp3"))
print("The price for a laptop is: ", product.getPrice("laptop"))

print("The amount of items for mp3 is: ", product.getAmount("mp3"))
print("The amount of items for a laptop is: ", product.getAmount("laptop"))


shop = shopping
#shop.addproduct('')
shop.doPurchase('')