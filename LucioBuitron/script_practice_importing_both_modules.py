from script_practice_modules_calculate_age import cal_age
from script_practice_modules_messages_age import category_age

#SOLICITAR EL NUMERO DE USUARIOS
number_users = int(input("Please enter a number of users:"))
dictionary_total_users = {}
print("\n")

#LLENAR EL DICCIONARIO SOLICITANDO EDAD Y NOMBRE
for i in range(number_users):
    name=input("Please enter the name of user #"+str(i+1)+":")
    age=int(input("Plese enter the age in years of user "+str(name)+":"))
    dictionary_total_users[name] = age
    print("\n")

for i in dictionary_total_users:
    print("Calculating the age of ",i)
    cal_age(dictionary_total_users[i])
    category_age(dictionary_total_users[i])
    print("\n")



