
def replace_chain(chain,old,new):
  if(chain.find(old)>=0):
     cadena=chain.split(old)
     chain=new.join(cadena)

     print(chain)
  else: print("String not found")
song="I love spom! Spom is my favorite food.Spom, spom, yum!"
replace_chain(song, "am", "@")
