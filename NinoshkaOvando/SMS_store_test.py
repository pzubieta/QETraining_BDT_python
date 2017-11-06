from SMS_store import *
def main():
    sms_store = SMS_store()
    sms_store.add_new_arrival("5464564564", "1pm","text sms 1")
    sms_store.add_new_arrival("5464564564", "2pm", "text sms 1")
    sms_store.add_new_arrival("5464564564", "3pm", "text sms 1")
    print("count Message is:" , sms_store.message_count())

    a = [0, 88, 26, 3, 48, 85, 65, 16, 97, 83, 91]
    print(a)
    print("Message list: ")
    print(sms_store.get_message(0))
    print(sms_store.get_message(1))
    print(sms_store.get_message(2))
    print(sms_store.get_message(3))
    print("Unreald Indexes Message list: ")
    print(sms_store.get_unreald_indexes())
    print("Delete a item of SMS list: ")
    print(sms_store.delete(1))
    print(sms_store.get_message(0))
    print(sms_store.get_message(1))
    print(sms_store.get_message(2))
    print(sms_store.get_message(3))

    print("Delete all items of SMS list: ")
    print(sms_store.delete_all())
    print(sms_store.get_message(0))
    print(sms_store.get_message(1))
    print(sms_store.get_message(2))
    print(sms_store.get_message(3))





main()