def practice_one(number_one, number_two, operator):
	print('######### PRACTICE ONE ##########')
	operators = {'+', '-', '*', '/', '%', '**', '//'}
	if operator in operators:
		if operator == '+': print ('the operator is add and the result is:', number_one + number_two)
		elif operator == '-': print ('the operator is rest and the result is:', number_one - number_two)
		elif operator == '*': print ('the operator is times and the result is:', number_one * number_two)
		elif operator == '/': print ('the operator is div and the result is:', number_one / number_two)
		elif operator == '%': print ('the operator is mod and the result is:', number_one % number_two)
		elif operator == '**': print ('the operator is times and the result is:', number_one ** number_two)
		elif operator == '//': print ('the operator is floor division and the result is:', number_one // number_two)
	else: print('not a valid argument')

def practice_two(number_one, number_two, operator,goal_number):
	print('######### PRACTICE TWO ##########')
	operators = ['+', '-', '*', '/', '%', '**', '//']
	if operator in operators:
		if operator == '+': 
			print ('the operator is add and the result is:', number_one + number_two)
			print(logical_method(number_two+number_two, goal_number))
		elif operator == '-': 
			print ('the operator is rest and the result is:', number_one - number_two)
			print(logical_method(number_two+number_two, goal_number))
		elif operator == '*': 
			print ('the operator is times and the result is:', number_one * number_two)
			print(logical_method(number_two+number_two, goal_number))
		elif operator == '/': 
			print ('the operator is div and the result is:', number_one / number_two)
			print(logical_method(number_two+number_two, goal_number))
		elif operator == '%': 
			print ('the operator is mod and the result is:', number_one % number_two)
			print(logical_method(number_two+number_two, goal_number))
		elif operator == '**': 
			print ('the operator is times and the result is:', number_one ** number_two)
			print(logical_method(number_two+number_two, goal_number))
		elif operator == '//': 
			print ('the operator is floor division and the result is:', number_one // number_two)
			print(logical_method(number_two+number_two, goal_number))
	else: print('not a valid argument')

def logical_method(x, goal_number):
	logical_options = ['==', '!=', '>', '<', '>=', '<=', '=', '+=', '-=', '*=', '/=', '%=']
	list_of_results = []
	for operator in logical_options:
		if operator is '==': 
			if x == goal_number: list_of_results.append('Values are not equal and the operator was ==')
			else: list_of_results.append( 'Value are not equal and the operator was ==')
		elif operator == '!=': 
			if x != goal_number: list_of_results.append('Values are not equal and the operator was !=')
			else: list_of_results.append( 'Value are equal and the operator was !=')
		elif operator == '>': 
			if x > goal_number: list_of_results.append('Value is grater')
			else: list_of_results.append( 'Value is lower')
		elif operator == '<': 
			if x < goal_number: list_of_results.append('Value is lower')
			else: list_of_results.append( 'Value is grater')
		elif operator >= '>=': 
			if x >= goal_number: list_of_results.append('Value is grater or equal')
			else: list_of_results.append( 'Value is lower')
		elif operator == '<=': 
			if x <= goal_number: list_of_results.append('Value is lower or equal')
			else: list_of_results.append( 'Value is higher')
		elif operator == '=':
			y = goal_number
			list_of_results.append('A value was assigned {}'.format(y))
		elif operator == '+=':
			y = x
			y += 1
			list_of_results.append('the value was plus one {}'.format(y))
		elif operator == '-=':
			y = x
			y -= 1
			list_of_results.append('the value was reduce one {}'.format(y))
		elif operator == '*=':
			y = x
			y *= 2
			list_of_results.append('the value was multiply by 2 {}'.format(y))
		elif operator == '/=':
			y = x
			y /= 2
			list_of_results.append('the value was devided by 2 {}'.format(y))
		elif operator == '%=':
			y = x
			y %= 2
			list_of_results.append('the value was mod by 2 {}'.format(y))
	return list_of_results



practice_two(7, 7, '+', 14)
practice_one(6, 6, '+')
practice_one(6, 6, '-')
practice_one(6, 6, '*')
practice_one(6, 6, '/')
practice_one(6, 6, '%')
practice_one(6, 6, '**')
practice_one(6, 6, '//')
practice_one(6, 6, '00')