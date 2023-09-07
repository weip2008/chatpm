from math import pi

def circleArea(r, /):
    """
    this function return a circle area with a given radius.

    calling example:
    r = 2
    a = circleArea(r)
    """
    return r*r*pi


if __name__ == '__main__':
    r = 1
    r = 'hello'
    r = 2.4
    r = circleArea
    area = r(2.3)
    print(area)
    area = circleArea(1.3)
    print(area)