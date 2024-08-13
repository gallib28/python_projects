import 
from collections.abc import ItemsView
toDo =[] 
class mission : 
  def __init__(self, task ,introDate,finishedDate):
    self.task = task
    self.introDate = introDate
    self.finishedDate = finishedDate



def view(mission) :
  for i in toDo :
    print(i) 

def add(list,mission):
  if check(mission)==True:
    list.append(mission)

def delete(list,mission):
  if check(mission)==True and mission in list:
    list.remove(item.index(mission))

def check(item):
  if type(item) != str:
    print("invalid input")
    return False 
  else:
    return True 



while True :
  print("1. view")
  print("2. add")
  print("3. delete")
  print("4. exit")
  c = int(input("what action you want to take? \n"))

  if c==1:
    view(toDo)
  elif c==2:
    add(toDo,input("enter item"))
  elif c==3:
    delete(toDo,item) 
  else :
    print("exit")
    break


def printobj(mission):
  print(mission.task)
  print(mission.introDate)
  print(mission.finishedDate)

def checkTimeLeft(toDo):
  for i in toDo:
    if toDo[i].finishedDate<5 :
       printobj(toDo[i])
       print("need to finish this task ")



while True:
    checkTimeLeft(toDo)
    time.sleep(604800)
    
