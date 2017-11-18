from Person import Person
from Employee import Employee

primeraPersona = Employee('JoseLuis','EsponjaCuadrada','Sales','2','0','0')
segundaPersona = Employee('Cumbiero','Terry','Factory','0','100','2')
terceraPersona = Employee('Ruber','Cuellar','Sales','2','0','0')


print("NAME                        |Departamento|Global Salary|Total Descuento|Net SAlary")


if  str(primeraPersona.Department) == 'Sales':
    Name = primeraPersona.getEmployee()
    Area = str(primeraPersona.Department)
    Global = primeraPersona.SalaryGlobal_sale_Employee(int(primeraPersona.piecesSold))
    Descuento = primeraPersona.descuento(Global)
    SalarioNeto = primeraPersona.Salario_Neto(Global, Descuento)
    print(Name,"   |",Area,"     |",Global,"        |",Descuento,"        |",SalarioNeto)

if  str(segundaPersona.Department) == 'Factory':
    Name = segundaPersona.getEmployee()
    Area = str(segundaPersona.Department)
    Global = segundaPersona.SalaryGlobal_fatory_Employee(int(segundaPersona.piecesGood),int(segundaPersona.piecesBad))
    Descuento = segundaPersona.descuento(Global)
    SalarioNeto = segundaPersona.Salario_Neto(Global, Descuento)
    print(Name,"             |",Area,"   |",Global,"      |",Descuento,"      |",SalarioNeto)


