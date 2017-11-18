class Message:
    def __init__(self, from_number, time_arrived, text_of_SMS, has_been_viewed=False):
        self.has_been_viewed = has_been_viewed
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_sms = text_of_SMS

    def set_status(self, status):
        self.has_been_viewed = status