from message_by_edad import message_by_age
from calculate_age import calculate_age

def add_userTo_dic(dictionary,name,age):
     dictionary[name]=age

def print_age_min_h_d(dict):
#    print (dict)
    for key, value in dict.items():
        age_dhm = calculate_age(value)
#        name = dict[value]
        name = key
        print ("Name: ",name)
        print(" -> has age in days :", age_dhm[0], "days")
        print(" -> has age in hours :", age_dhm[1], "hours")
        print(" -> has age in minutes :", age_dhm[2], "minutes")
        print (message_by_age(value))


def add_user(number_u):
    count = 0
    dictionary = {}
    if number_u> 0:
        while count < number_u:
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            add_userTo_dic(dictionary,name,age)
            count +=1
    else:
        dictionary = None
    print (dictionary)
    print_age_min_h_d(dictionary)

number_users = int(input("Enter user numbers to add: "))
add_user(number_users)
