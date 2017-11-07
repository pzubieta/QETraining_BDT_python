import logging

class Person:
    logging.basicConfig(filename="myLog.log", level=logging.DEBUG)
    #logging.basicConfig(filename="myLog.log", level=logging.INFO)
    logging.info("Program started")

    def __init__(self, first, last):
        logging.info("initializing parameters")
        logging.debug("initializing firstname variable with value : {}".format(first))
        self.firstname = first
        logging.debug("initializing lastname variable with value: {}".format(last))
        self.lastname = last

    def name(self):
        logging.info("returning the name",)
        name = self.firstname + " " + self.lastname
        logging.debug("returning the name: {} {}".format(self.firstname, self.lastname))
        return name


class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        logging.info("returning the employee", )
        #super().__init__(first, last)
        self.staffnumber = staffnum

    def getEmployee(self):
        logging.debug("returning the employee: {} {}".format(self.name(), self.staffnumber))
        return self.name() + "," + self.staffnumber


x = Person("Marge", "Simpsons")
y = Employee("Homer", "Simpsons", "1007")

print(x.name())
print(y.getEmployee())