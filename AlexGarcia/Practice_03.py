print('***************Exercise01****************************')
#Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius value is greater of 10.
def cicle_area(radio):
  pi=3.14159
  Area=pi*(radio**2)
  print('the area is equals to:', Area, 'and the radio is:',radio)

def tool_radio():
	r=int(input("ingrese un radio\n"))
	if(r>10):
		cicle_area(r)
	else:
		print('the radius value shoul be greater of 10.')
    
tool_radio()

print('***************Exercise02****************************')

#Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until any value lower than 35. So sum_to(10)wouldbe1+2+3...+10which would return the value 55, but if n=40 only until sum to 35 need to be returned.  

def sum_to():
  Num=int(input("ingrese un numero\n"))
  sum=0
  if Num==40:
    print('deberiamos sumar 1+2+3+...+31+32+34+35')
    for i in range(1,Num+1):
      sum=sum+i
      if sum>=630:
        break
      else:
        continue
    print(sum)
  else:
    for i in range(1,Num+1):
      sum=sum+i
    print(sum)

sum_to()
print('***************Exercise03****************************')

#Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years:
#		days_in_month("February") == 28
#	    days_in_month("December") == 31
# If the function is given invalid arguments, it should return None. 

def mes_tiene():
  mes=raw_input("ingrese un mes\n")
  mes=mes.capitalize()
  Enero="Enero"
  Febrero="Febrero"
  Marzo="Marzo"
  Abril="Abril"
  Mayo="Mayo"
  Junio="Junio"
  Julio="Julio"
  Agosto="Agosto"
  Septiembre="Septiembre"
  Octubre="Octubre"
  Noviembre="Noviembre"
  Diciembre="Diciembre"
  
  if (mes==Enero):
    print('Enero tiene 31')
  elif (mes==Febrero):
    print('Febrero tiene 28')
  elif (mes==Marzo):
    print('Marzo tiene 31')
  elif (mes==Abril):
    print('Abril tiene 30')
  elif (mes==Mayo):
    print('Mayo tiene 31')
  elif (mes==Junio):
    print('Junio tiene 30')
  elif (mes==Julio):
    print('Julio tiene 31')
  elif (mes==Agosto):
    print('Agosto tiene 31')
  elif (mes==Septiembre):
    print('Septiembre tiene 30')
  elif (mes==Octubre):
    print('Octubre tiene 31')
  elif (mes==Noviembre):
    print('Noviembre tiene 30')
  elif (mes==Diciembre):
    print('Diciembre tiene 31')
  else:
    print('None')

mes_tiene()