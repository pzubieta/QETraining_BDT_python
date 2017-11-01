variable_number_1 = 50
variable_number_2 = 5
variable_string = 'this is a string variable :'
lists = ['a', 'b', 'c', 'd']
list_member = 'a'

print ('======OPERATORS======')
print ('the values that we are using value 1: %d , value 2 : %d ' % (variable_number_1, variable_number_2))
print ('using the addition operator ' + str(variable_number_1 + variable_number_2))
print ('using the subtraction operator ' + str(variable_number_1 - variable_number_2))
print ('using the multiplication operator ' + str(variable_number_1 * variable_number_2))
print ('using the division operator ' + str(variable_number_1 / variable_number_2))
print ('using the module operator ' + str(variable_number_1 % variable_number_2))
print ('using the exponent operator ' + str(variable_number_2 ** 2))
print ('using the floor operator on variable 2 :' + str(variable_number_2 // 2))

print ('======MEMBERSHIP OPERATORS======')
print ('list contain' + str(lists))
print ('finding \"' + str(list_member) + '\" in the list')
if list_member in lists:
    print (str(list_member) + ' is in the list')
