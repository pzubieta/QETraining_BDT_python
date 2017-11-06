class SMS_message:
    def __init__(self, has_been_viewerd, from_number, time_arrived, text_of_SMS):
        self.has_been_viewerd = has_been_viewerd
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS

    def get_has_been_viewerd(self):
        return self.has_been_viewerd

    def set_has_been_viewerd(self, value):
        self.has_been_viewerd= value

    def get_from_number(self):
        return self.from_number

    def get_time_arrived(self):
        return self.time_arrived

    def get_text_of_SMS(self):
        return self.text_of_SMS
