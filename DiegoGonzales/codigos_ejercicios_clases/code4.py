def myfunction(num):
	""" My documentation of the code """
	cont = 0 
	while cont <= num:
		print(cont)
		cont=cont+1

def suma(num1, num2):
	suma = num1 + num2
	return suma


def print_lyrics():
	print("I am a test, and I am okay.")
	print("I sleep all nigth and I work all day.")


result = suma(5,10)
print (result)
myfunction(10)    
print_lyrics()