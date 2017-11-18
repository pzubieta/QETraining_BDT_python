from CircleStatus.Area_Circle import area_of_circle
from CircleStatus.Perimeter_Circle import perimeter_circle
def main_cirgle():
    radio = int(input("insert a radio of the circle: "))
    if radio <= 0:
        print("insert a value major to zero")
    else:
        print("Radio = ", radio)
        print("Perimeter = ", perimeter_circle(radio))
        print("Area = ", area_of_circle(radio))

main_cirgle()