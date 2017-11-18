def perform_operation(operator, number1, number2):
	Addittion="+"
	Sustraction="-"
	Multiplicacion="*"
	Division="/"
	Modulus="%"
	Exponent="**"
	Floord_Division="//"
	
	print("number1 =", number1)
	print("number2 =", number2)
	if(operator is Addittion):
		Results=number1+number2
		print ("Addittion is equals to" ,Results)
	elif(operator is Sustraction):
		Results=number1-number2
		print ("Sustraction is equals to", Results)
	elif(operator is Multiplicacion):
		Results=number1*number2
		print ("Multiplicacion is equals to", Results)
	elif(operator is Division):
		Results=number1/number2
		print ("Division is equals to", Results)
	elif(operator is Modulus):
		Results=number1%number2
		print ("Modulus is equals to", Results)
	elif(operator == Exponent):
		Results=number1**number2
		print ("Exponent is equals to", Results)
	elif(operator == Floord_Division):
		Results=number1//number2
		print ("Floord_Division is equals to", Results)
	else:
		print("Only use +, -, *, /, %, **, // as operator")
perform_operation("*", 2, 2)