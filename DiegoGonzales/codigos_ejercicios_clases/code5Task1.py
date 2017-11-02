def task(operator, num1, num2):
    result = 0
    if operator == "+":
    	result = num1 + num2

    if operator == "-":
    	result = num1 + num2	

    if operator == "*":
    	result = num1 + num2
    	
    if operator == "/":
    	result = num1 + num2		
    
    if operator == "%":
    	result = num1 + num2

    cadena = num1," ",operator," ",num2," = "	
    return 	cadena, result

print(task("+", 10, 5))    