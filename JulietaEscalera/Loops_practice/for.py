# method pair or odd
def par_impar(n):

    if(n%2==0): print(n, " es par ")
    else: print (n, " es impar ")
    return

# method is prime

def es_primo ():
    prim_list=[2,3,5,7,13,17,19,23,29,31,37,41,43,47]
    num_list=[14,2,5,582,3,8,25,49]
    esprim=0

    for val in num_list :
         for primo1 in prim_list:

            esprim= val % primo1
            primo=val/primo1
            print(val," ",primo1)

            if (esprim != 0 and primo==1):
                print("El numero es primo", val)
                break
            if(esprim ==0 and primo !=1):
                print("El numero no es primo", val)
                break


# method area or circle
 
def area_of_circle(r):
    pi=3.1416

    if r>10 : print("Area del circulo=", pi*(r**2))
    else: print("The radious is less or iqual 10")




#method sum_to

def sum_to(n):
    limit=0
    sum=0
    while(limit<35 ):
      limit+=1
      sum=limit+sum
      if(limit==n):
         break
    print ("The sum to",n,"is",sum)


par_impar(5)

es_primo()

area_of_circle(2)

sum_to(10)


