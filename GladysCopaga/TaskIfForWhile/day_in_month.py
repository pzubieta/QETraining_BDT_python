def days_in_month(month):
	month_31 = ["Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre"]
	month_30 = ["Abril", "Junio", "Septiembre", "Noviembre"]
	month_28 = ["Febrero"]
	if month in month_31:
		print ("The month has 31 days")
	elif  month in month_30:
		print ("The month has 30 days")
	elif  month in month_28:
		print ("The month has 28 days")
	else:
		print ("Enter a valid month")
days_in_month("Septiemb")