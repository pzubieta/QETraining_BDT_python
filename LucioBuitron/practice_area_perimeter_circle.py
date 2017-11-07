#CRETE THE FUNCTION WITH TWO METHODS TO CALCULATE AREA AND PERIMETER
#These methods will be called from other file importing it

def cal_circle_area(ratio,pi):
    area=ratio*2*pi
    print("The AREA of the circle with radio "+str(ratio)+" is: ",area)

def cal_circle_perimeter(ratio,pi):
    perimeter=ratio*ratio*pi
    print("The PERIMETER of the circle with radio "+str(ratio)+" is: ",perimeter)




