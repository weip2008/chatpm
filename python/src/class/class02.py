class Robot(object):
    def __init__(a, name): # first positional argument is self (this)
        a.name = name

    def __repr__(self): # return a string to represent the object
        return self.name


if __name__ == '__main__':
    john = Robot('john')
    print(john)