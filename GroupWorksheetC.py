def mystery1(a):
   print (a * 10)


def main1():
    x = 5
    mystery1(x)
    

def mystery2(a):
    b = a + 1
    return 10 * b

def main2():
    y = 6
    print(mystery2(y))
    
    
    
def mystery3(g):
    h = g + 1
    print(h)
    return 10 * g

def main3():
    y = 5
    z = mystery3(y)
    print(z)
    

def mystery4(a):
    return a + 1

def main4():
    mystery4(41)
    
    
    
def mystery5(a, b, c):
    return a + b + c

def main5():
    x = 3
    y = 7
    answer = mystery5(x, y , x)
    print(answer)
    
    
def mystery6(a):
    return a - 1, a + 1

def main6():
    w = 4
    x, y = mystery6(w)
    print(x, y)


def mystery7(a, b):
    print(a, b)

def main7():
    a = 7
    b = 3
    mystery7(b, a)


def mystery8(x):
    value = 2 * x
    return value

def main8():
    value = 3
    answer = mystery8(value)
    print(answer, value)



def mystery9(x):
    return x * 10
    print(x * 2)
    
def main9():
    y = 3
    answer = mystery9(y)
    print(answer)
    
    
    
def mystery10(x):
    print(x * 3)
    
def main10():
    y = 4
    z = mystery10(y)
    print(z)
    

def variable1(x):
    x = 3              # Value of x
    y = 2.65           # Value of y
    response = "yes"
#This will evaluate the following Boolean Expressions
    print(x == 3) #Expression 11
    print(x < 3)  # Expression 12
    print(x <= 3) # Expression 13 
    print(x != y) # Expression 14
    print(x >= y) # Expression 15
    print(x == int(y)) # Expression 16
    print(x == round(y)) # Expression 17
    print(response == "yes") # Expression 18
    print(response[0].lower() == "y") # Expression 19
    print("No" < response) # Expression 20
    print(type(x) == type(y)) # Expression 21
    print(type(x) == type(0)) #  Expression 22