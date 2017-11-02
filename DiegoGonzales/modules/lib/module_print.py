def show_ege(ege, arg1="", arg2="", arg3="", arg4=""):
    if ege <= 12:
        print(arg1.upper()," You are a child: ", ege, " Edad en Dias ", arg2, " Edad en horas ", arg3, " Edad en minutos ", arg4)
    elif ege >= 13 and ege <= 17:
        print(arg1.upper(), " You are teenager: ", ege, " Edad en Dias ", arg2, " Edad en horas ", arg3, " Edad en minutos ", arg4)
    elif ege >= 18 and ege <= 29:
        print(arg1.upper(), " You are young: ", ege, " Edad en Dias ", arg2, " Edad en horas ", arg3, " Edad en minutos ", arg4)
    else:
        print(arg1.upper(), " You are adult: ", ege, " Edad en Dias ", arg2, " Edad en horas ", arg3, " Edad en minutos ", arg4)
