def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2  
def div(num1,num2):
    return num1/num2
def mod(num1,num2):
    return num1%num2  


available = True
def calc():
    
    print("welcome to calculator")
    num1 = float(input("enter first number "))
    num2 = float(input("enter second number "))
    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    print("5. mod")
    print("6. exit")
    c = int(input("what action you want to take?"))
    if c==1:
        print(add(num1,num2))
    elif c==2:
        print(sub(num1,num2))
    elif c==3:
        print(mul(num1,num2))
    elif c==4:
        print(div(num1,num2))
    elif c==5:
        print(mod(num1,num2))
    else:
        print("exit")
        available = False 
        return available


calc()

  



