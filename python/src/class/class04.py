class Robot(object):
    def __init__(self, name): 
        self.name = name

    def __repr__(self): 
        return self.name

    def greeting(self):
        print(f'Hello, my name is {self.name}!')

    def add(self, a, b):
        return a + b

    def __len__(self):
        return len(self.name)

if __name__ == '__main__':
    john = Robot('john')
    print(john)
    john.greeting() # When calling a function, the first argument is not considered as a parameter.
    print(john.add(3,4))
    print(len(john))
    for i in range(1, 11):
        print(i)