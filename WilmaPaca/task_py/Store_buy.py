import logging
from Product import Product
class Product_store:
    def __init__(self):
        self.amount_item_buy = 0
        self.list_itemsPrice_buy = {}
        self.list_itemsAmount_buy = {}
#        self.list_items_amount = {}
        self.Total_price = {}
        self.index = 0
        self.item = {}

    def add_product(self,n_item):
        while self.index < n_item:
            item = input("Enter product: ")
            price = input("Enter price: ")
            amount = input("Enter amount: ")
            pro = Product(item,price,amount)
            self.item[self.index] = pro

            self.index += 1

    def getItem(self):
        print("#", " ", " ITEM ", " ", "PRICE  ", " ", "AMOUNT ")
        for key, value in self.item.items():
            print (key," ",value.getItem()," ",value.getPriceItem()," ",value.getAmount())

    def buyItemP(self,value):
        a_amount = int(input("Amount: "))
        for key, value in self.item.items():
#            print(value)
            quantity = int(value.getAmount())
#            print (quantity, " ",a_amount)
            if a_amount <= quantity:
                a = value.getItem()
                self.list_itemsAmount_buy[a] = int(value.getAmount())
#                print("******************************************", value.getItem())
#                self.list_items_buy.extend(key,value.getItem())
                self.list_itemsPrice_buy[a] = float(value.getPriceItem())
                self.decreaseAmount_item(key,a_amount)
                break

    def decreaseAmount_item(self, key, amount_decrease):
        for key, value in self.item.items():
            change_a = int(value.getAmount()) - amount_decrease
            value.setAmount(change_a)

    def calculte_total_price(self,unit_price,amount_item):
        return unit_price*amount_item

    def sum_totalPriceItemsBuy(self):
        for key,value in self.Total_price.items():
            self.amount_item_buy += self.calculte_total_price[value]

    def printListItemsToBuy(self):
        i = self.index
        print("  ITEMS   ", " ", " UNIT  PRICE  ", " ", "  AMOUNT  ", " ", " TOTAL PRICE   ")
        for key,value in self.list_itemsPrice_buy.items():
            price = self.list_itemsPrice_buy[key]
            quantity = int(self.list_itemsAmount_buy[key])
            a = self.calculte_total_price(price, quantity )
            self.Total_price[key] = a
            print (key," ",self.list_itemsPrice_buy[key]," ",self.list_itemsAmount_buy[key], self.Total_price[key])
            i +=1
        print ("TOTAL PRICE ALL ITEM: ", self.amount_item_buy)

product_number = int(input("Enter product number to insert: "))
buyItem = Product_store()
buyItem.add_product(product_number)
print(" ---------- Following products available ----------")
buyItem.getItem()
itemToBuy = input("Enter product  to buy e.g. apple: ")
buyItem.buyItemP(itemToBuy)
print ("Following product are bought: ")
buyItem.printListItemsToBuy()
print ("Do you want to add other product?")
answer_user = input("Enter 'Y'/'N' :")
if answer_user == "Y":
    print(" ---------- Following products available ----------")
    buyItem.getItem()
    itemToBuy = int(input("Enter product e.g. apple: "))
    buyItem(itemToBuy)
else:
    print ("Thanks !!!")

