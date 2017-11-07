class ExceptionAmazon(Exception):

    def __init__(self, message="Null"):
        self.message = message

    def getException(self):
        try:
            raise ExceptionAmazon(self.message)
        except ExceptionAmazon as error:
            return "Error: " + error.message + " _" + self.__class__.__name__