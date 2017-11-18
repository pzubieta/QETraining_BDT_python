list = [1, 5, 7, 10]


def adding_a_list(list):
    result = 0
    last_value = 0
    for value in list:
        last_value = result
        result += value
        if result > 35:
            print ('we exceeded ,come back to ' + str(last_value))

        else:
            print ('this is the value that works {}'.format(result))


adding_a_list(list)
