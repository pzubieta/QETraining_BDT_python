print "+_+_+_+_++_+_+_+ Par/impar_+_+_+_+_+_+_+_+_+_"

n= [22, 24,4,5,3,6,43]
count=0
long=len(n)

while (count<long):
    if (n[count]%2==0):
        print "es par",n[count]
    else:
        print "es impar", n[count]
    count= count+1

#primo
print"_+_+_+_+_+_+Primo+_+_+_+_+_+_"

lista=[3,4,7,45,3,45,2,23,56,53,71]

for j in  range (len(lista)):
    cont=1
    divisores=0
      #lista [j]
    # print "array es:",lista[j]
    for i in range (lista[j]):
        if(lista[j]%cont==0):
            divisores= divisores +1
           #print "total de divisores:",divisores
        #else:
            # print "nah"
        cont=cont+1
    if (divisores==2):
         print "el numero:", lista [j],"es primo"
    else :
         print "el numero:", lista [j],"no es primo"

print"_+_+_+_+_+_+area circulo+_+_+_+_+_+_"



def area_circle(r):

    if r > 10:
        area1 = 3.14*(r**2)
        print "Function: el resultado es",area1
    else:
        print   "es menor a 10"
    return (area1)

#llamada
r=12
AreaCircle= area_circle(r)
print "Main: El area es",AreaCircle


print "_+_+_+_+_+_+Sumatoria+_+_+_+_+_+_"

def sum_to (val):
    sum1= 0
    n = 1
    #val=37
    #print "suma es", sum1
    while val>= n:
         if n >= 36:
             break
         else:
             #print n,"es menor a",35
             #print "numero es",n
             sum1=sum1+n
             #print "suma es",sum1
             n=n+1
    return (sum1)
    #print "La suma es:", sum1

val=45
sumatory=sum_to(val)
print "the summatory of",val," is:", sumatory

print "_+_+_+_+_+_+Months+_+_+_+_+_+_"

def days_in_month(month):

    if month =="January":
        #print "January has 31 days"
        days=31
    elif month =="February":
        #print "February has 28 days"
        days=28
    elif month =="March":
        #print "March has 31 days"
        days=31
    elif month =="April":
        #print "April has 30 days"
        days=30
    elif month =="May":
        #print "May has 31 days"
        days=31
    elif month =="June":
        #print "June has 30 days"
        days=30
    elif month =="July":
        #print " July has 31 days"
        days=31
    elif month =="August":
        #print "August has 31 days"
        days=31
    elif month =="September":
        #print "September has 30 days"
        days=30
    elif month =="October":
        #print "October has 31 days"
        days=31
    elif month =="November":
        #print "November has 30 days"
        days=30
    elif month =="December":
        #print "December has 31 days"
        days=31
    else:
        print "Eso no es un mes !!!!!"
    return (days)




month= "March"
dayofMonth= days_in_month(month)
print month, "has", dayofMonth, "days" 