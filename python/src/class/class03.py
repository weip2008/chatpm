class Robot(object):
    def __init__(self, name): 
        self.name = name

    def __repr__(self): 
        return self.name

    def greeting(self):
        self.energy = 1000 # add attribute at any function
        print(f'Hello, my name is {self.name}!')

    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    john = Robot('john')
    print(john)
    john.greeting() # When calling a function, the first argument is not considered as a parameter.
    print(john.add(3,4))
    print(john.energy)
    john.year = 2020 # create attribute any time
    print(john.year)
    hao = Robot('Hao')
    print(hao.year)
