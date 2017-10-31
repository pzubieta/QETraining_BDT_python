#--------------------------------------------------------------------------

def area_of_circle (radius):
    #calculates the circle area for given radius in a list when radius are greater than 10
    res = 0

    for r in radius:
        if r > 10 : print ("Area = ", 3.14159265 * (r ** 2))


def sum_to (n):
    """Sum to n when n is lower than 35"""
    count = 0
    sum = 0

    if n > 35 : n = 35

    while count <= n:
        sum = sum + n
        count = count + 1

    print("Sum to ", n," is: ", sum)

area_of_circle([15,3,7,12,17])
sum_to (14)

#------------------------------------------------------------------------------
def evenOddCheck(numList)
    """Check is the given number is odd or even"""
    for i in numList:
        if numList[i] % 2 = 0 : print("the number is EVEN."
        else : print("the number is ODD.")


def primesFrom(rangeNum)
    count = 1
    while count < rangeNum:
        count = count + 1
        if rangeNum > 35
            print("the number is greater than 35: ", rangeNum)
            continue



def daysInMonth(monthReq)
    res = 31
    if monthReq == "January" || monthReq == "March" || monthReq == "May" || monthReq == "July" || monthReq == "August" || monthReq == "October" || monthReq == "Dicember" :
        print("The ", monthReq, " moth has: 31 days."
    elif monthReq == "April" | | monthReq == "june" | | monthReq == "September" | | monthReq == "November":
        print("The",  monthReq, " moth has: 30 days."
    elif :
        print("The ", monthReq, " moth has: 28 days."

numb = [9, 1, 3, 2]
evenOddCheck(numb)
primesFrom(35)

daysInMonth("February")