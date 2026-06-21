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

if n not in youdict: 
        print('''Invalid choice \nremember you are playing snake water gun game ''')

        exit()

you = youdict[n]

print (f"your choice = {reversedict[you]} \n computer chose = {reversedict[computer]}")

if (computer == you):
    print ("DRAWN match ")\
    
else:
    if ((you-computer)==-1 or (you-computer) == 2):
        print(" you win ")
        
    elif((you-computer)==-2 or (you- computer)==1):
        print("You loose")