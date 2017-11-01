#import PZPrint_Age_mins
#import PZPrint_4_ages

def fillUsers():
    usersAmount = eval(input("Enter the amount of users:"))
    print (type(usersAmount))

    count = 1
    hshUsersName = {}
    hshUsersAge = {}

    while count <= usersAmount:
        hshUsersName[count] = input("Enter the user "+str(count)+" name:")
        hshUsersAge[count] = eval(input("Enter the user "+str(count)+" age:"))
        count +=1
    for k in hshUsersName.keys():
        print (hshUsersName[k])

fillUsers()