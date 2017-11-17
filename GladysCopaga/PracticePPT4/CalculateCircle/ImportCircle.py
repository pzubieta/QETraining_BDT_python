import Module_areaCircle
import Module_perimeterCircle

def importCircle():
    radius = float(input("Please enter the radius to calculate are and permiter of a cicle: "))
    #if type(radius) == float:
    Module_perimeterCircle.perimeterCircle(radius)
    Module_areaCircle.areaCircle(radius)
    #else:
    #    print("Enter a valid value for radius")
importCircle()