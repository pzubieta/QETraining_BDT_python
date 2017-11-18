from area import calculate_area
from perimeter import calculate_perimeter

# insert the value of radius
radius = int(input("insert the radius of the circle \n"))
print("===The area of the circle is {}".format(calculate_area.calculate_area(radius)))
print("===The perimeter of the circle is {}".format(calculate_perimeter.calculate_perimeter(radius)))
