"""
A tuple is an ordered collection of python objects that is 
iterable, immutable, separated by commas, surrounded by ().

t1 = (1, 2, 3, 4)
"""
t1 = (1, 2, 3, 4, 'Hello', 'world', (5,6,7))

print(type(t1))
print(t1)

# tuple is iterable
for i in t1:
    print(i)

# slice a tuple
print(t1[5])
print(t1[4:6])  # tuple[start:stop:step], the stop element is excluded
print(t1[4:]) # all the way to the end
print(t1[::-1])

# the tuple is immutable
# t1[5] = "John" # TypeError: 'tuple' object does not support item assignment

# operator on tuple: +, *
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)

t4 = t3[0:3]+(1, 1, 1, 'Hello', 'world')+t3[4:]
print(t4)

print(t1*3)

student = ("John", 12, 'Male') # student is a tuple
print("%s is %s years old and %s." % student)

# there are few function for tuple: count(), index()
print(t4)
print(t4.count(1))
print(t4.index("world"))

# built in functions len(), sorted(), reversed()
print(len(t4))
print(tuple(reversed(t4)))

t4=(1,4,2,6,3)
print(sorted(t4))
t4=("John","Wang","Hello","World")
print(sorted(t4))

# use tuple() as function
s = "John"
i = tuple(s)
print(i)