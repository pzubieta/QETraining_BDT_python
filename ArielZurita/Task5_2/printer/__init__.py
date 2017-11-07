from ArielZurita.Task5_2.areaCircle.calculateAreaCircle import calculateAreaCircle
from ArielZurita.Task5_2.perimeterCircle.calculatePerimeter import calculatePerimeterCircle
def printResults():
    radius = int(input("Enter the radius \n"))
    resArea = float(calculateAreaCircle(radius))
    resPerimeter = float(calculatePerimeterCircle(radius))
    print("Area is %d" %resArea)
    print("Perimeter is %d" % resPerimeter)

printResults()
