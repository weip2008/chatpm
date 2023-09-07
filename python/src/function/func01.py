def f(x,y,z):
    return x, y, z

def f1(x,y):
    print(x,y)

def add(x,y):
    return x+y

if __name__ == '__main__':
    a = f1(4,5)
    print(a)

    a,b = f(3,5,'hello')
    print(a,b)

    a = add(4,5)
    print(a)