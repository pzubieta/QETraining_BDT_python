import area_circulo
import perimetro_circulo


def circulo(radio):

    if type(radio)!=type("a"):
        print("El radio tiene que ser un numero")
    else:
        a=float(area_circulo.area_circulo(radio))
        b=float(perimetro_circulo.perimetro_circulo(radio))
        print("El area del circulo es: ",a)
        print("El perimetro del circulo: ",b)


radius=float(input("Inserte el radio del circulo: " ))
circulo(radius)