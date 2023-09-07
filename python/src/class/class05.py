"""
__new__(cls): construct the object
__init__(self): initializing the object 
"""

class A:
    def __new__(cls):  # constructor
        print("A.__new__() is called.")

class B:
    def __init__(self): # initializer
        print("B.__init__() is called.")

class C:
    def __init__(self):
        print("C.__init__() is called.")

    def __new__(cls): # override the __new__() function
        print("C.__new__() is called.")
        return super(C, cls).__new__(cls)

class D(object):
    def __new__(cls):
        print("D.__new__() is called.")
        return B()

class E:
    def __init__(self):
        print('E.__init__() is called')
        return 33

if __name__ == '__main__':
    x = A()
    y = B()
    z = C()
    print(z)
    x = D()
    print(x)
    print(type(x))
    # x = E()

