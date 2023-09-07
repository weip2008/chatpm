class myerror(Exception):
    pass

from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise myerror(f"Please check radius data type. type is {type(r)}")
    if r<0:
        raise ValueError(f"Radius cannot be neigative. but r={r}")
    return r * r * pi

if __name__ == '__main__':
    try:
        x = circle_area(2-3j) 
        print(x)
    except myerror as err:
        print(f'{type(err).__name__}: {err}')
    except ValueError as err:
        print(f'{type(err).__name__}: {err}')

    try:
        x = circle_area(-3) 
        print(x)
    except myerror as err:
        print(f'{type(err).__name__}: {err}')
    except ValueError as err:
        print(f'{type(err).__name__}: {err}')

 