#SET THE REQUIRED STRING VARIABLES FOR THE FUNCTION
#Message
statement=input("Please enter the message with at least 5 words:")

#Word to find
origin_word=input("Please enter the word you want replace to: ")

#Word to replace
target_word=input("Please enter the word you want replace for: ")
print("\n")

def replace_words(statement,origin_word,target_word):

    updated_message=statement.replace(origin_word, target_word)

    if updated_message.__contains__(target_word):
        print("Original message is: ",statement)
        print("Message after replacement is: ", updated_message)
    else:
        print("The given word was not found in the message. Sorry")

replace_words(statement, origin_word, target_word)
