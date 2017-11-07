import time
class SMS:

    def __init__(self,msge,number):
        self.message=msge
        self.number=number
        self.state=0
        self.ctime=time.strftime("%c")

    # state = 1 viewed
    # state = 0 no-viewed
    def set_state(self, state_flag):
        self.state = state_flag

    def get_state(self):
        return self.state

    def get_message(self):
        return self.message

    def get_number(self):
        return self.number

    def get_time(self):
        return self.ctime
