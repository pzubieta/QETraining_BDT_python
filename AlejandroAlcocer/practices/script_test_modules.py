import QETraining_BDT_python.AlejandroAlcocer.practices.calculate_age_module as ages
import QETraining_BDT_python.AlejandroAlcocer.practices.print_messages_module as prints

def insert_users():
    more_users = True
    users_dic = {}
    while more_users == True:
        name = input('name: ')
        users_dic[name] = int(input('insert your age: '))
        if ask_for_more_users() == True:
            more_users == True
        else:
            calculate_all(users_dic)
            more_users == False

def ask_for_more_users():
    more_users = input('is there any more users you wish to log y/n: ')
    if more_users.lower() == 'y':return True
    elif more_users.lower() == 'n': return False
    else: return 'invalid option'


def calculate_all(users_dic):
    for name in users_dic:
        ages.calculate_age_in_minutes(users_dic[name])
        ages.calculate_age_in_hours(users_dic[name])
        ages.calculate_age_in_days(users_dic[name])
        prints.print_messages(users_dic[name])



insert_users()