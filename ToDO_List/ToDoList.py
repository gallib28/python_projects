import 
from collections.abc import ItemsView
toDo =[] 
class mission :
  name 

  def __init__(self, task ,introDate,finishedDate):
    self.task = task
    self.introDate = introDate
    self.finishedDate = finishedDate










def view(t) :
  for i in toDo :
    print(i) 

def add(list,item):
  if check(item)==True:
    list.append(item)

def delete(list,item):
  if check(item)==True and item in list:
    list.remove(item.index(item))

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




def checkTimeLeft(m):
  for i in toDo:
    if m.finishedDate<5 :
       printobj(m)
       print("need to finish this task ")



while True:
    my_job()
    time.sleep(604800)