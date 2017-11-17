import Module_calculate
import Module_print

def importBoth ():
    numberOfUsers = int(input("Please, enter the number of users: "))
    if numberOfUsers > 0:
        list = {}
        for i in range(numberOfUsers):
            names = input("Please enter a name: ")
            ages = int(input("Please enter an age: "))
            list[names] = ages

        for name, age in list.items():
            print(name)
            Module_calculate.calculate(age)
            Module_print.printMessages(age)

        #for key in list:
                #print(key)
         #   Module_calculate.calculate (list[key])
         #   Module_print.printMessages (list[key])
    #    for
    #print(x)
importBoth()