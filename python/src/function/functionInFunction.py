def parentFunc(x, y, z):
    def childFunc(a, b):
        return a/b
    c = childFunc(x,y)
    c = childFunc(c, z)
    return c+z


j = parentFunc(3,4,5)
print(j)

def quadratic(a, b, c):
    def f(x):
        return a*x*x+b*x+c
    return f

func = quadratic(3, -4, 4)
print(type(func))
j = func(6.7)
print(f'j = {j:.2f}\n')
print(type(j))