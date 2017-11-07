def days_in_month():
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    option = str(input("Name of a month\n"))
    for i in range(12):
        if months[i] == option:
            print(months[i], " has ", days[i], "days")
            break
    else: print("None")
days_in_month()

