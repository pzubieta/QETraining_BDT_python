class Amazon:

    def __init__(self, item, price, amount):
        self.items = item
        self.prices = price
        self.amounts = amount

    def buy(self):
        if self.amounts == 0:
            print('Sorry, we are all out of {} right now.'.format(self.items))
            return
        print("How many are you buying? We have {}".format(self.amounts))
        quant = int(input("Amount:  "))
        while quant > self.amounts:
            print('Sorry, we only have {} left'.format(self.amounts))
            quant = int(input("Amount:  "))
        self.amounts -= quant
        subto = self.prices * quant
        total = subto * 1.08
        print("There are now {} left".format(self.amounts))
        print("The total price is ${}".format(total))
        return



stock = {}
stock['box'] = Amazon("box", 4.95, 20)
stock['paper'] = Amazon("paper", 1.99, 50)
stock['staples'] = Amazon("staples", 1.00, 200)

print("Which are you buying? {}".format(','.join(stock.keys())))
ioi = input("Please use the exact word name: ")

while ioi not in stock:
   print("Sorry, we do not have any {} right now.".format(ioi))
   print("Which are you buying? {}".format(','.join(stock.keys())))
   ioi = input("Please use the exact word name: ")



stock[ioi].buy()