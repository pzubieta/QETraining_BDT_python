
print "_+_+_+_+_+_+_ Exercise 1+_+_+_+_+_+_+_+_+_+_"
x= "esto es una pruebaddfgfdg https://docs.google.com/document21 testsfdsf"
#x="sfdsfe4 dsgfsdg fsdf "
n= x.find ("http")
key=0
#print (n)
url=""
if (n>0):
   while (key==0 ):
       if (x[n]!=" "):
           #print (x[n])
           url=url+x[n]
           n=n+1
       else:
           key=1
           #print ("nehhh")
   print ("La direccion url es:",url)
else:
   print ("no hay Url")


print "+_+_+_+_+_+_+_+_+_+_+_+_+Exercise 2+_+_+_+_+_+_+_+_+_+_+_+_"

z="Papafrita miau aba"
old="a"
new="5"

def replace(z, old, new):
    n=len(z)
    count=0
    newstr=""
    while (count<n):
        if z[count]==old:
            #print "secambia" , z[count]
            newstr=newstr+new
        else:
            #print "no pasa nada"
            newstr=newstr+z[count]
        count=count+1
    return (newstr)

phrase=replace(z,old,new)
print "La frase original es:", z
print "su reemplazo es:", phrase

print "+_+_+_+_+_+_+_+_+_+_+_+_+  Exercise 3   +_+_+_+_+_+_+_+_+_+_+_+_"



