def count_letters(statement, char):
  count = 0
  for i in statement:
    if char == i:
      count += 1
  return count

#DEFINE THE VARIABLE TEXT TO HANGLE MESSAGE WITH CAPITAL OR NON CAPITAL LETTERS SEPARATELY FOR TESTING PURPOSES
statement=input("Please enter the message where the letters will be count:")
dictionaryCapital={}
dictionaryNoCapital={}

#ITERATE FOR ALL WORDS IN ORDER TO COUNT THEM USING OUR FUNCTION
for i in statement:
    dictionaryCapital[i]=count_letters(statement,i)

#ITERATE FOR ALL WORDS IN ORDER TO COUNT THEM USING OUR FUNCTION BUT CONVERTING ALL TO LOWER CASE TO AVOID COUNT REPEATLY
for i in statement.lower():
    dictionaryNoCapital[i]=count_letters(statement,i)

print("\n")
print("This is the count of each letters in the message with Capital letters:")
print (dictionaryCapital)
print("\n")
print("\n")
print("This is the count of each letters in the message with No Capital letters:")
print (dictionaryNoCapital)
