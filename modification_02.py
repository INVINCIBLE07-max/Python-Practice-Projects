# SNAKE WATER GUN            

'''
-1 = water 
0 = gun 
1 = snake'''


'''water kills gun and snake 
gun kills snake 
snake drinks/kills water 

or 

# Rules:
# Water beats Gun
# Gun beats Snake
# Snake beats Water
'''


import random 

computer = random.choice([1,-1,0])

youdict = {"s":1 , "g" : 0 , "w" : -1}

reversedict = {-1 : "water" , 0 : "gun" , 1 : "snake" }

n = input("Enter your choice ")

you = youdict[n]

print (f"your choice = {reversedict[you]} \n computer chose = {reversedict[computer]}")

maindic = {1:-1 , -1:0 , 0:1}

if (maindic[you]==computer):
      print("You win ")

else:
      print("You loose ")
