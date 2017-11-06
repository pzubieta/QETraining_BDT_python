def string_order_number(s):
    alphabet = {}
    s = s.lower()
    s_array = list(s)

    s_array.sort()

    for index in range(len(s_array)):
        element = s_array[index]
        if element == " ":
            continue
        counter = s_array.count(element)
        alphabet[element] = counter

    print(alphabet)
string_order_number("marcEla ines  barrionuevo zambrana")