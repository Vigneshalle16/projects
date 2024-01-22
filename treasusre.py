print(" Welcome to Trreasue Island")
choice_1 = input ('which way? "left" or "right".').lower()
if choice_1 == "left" :
   a = input('you are at lake, type "swim" or "wait".').lower()
   if a == "swim" :
      b = input('type color, "red" , "blue" or "yellow".').lower()
      if b == "yellow" :
         print("you win")
      else :
         print ("game over")
   else :
    print("game over")
else : 
   print ("game over")
