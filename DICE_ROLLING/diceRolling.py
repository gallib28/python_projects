import random 
def display(roll1):
  print("result : "+str(roll1))

def roll():
      roll = random.randint(1,6)
      display(roll)
      return roll 
        
i = int(input("how many times you want to roll the dice?"))
if  i < 0 and i > 6:
  print("invalid input")
else:
  for x in range(i):
    roll()



