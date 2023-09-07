"""
variable defined outside function is global by default
use global variable inside function need use global keyword to specify the variable
"""
globalVariable = 12 # by default this variable is global variable
x = 30
z = [1,2,3]
y = 10
def func(a, b, c):
    globalVariable = 100 # this is local variable
    global x
    x += 111 # function uses global variable value
    global y # declare global variable in function, it is not necessary to declare outside function
    y = "hello world!"
    return globalVariable

def func1(a,b):
    global y # without this declearation, y will be local variable
    y = 15  # 
    return y

def func2(a):
    z[0] += a 
    return z

def func3(a):
    y *= a # UnboundLocalError: local variable 'y' referenced before assignment
    return y

if __name__ == '__main__':
    print(globalVariable)
    print(func(1,2,3))
    print(x)
    print(f"y: {y}")
    print(func1(3,4))
    print(f"After func1 call, y: {y}")
    print(func2(3))
    # print(func3(4))
