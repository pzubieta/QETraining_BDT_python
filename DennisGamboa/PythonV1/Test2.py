class Retail:

    def __init__(self, price, unitsOnHand, description):
        self.price = price
        self.unitsOnHand = unitsOnHand
        self.description = description

    def buy(self):
        if self.unitsOnHand == 0:
            print('Sorry, we are all out of {} right now.'.format(self.description))
            return
        print("How many are you buying? We have {}".format(self.unitsOnHand))
        quant = int(input("Amount:  "))
        while quant > self.unitsOnHand:
            print('Sorry, we only have {} left'.format(self.unitsOnHand))
            quant = int(input("Amount:  "))
        self.unitsOnHand -= quant
        subto = self.price * quant
        total = subto * 1.08
        print("There are now {} left".format(self.unitsOnHand))
        print("The total price is ${}".format(total))
        return


stock = {}
stock['box'] = Retail(4.95, 20, "Boxes")
stock['paper'] = Retail(1.99, 0, "Big Stacks of Paper")
stock['staples'] = Retail(1.00, 200, "Staples")

print("Which are you buying? {}".format(','.join(stock.keys())))
ioi = input("Please use the exact word name: ")

while ioi not in stock:
   print("Sorry, we do not have any {} right now.".format(ioi))
   print("Which are you buying? {}".format(','.join(stock.keys())))
   ioi = input("Please use the exact word name: ")

stock[ioi].buy()