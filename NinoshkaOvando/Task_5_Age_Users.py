from Package_test.Call_fuctions_package.Print_Age import print_ages_range
from Package_test.Modules_package.Calcule_Age import  calcule_age_hours, calcule_age_days, calcule_age_minutes

def main():
    print("###Curse Program###")
    amount= int(input("Which is the amount of user: "))
    users={}
    print("amount ", amount, type(amount) )

    if (type(amount) == int):
        amount_int=int(amount)
        print("amount_int ", amount_int)
        if(amount_int > 0):
            cont =0
            while(cont < amount_int):
                print("while ")
                name_usr = input('Enter the name of user {}: '.format(cont+1))
                age_usr = int(input('Enter the age of user {}: '.format(cont+1)))
                users[name_usr] = age_usr
                cont += 1
            if(len(users) >0):
                cont_1=1
                print('###########Starting###########')
                for k, v in users.items():
                    print('--------------------------------------------')
                    print('The user {}:{} is {}'.format(cont_1,k,print_ages_range(v) ))
                    print('The user {}:{} has {} years, {} days, {} hours, {} minutes.'.format(cont_1,k,v, calcule_age_days(v), calcule_age_hours(v),calcule_age_minutes(v) ))
                    print('--------------------------------------------')
                    cont_1+=cont_1
        else:
            amount = input("Your amount is not an integer or major than 0: ")
    else:
        print("The amount is not integer")

main()