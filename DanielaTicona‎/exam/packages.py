def salesEmployee(numPieceS):
    salarioS = numPieceS * 2.5
    return salarioS

def factoryEmployee(numPieceP, numPriceD):
    salarioF=numPieceP*(10- numPriceD)*1.3
    return salarioF

def Discount (salary):
    discount=salary*0.125
    return discount

def netSalary(salary, discount):
    netSalario=salary-discount
    return netSalario
#sasad
