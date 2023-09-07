"""
Ternary operator: if-else, and-or

if-else: a if a<b else b
1. first value
2. condition: if condition is True, return first value, 
3 another value, if condition is False, return another value.

and-or
1. condition
2. return first value if condition is True
3. return another value if condition is False
"""

a, b = 10, 20
min1 = a if a<b else b
print(min1)

max1 = a if a>b else b
print(max1)

# 1. condition, 2. first value when True, 3. another value if False
min1 = a<b and a or b
print(min1)

min1 = min(a, b)
print(min1)

max1 = max(a,b)
print(max1)

# use tuple and condition to choose value
max1 = (a, b)[a<b] # return b if True, otherwise return a
print(max1)

# use dict and condition to choose value
min1 = {True:a, False:b}[a<b]
print(min1)

t = (2, 3, 14, 6, 5,7)
max1 = max(t)
print(max1)
min1 = min(t)
print(min1)

"""
use ternary statement find minimum value of two numbers
"""

a, b = 10, 20
min0 = min(a, b)
print("07:", min0)

min1 = a if a < b else b
print("10:", min1)

print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a") 

if a != b: 
    if a > b: 
        print("a is greater than b") 
    else: 
        print("b is greater than a") 
else: 
    print("Both a and b are equal") 

min1 = a<b and a or b
print("23:",min1)

# use tuple and test make decision
min2 = (b, a)[a < b]
print("27:", min2)

# use dict and test make decision
min2 = {True: a, False: b}[a < b]
print("31:", min2)

# min5 = (lambda: a, lambda: b)[a > b]()
# print("21:", min5)

min3 = min(34, 56, 74, 23)
print("37:", min3)

t = (3, 7, 2, 67)
print("40:", min(t))

l = [8, 4, 76, 45]
print("43:", min(l))

