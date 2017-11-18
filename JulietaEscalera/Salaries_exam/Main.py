from Employee import *


def numEmployes(num):
    employ=[]

    if (num >=3):
        i = 0
        while (num>0):
            if (num < 15):
                name = str(input("Insert first name: "))
                lastname = str(input("Insert last name: "))
                depto= str(input("Insert depto as 'Sales' or 'Factory': "))
                emp1=Employee(name, lastname, depto)
                salary=emp1.salary()
                print(name,lastname,depto,salary)

                i+=1
                num -=1

    else:
         print("Atleast 3 employees should be register")



numEmployes(4)