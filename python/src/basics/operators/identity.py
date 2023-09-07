"""
Identity operator: is, is not
Always return True or False.

"""

a = 5.5
b = 5.5
c = a

print(a is b) # same value of premitive data type (int, float, str)
print(a is c)

c = 10 # peel off the label c put that label in the new location which store 10
print(a)
print(a is c) # a is no long c, this is only happens on premitive data type such as int, float.

l1 = [1,2,3,4,5] # l1 is an instance of list, NOT premitive data type
l2 = [1,2,3,4,5] # same as l2
l3 = l1
print("21: ",l1 is l2) # even l1 and l2 hold same content, they are not the same
print("22: ",l1 is l3) # l1,l3 are different label on same memory location

l3.append('hello') # if you change the content of l3, 
print(l1 is l3)
print(l1) # content of l1 will be changed as well

a = str('John') # same as a = "John"
b = str('John') # a, b have same value, do not make them different object
c = a
print(a is b) # same value of premitive data type (int, float, str)
print(a is c)

from turtle import Turtle
