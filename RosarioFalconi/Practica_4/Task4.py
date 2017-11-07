import RosarioFalconi.Practica_4.Task4_Msg as msg
import RosarioFalconi.Practica_4.Task4_Calculate_Age as ca

def calling_module_functions (edad):
    if not edad.isnumeric():
        print("Edad no valida")
    else:
        age2 = int(edad)
        msg.age_message(age2)
        ca.age_days(age2)
        ca.age_hours(age2)
        ca.age_minutes(age2)

#age = input ("Ingrese la edad:")
#calling_module_functions(age)