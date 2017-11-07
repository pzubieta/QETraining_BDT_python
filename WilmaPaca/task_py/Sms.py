class Sms_message():
    def __init__(self, from_number = None,time_arrived =None,text_sms = ""):
        self.phone = from_number
        self.time_sms = time_arrived
        self.message = text_sms
        self.state = False
# Get every parameter of sms
    def getPhone(self):
        return self.phone
    def getTimeSms(self):
        return self.time_sms
    def getMessage(self):
        return self.message
    def getState(self):
        return self.state

# Set values for every parameter
    def setPhone(self,number):
        self.phone = number
    def setTimeSms(self, new_time):
        self.time_sms = new_time
    def setMessage(self,new_message):
        self.message = new_message
    def setState(self, new_state):
        self.state = new_state