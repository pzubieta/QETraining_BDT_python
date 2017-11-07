import AlejandroAlcocer.practices.calculate_age_module as ages
import AlejandroAlcocer.practices.print_messages_module as prints
import AlejandroAlcocer.practices.calculate_perimeter as circ_perimeter
import AlejandroAlcocer.practices.calculate_area as circ_area

#############   FUNCTIONS   ################

def insert_users():
    """
    This method is a loop to collect user in a dictionary.
    :return: A dictionary fill with users.
    """
    more_users = True
    users_dic = {}
    while more_users == True:
        name = input('name: ')
        users_dic[name] = int(input('insert your age: '))
        if ask_for_more_users(): more_users = True
        else: more_users = False
    return users_dic

def ask_for_more_users():
    """
    This method ask if the user wants to add more users to a dictionary.
    :return: True if the users wants to and false if he doesn't.
    """
    add_more_users = True
    while add_more_users == True:
        more_users = input('is there any more users you wish to log y/n: ')
        if more_users.lower() == 'y':return True
        elif more_users.lower() == 'n': return False
        else: print('invalid option, try again.')



def calculate_all(users_dic):
    """
    This method calculate all the ages and prints to return a new dictionary with more values.
    :param users_dic: A dictionary with the users that are going to be calculated.
    :return: A new dictionary with a list of values for each user
    """
    new_users_dic = {}
    list_for_key = []
    for name in users_dic:
        list_for_key.append('age in minutes is: ' + str(ages.calculate_age_in_minutes(users_dic[name])))
        list_for_key.append('age in hours is: ' + str(ages.calculate_age_in_hours(users_dic[name])))
        list_for_key.append('age in days is: ' + str(ages.calculate_age_in_days(users_dic[name])))
        list_for_key.append(prints.print_messages(users_dic[name]))
        new_users_dic[name] = list_for_key
        list_for_key = []
    return new_users_dic

def circle_attributes():
    radius = int(input('Insert a radius of a circle: '))
    print('the area of the circle is: {}'.format(circ_area.calculate_area_circle(radius)))
    print('the perimeter of the circle is: {}'.format(circ_perimeter.calculate_perimeter_circle(radius)))

def run_names():
    dictionary = calculate_all(insert_users())
    for name in dictionary:
        print(name, dictionary[name])


def select_script():
    option = input('select script, options available are 1 and 2: ').strip()
    if option == '1': run_names()
    elif option == '2': circle_attributes()
    else: print('invalid option leaving the script')

#############   TESTS   ################
select_script()
