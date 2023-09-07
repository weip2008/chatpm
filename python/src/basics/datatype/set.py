"""
A set is NOT ordered collection of python objects that is 
iterable, mutable, separated by commas, surrounded by {}.

j1 = {1, 3, 5, 7, 9} all odd number less than 10
"""

j1 = {1, 3, 5, 7, 9}
print(type(j1))
print(j1)

# set is iterable which means you can iterate each item one after another
# n = 10
# for i in n: # TypeError: 'int' object is not iterable
#     print(i)

j = iter(j1) # j is iterator which is iterable
print(type(j))
print("next element:",next(j)) # if j is an iterator, you can use next() function to get next available item.
print("next element:",next(j))
print("next element:",next(j))
print("next element:",next(j))
print("next element:",next(j)) 
# print("next element:",next(j)) # you can not iterate iterator when it reaches the end of the iterator
# print("next element:",next(j))

# iterate: the processing to get each next avaible element
# iterator: is an python object which has bunch of element available for you to get.

for i in j1: # where the i each individual element (this is also an iterate operation)
    i = i*2+123
    print(i) # one can use for-loop to iterate each element of an iterable object.

# set cannot be sliced
# a = j1[3]
# print(a)

# set cannot have duplicated elements
s1 = {1,1,1,2,2,2,3,3,5,6,7}
print(s1)

# set is mutable
s1.add(10)
print(s1)
s1.add(10)
print(s1)
s1.add(10)
print(s1)
s1.add(10)
print(s1)
