import pyodbc
import pandas 
from collections.abc import ItemsView
import  tkinter as tk
import datetime

curr_date = datetime.datetime.now()
print(curr_date)



class Mission : 
  name="name of task"
  dueDate = "00-00-0000"
  createDate = "00-00-0000" 
  def __init__(self, task ,introDate,finishedDate):
    self.name = task
    self.introDate = introDate
    self.dueDate = finishedDate

  def getDueDate():
    return this.dueDate 
  

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
    size += 1 

def deleteTask(list,mission):
  if helpFind(mission)==True and mission in list:
    list.remove(item.index(mission))
    size -= 1 


def printobj(mission):
  print(mission.name,'\n')
  print(mission.introDate,'\n')
  print(mission.finishedDate,'\n')


def checkTimeLeft(toDo):
  for i in toDo:
    if toDo[i].finishedDate<5 :
       print(f"need to finish this task ASAP: \n
       {printobj(toDo[i])} ")


# for timing the program 
while True:
    checkTimeLeft(toDo)
    time.sleep(604800)
    

toDo = [] 
size = 0 
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


