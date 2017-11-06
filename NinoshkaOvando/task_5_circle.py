from package_geometry.Circle import calculate_area
from package_geometry.Circle import calculate_perimeter

def menu():
    print("Function circles")
    print("for Example: radius = 5 , perimetro is ",calculate_perimeter(5)," area = ",calculate_area(5))


    print("1 option :calculate area ")
    print("2 option :calculate perimeter")
def Main():

    menu()
    opt= int(input("Enter option: "))
    if(opt== 1):
       radio = int(input("Enter the radius: "))
       res= calculate_area(radio)
       print("Radius is ",res)
    elif(opt ==2):
        perim = int(input("Enter the radius: "))
        res= calculate_perimeter(perim)
        print("Perimeter is ",res)




Main()