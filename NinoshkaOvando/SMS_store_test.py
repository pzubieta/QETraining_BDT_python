from SMS_store import *
def main():
    sms_store = SMS_store()
    sms_store.add_new_arrival("5464564564", "1pm","text sms 1")
    sms_store.add_new_arrival("5464564564", "2pm", "text sms 1")
    sms_store.add_new_arrival("5464564564", "3pm", "text sms 1")
    sms_store.add_new_arrival("5464564564", "4pm", "text sms 1")
    sms_store.add_new_arrival("5464564564", "5pm", "text sms 1")
    sms_store.add_new_arrival("5464564564", "6pm", "text sms 1")
    sms_store.add_new_arrival("5464564564", "7pm", "text sms 1")
    print("count Message is:" , sms_store.message_count())

    print("Message list: ")
    sms_store.print_list_sms()
    print("Message list that has been viewerd: ")
    print(sms_store.get_message(0))
    print(sms_store.get_message(1))
    print(sms_store.get_message(5))
    print(sms_store.get_message(6))
    print("Unreald Indexes Message list: ")
    print(sms_store.get_unreald_indexes())
    sms_store.print_list_sms()
    print("Delete a item of SMS list: ")
    print(sms_store.delete(1))
    print(sms_store.delete(5))
    print(sms_store.delete(3))
    sms_store.print_list_sms()

    print("Delete all items of SMS list: ")
    print(sms_store.delete_all())
    sms_store.print_list_sms()





main()