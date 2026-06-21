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

if (computer == you):
    print("Match draw ")

else :
    if (computer == 1 and you == 0):
        print ("you win ")

    elif (computer == 1 and you == -1):
        print("You win ")
         
    elif (computer == -1 and you == 0):                                       
        
            print("You loose ")
        
    elif (computer == -1 and you == 1):
            print("You win ")
         
    elif (computer == 0 and you == -1):
            print("You win ")
        
    elif (computer == 0 and you == 1):
            print("You loose ")
    
    else:
          print("Something went wrong ")

