"""
A list is an ordered collection of python objects that is 
iterable, mutable, separated by commas, surrounded by [].

j1 = [1, 2, 3, 4]
"""

j1 = [1, 2, 3, 4]
print(type(j1))

# list is iterable
for i in j1:
    print(i)

# list slicing: list[start:stop:step]
print(j1[:2]) # index 2 is excluded
print(j1[2])

# list is mutable which means I can make change on individual item
j1[2]=10
print(j1)

t1 = (5,6,4,8,0)
print(t1)
j1 = list(t1)
j1[3] = 10
t1 = tuple(j1)
print(t1)

# functions for list: append(),count(),insert(),pop() (>>> help(list))
print(j1)
item = j1.pop(2)
print(j1)
print(item)
j1.insert(2,"hello")
print(j1)
j1.append("world")
print(j1)
print(j1.count("hello"))

# built in functions: len(), sorted(), reversed() {>>> dir(__builtins__)}
j1 = [4,5,2,65,78,12]
print(len(j1))
print(sorted(j1))
print(list(reversed(j1)))