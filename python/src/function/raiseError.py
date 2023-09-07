"""
❗️⚡️User may pass wrong argument to function.
raise Error when bad thing happens.
"""
from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError(f"Please check radius data type. type is {type(r)}")
    if r<0:
        raise ValueError(f"Radius cannot be neigative. but r={r}")
    return r * r * pi

def circleArea(r):
    return r*r*pi


if __name__ == '__main__': 
    面积 = circleArea(2-3j) # 😢without check the calling argument, give you meaningless output
    print(f'圆面积={面积}')
    x = circleArea(-3) # 😢without check the calling argument, give you meaningless output
    print(x)
    try:
        x = circle_area(2-3j) # 😢without check the calling argument, give you meaningless output
        print(x)
    except Exception as err:
        print(err)
    try:
        x = circle_area(-3) # 😢without check the calling argument, give you meaningless output
        print(x)
    except Exception as err:
        print(err)
    x = circle_area("hello") # 😢without check the calling argument, give you meaningless output
    print(x)
    print("Done.")