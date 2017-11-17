from Calculate.Salary import *
from Calculate.discount import *

def netSalary():
    totalSal = salary()
    disc = discount()
    return totalSal - disc