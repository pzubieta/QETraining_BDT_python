'''Global variables :) '''
str = "This is a simple text used to verified the correct functionality of str_replacing function. Adding a Z and a z"
abc = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'y':0,'z':0}

print('\n======= Search an url into a given text ======\n')
search = "i"
rpl = "0"
def str_searching():
    global str
    targ="http"
    ini = 0
    fin = 0
    if str.find(targ)>0 :
        ini = str.find(targ)
        new_str = str[ini:len(str)]
        fin = new_str.find(' ')
        print('There is a url in text ', new_str[0:fin])
    else:
        print ("There is not a url in text")
str_searching()

print('\n======= Replacing a letter from a string ======\n')
def str_replacing():
    global search
    global rpl
    global str
    print('OLD text: \n', str)
    new_str=" "
    glue=" "
    i=0
    for i in range (len(str)):
        if str[i].lower() == search:
            new_str= new_str + glue.join(rpl)
        else:
            new_str= new_str + glue.join(str[i])
        i += 1
    print('NEW text: \n', new_str)
str_replacing()

print('\n======= Count how many times a letter is repeated on a text ======\n')
def str_countAlpha():
    global str
    global abc
    i=0
    for i in range (len(str)):
        if str[i].lower() != " ":
            if str[i].lower() in abc:
                abc[str[i].lower()] +=1
    print (abc)

str_countAlpha()
