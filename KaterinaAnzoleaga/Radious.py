def area_of_circle (r):
    return 3.1416*r**2

success = 1
while success:
    radio = float (input("Ingres el radio del circulo: "))
    if radio >= 10:
        print ("El área de un circulo de radio ", radio, "es: ", area_of_circle(radio))
    else:
        print ("Ingrese un número mayor")
        break



