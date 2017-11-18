a = "Hey"
b = "Hey there!"
c = "742 Evergreen Terrace"
d = "1234"
e = "'How long is a piece of string?' he asked"
f = "'!$*#@ you!' she replied"

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

a = "Hey"
print(len(a))

print(1+2)
print("1"+"2")

a = "pic123"
b = "21344"
print (a.isnumeric())
print (b.isnumeric())

e = "Once again he asked \"How long is a piece of string?\""
print(e)

msg = "ATTENTION!\rFor those about to rock, we salute you!"
print(msg)

msg = """This string
spans
multiple lines"""
print(msg)

msg = '''This string
spans
multiple lines'''
print(msg)


planet = "Jupiter"
print(planet[2])


planet = "Jupiter"
print(planet[2:5])

print("Hello %s, you scored %i out of %i" % ("Homer", 3, 100))