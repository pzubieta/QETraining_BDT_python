def replace(text, oldValue, newValue):
    text = text.split(oldValue)
    text = newValue.join(text)
    print(text)

replace("Mississippi", "i", "I")
replace("I love spom! Spom is my favorite food.Spom, spom, yum!" , "om", "am")
replace("I love spom! Spom is my favorite food.Spom, spom, yum!" , "o", "a")