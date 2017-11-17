global totalSal

def salary1(numSold):
    totalSal = 0
    return numSold * 2.5


def salary2(numProd,numDefect):

 return (numProd * 10 - numDefect * 1.3)

def discount1(numSold):
    totalSal = salary1(numSold)
    return totalSal * 0.125

def discount2(numProd,numDefect):
    totalSal = salary2(numProd,numDefect)
    return totalSal * 0.125

def netSalary1(numSold):
    totalSal = salary1(numSold)
    disc = discount1(numSold)
    return totalSal - disc

def netSalary2(numProd,numDefect):
    totalSal = salary2(numProd,numDefect)
    disc = discount2(numProd,numDefect)
    return totalSal - disc


