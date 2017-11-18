#function return URL
def retun_string(s):

    val = "https://"
    val2 = ".com"
    val3 = len(val2)
    limit=s.find(val)
    limit2=s.find(val2)
    limit3=limit2+val3
    if limit != -1:
         print(s[limit:limit3])
    else:
        print("There is no URL")
retun_string("I am in https://www.yahoo.com test")

#function replace(s, old, new)
def replace(s, old, new):
    words = s.split(old) # create an array split by old string -> array
    answer = new.join(words) # join all array elements by new string -> string
    print(answer)
replace("Mississippi", "i", "I")
replace("I love spom! Spom is my favorite food.Spom, spom, yum!", "om", "am")
replace("I love spom! Spom is my favorite food.Spom, spom, yum!", "o", "a")



