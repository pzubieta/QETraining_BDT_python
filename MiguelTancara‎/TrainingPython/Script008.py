# for loop statement
# for iterating_var in sequence:
#   statements

# Basic example
numbers = [6,5,3,8,4,2,5,4,11]
sum = 0
for val in numbers:
    #sum = sum + val
    sum += val
print ("The sum is: ", sum)


# Getting and printing the value of an array
genre = ["pop", "rock", "jazz"]

for i in range(len(genre)):
    print("I like", genre[i])