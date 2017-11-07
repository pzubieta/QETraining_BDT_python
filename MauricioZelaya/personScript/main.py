from personScript.person import person
from personScript.employee import employee

x = person("dana", "florero", 4, 123)
y = employee("mauricio", "zelaya", 37, 12345, 777, "QE")
print(x.get_full_name())
print("\n\n###################################\n\n")
print("employee ID: %s" % y.get_employee_id())
print("employee full name: %s" % y.get_employee_name())
print("work in department: %s" % y.get_employee_department())