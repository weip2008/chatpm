def f(a, func): # pass a function as an argument
    return func(a)

def circleArea(r):
    from math import pi
    return pi*r*r

def squareArea(s):
    return s * s

def triangleArea(base, height):
    return base*height/2
    
if __name__ == '__main__':
    area = f(2, circleArea)
    print(area)
    area = f(2, squareArea)
    print(area)
