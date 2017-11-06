import Person, Employee
def main():
    person_a = Person.Person("Mauge", "Arealo", 23, "343434232 cb")
    Person_b = Employee.Employee("Adrian", "Marcos", 34, "3345566 bn", 3435, "Sales")

    print(person_a.Name())
    print(Person_b.getEmployee())

main()