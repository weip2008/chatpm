def calculate(a, b):
    yield a + b
    yield a - b
    yield a * b
    yield a / b

if __name__ == '__main__':
    g = calculate(5,4)
    print(g)
    for i in g:
        print(i, end=', ') 