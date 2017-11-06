from SMS_Module.SMS import SMS

inbox_sms = SMS()
inbox_sms.add_new_arrival(1, "10:10:10 AM", "Hola esto es un demo")
inbox_sms.add_new_arrival(2, "10:20:30 AM", "Como es loco estas ahi")
inbox_sms.add_new_arrival(3, "10:30:40 AM", "Che estamos aqui por el correo")
inbox_sms.add_new_arrival(4, "10:40:50 AM", "Esto es una joda")
inbox_sms.add_new_arrival(5, "10:50:60 AM", "Es porque estamos tomando unas chelas")
inbox_sms.add_new_arrival(6, "11:10:50 AM", "Compren para mi mas unas chelas porfavor cumpas, cambio y fuera.")

print(inbox_sms.message_count())
inbox_sms.get_unread_index()
print(inbox_sms.get_Message(4))
inbox_sms.get_unread_index()
inbox_sms.delete(5)
inbox_sms.get_unread_index()
print(inbox_sms.clear())
print(inbox_sms.get_unread_index())