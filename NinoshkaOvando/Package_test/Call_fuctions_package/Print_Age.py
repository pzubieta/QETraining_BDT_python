def print_ages_range(age):
    aux_age=int(age)
    if(aux_age<= 12): return 'You are a child when you have {} ages'.format(aux_age)
    elif(aux_age<= 17 and aux_age>=13): return 'You are teenager when you have {} ages'.format(aux_age)
    elif (aux_age <= 29 and aux_age >= 18): return 'You are young when you have {} ages'.format(aux_age)
    elif (aux_age>= 30): return 'You are adult when you have {} ages'.format(aux_age)
    else:
        return 'You are not a child,teenager, young, adult  when you have {} ages'.format(aux_age)
