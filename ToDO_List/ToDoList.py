import pyodbc
from collections.abc import ItemsView
toDo =[] 


class mission : 
  def __init__(self, task ,introDate,finishedDate):
    self.task = task
    self.introDate = introDate
    self.finishedDate = finishedDate

def helpFind(item):
  if type(item) != str:
    print("invalid input")
    return False 
  else:
    return True 

def viewTask(mission) :
  for i in toDo :
    print(i) 

def addTask(list,mission):
  if helpFind(mission)==True:
    list.append(mission)

def deleteTask(list,mission):
  if helpFind(mission)==True and mission in list:
    list.remove(item.index(mission))

def printobj(mission):
  print(mission.task,'\n')
  print(mission.introDate,'\n')
  print(mission.finishedDate,'\n')

def checkTimeLeft(toDo):
  for i in toDo:
    if toDo[i].finishedDate<5 :
       print(f"need to finish this task ASAP: \n
       {printobj(toDo[i])} ")



while True:
    checkTimeLeft(toDo)
    time.sleep(604800)
    



# while True :
#   print("1. view")
#   print("2. add")
#   print("3. delete")
#   print("4. exit")
#   c = int(input("what action you want to take? \n"))

#   if c==1:
#     view(toDo)
#   elif c==2:
#     add(toDo,input("enter item"))
#   elif c==3:
#     delete(toDo,item) 
#   else :
#     print("exit")
#     break


