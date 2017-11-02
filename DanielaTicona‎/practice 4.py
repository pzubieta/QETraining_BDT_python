
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

alpha ={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,' ':0}
r="A mi me GustA LA SAlchipApaAA"
y= r.lower()
print y
for i in range (len(y)):
    if alpha.has_key(y[i]):
        word=y[i]
        alpha[word]= alpha[word]+1
        #print "esta el valor", word, "y este es el valor", alpha[word]
    else:
        print "nuu hay"
print "the String is:", y
print alpha


#print alpha.keys(), alpha.values()



