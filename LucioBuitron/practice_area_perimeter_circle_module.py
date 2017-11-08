#IMPORTED SOME METHODS OF A MODULE
from practice_area_perimeter_circle import cal_circle_area, cal_circle_perimeter

#ASKING RATIO FOR CIRCLE
ratio=int(input("Please enter the radio size of the circle: "))
pi=3.1416
print("\n")

#CALLING TO METHODS OF IMPORTED MODULE
cal_circle_area(ratio,pi)

cal_circle_perimeter(ratio,pi)
