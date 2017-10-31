def days_in_month(mount):
 if(type(mount)==  str):
    mount_aux = str(mount)
    list_31_days= ['January','March' , 'May', 'July', 'August', 'October', 'December']
    list_30_days = ['April', 'June','September', 'November' ]
    cont1 =0
    cont2 = 0
    if (mount_aux == "February"):
        return 'Number days is 28 of {} '.format(mount_aux)
    else:
        while(cont1 <7 ):
            if (mount_aux == list_31_days[cont1]):
                return 'Number days is 31 of {} '.format(mount_aux)
            cont1+=1
        while (cont2 < 4):
            if (mount_aux == list_30_days[cont2]):
                return 'Number days is 30 of {} '.format(mount_aux)
            cont2 += 1
    return None

def test_days_in_month():
    list_mounts = ['January', "February", 'March', 'May', 'July', 'August', 'October', 'December', 'April', 'June','September', 'November' ]
    for val in list_mounts:
        print(days_in_month(val))
def Main():

    test_days_in_month()
    print("Return the number of days of a month ")
    print('January', "February", 'March', 'May', 'July', 'August', 'October', 'December', 'April', 'June','September', 'November')
    val= input("Enter a month: ")
    print(days_in_month(val.capitalize()))

Main()