import random

def display(roll1,count):
  print("result : "+str(roll1))
  print("counter = "+ str(count+1))

def roll():
    global total,count
    roll = random.randint(1,6)
    display(roll,count)
    total += roll
    count += 1
    return roll

total =0
count =0




i = int(input("how many times you want to roll the dice?"))
if  i < 0 and i > 6:
  print("invalid input")
else:
  for x in range(i):
    roll()



