"""
Dictionaries are Python's implemementation of a data structure
that is more generally known as an associative array.

A dictionary consists of a collection of key-value pairs of python objects.
It is unordered, iterable, mutable, and each paire separted by commas, surrounded by {}.
and no duplicated key, the key-value pair are separated by colon.

d1 = {1:"one", 2:"two", 3:"three"} # key:value pair
"""

# create a dictionary
d = {}
print(type(d))
print(len(d))

days = {
    1:"Monday",
    2:"Tuesday",
    3:"Wendsday",
    4:"Thursday",
    5:"Friday",
}

print(type(days))
print(len(days))

t1 = ((1,2),(3,4),(5,6)) # tuple
d = dict(t1)
print(d)
print(type(d))

l1 = [(1,2),(3,4),(5,6)] # list
d = dict(l1)
print(d)


# dict is iterable
for i in days:  # get each element in the dictinary, iterate dictionary
    print(i, days[i])  # only iterate each key, where days[i] will get the value of the key

# dict is mutable, which means you can make change after you create it
days[6] = "Saturday"
days[7] = "Sunday"
print(days)
days[3] = "Three"
print(days)

del days[3]
print(days)

day = days[5]
print(type(day))
print(day)

d1 = days[5]
print(d1)

days[3] = 2-3j
print(type(days[3]))

print(days)

print(days.get(5))

# no duplicate key
days[3] = "this is a number 3"
print(days)

d1 = {'key1':'value1'}
d2 = {'key2':'value2'}
d1['key3'] = d2
print(d1)

d1 = {"school1":{(111,"student1"), (222, "student2"),(111,"student1")}}
print(d1)

# built in functions: items(), keys(), values(), pop(), clear()
for key, value in days.items():
    print(key, value)

items = days.items()
print(type(items))

a,b,c = (10, 20, 30)
print(a, b)

print(days.keys())

v = days.pop(3)
print(days)
print(v)

print(days.values())
days.clear()
print(days)

from math import pi

def circleArea(radius):
    return pi*radius**2

def triangleArea(base, height):
    return base*height/2

def notFound(*arg):
    return "No such key."

switch = {'circle':circleArea, 'triangle':triangleArea}

area = switch['circle'](2)
print(area)
area = switch['triangle'](2,4)
print(area)

area = switch.get('sphere',notFound)(2)
print(area)
area = switch.get('circle',notFound)(2)
print(area)
area = switch.get('triangle',notFound)(2,6)
print(area)
