from exam.packages import *
from exam.Person  import *



Int_numUsr= int(input("introduzca la cantidad de usuarios:"))
tip=Int_numUsr
count=0

print("\n")
listUsr=[]
#INTRODUCE USUARIOS


if Int_numUsr< 3 or Int_numUsr>15:
    print("no esta en el rango de numeros de usarios")
else:
    while count< Int_numUsr:
        #print ("CONTADOR ES:",count)
        name=input("introduzca el nombre usario:")

        dep=input("Introduzca Departamento del usario:")

        if dep=="Factory":
            piecesP=int(input("Introduza la Cantidad de piezas producidas: "))
            piecesD=int(input("introduzca la cantidad de piezas defectuosas: "))
            totalF= factoryEmployee(piecesP,piecesD)
            disF= Discount(totalF)
            netF= netSalary(totalF,disF)
            listUsr.append(Employee(name, dep, totalF, disF,netF))

        elif dep =="Sales":
            piecesS = int(input("Introduza la Cantidad de piezas vendidas: "))
            totalS= salesEmployee(piecesS)
            disS = Discount(totalS)
            netS = netSalary(totalS, disS)
            listUsr.append(Employee(name, dep, totalS, disS, netS))
        else:
            break

        count=count+1
#para imprimir
GetEmployeeS()




