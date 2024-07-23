correct = False 
import random
randNum = random.randint(1,100)


while correct != True  :
    g = int(input("enter your guess"))
    if g == randNum:
        print("correct")
        correct = True 
    elif g > randNum :
        print("too high")
    else:
        print("too low")

