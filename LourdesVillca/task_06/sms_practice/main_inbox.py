import time
from task_06.sms_practice.SMS_store import SmsStore

my_inbox = SmsStore()


def generate_message():
    send_message = input("Would you like to send message (Y/N): \n")
    while send_message.lower() == "y":
        print("Send Message:\n")
        from_number = int(input("From number: "))
        time_arrived = time.strftime("%c")
        text_of_SMS = input("SMS text: ")
        my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
        send_message = input("Would you like to send other message (Y/N): \n")


def menu_options():
    print("-------------MENU OPTIONS SMS STORE----------------")
    print("1.- Send Message")
    print("2.- Get Total Messages")
    print("3.- Get Index for Unread Messages")
    print("4.- Get Message")
    print("5.- Delete Message given an Index")
    print("6.- Delete All Messages")
    print("7.- Exit")


def index_message():
    index = int(input("Insert an Index"))
    if type(index) == int:
        return index
    else:
        print("Inserted index is not a number")


def select_option():
    menu_options()
    try:
        option = int(input("select any option \n"))
        while option != 6:
            if option == 1:
                generate_message()
            elif option == 2:
                print("--Total Messages--", my_inbox.message_count())
            elif option == 3:
                print("Unread Messages", my_inbox.get_unread_indexes())
            elif option == 4:
                print("Message: ", my_inbox.get_message(index_message()))
            elif option == 5:
                my_inbox.delete(index_message())
            elif option == 6:
                my_inbox.delete()
            elif option == 7:
                exit()
            menu_options()
            option = int(input("select any option"))

    except ValueError:
        print("Invalid typed option")


select_option()
