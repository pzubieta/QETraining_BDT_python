#Remplace a char in a word
def remplace_char(text_example, char_old, chart_new):
    result=""
    result_aux=""
    index_aux = text_example.find(char_old)
    if (index_aux == -1):
        return 'There is not any {} char on {} word '.format(char_old,text_example)
    else:
        cont = 0
        while(cont <len(text_example)):
            if(text_example[cont]==char_old):
                result_aux= result_aux+chart_new
            else:
                result_aux = result_aux+text_example[cont]

            cont += 1

        return 'The new word is "{}". Old word "{}" remplaced "{}" to "{}"'.format(result_aux,text_example,char_old ,chart_new )

def test_emplace_char():
    print(remplace_char("Misisipi", "i", "I"))

def main():

    print("Welcome to Remplace program")
    print("Example:")
    test_emplace_char()
    print("To start, you can input an Word with old chat remplace with new char")
    print("Word: Misisipi")
    print("Old char: i")
    print("New char: I")
    text_example = str(input("Enter a word: "))
    char_old = str(input("Enter an old char: "))
    chart_new = str(input("Enter a new char: "))
    print(remplace_char(text_example, char_old, chart_new))
main()