"""
Logical Operator: always return True or False.

and: return True only both sides are True, return False otherwise  
or : return False only both sides are False, return True otherwise
not: return reverse of comparison result
"""

a, b = 10, 20
c = a==20 and b==20 # comparison operator has higher priority than logical, assignmen has lowest priority
print(c)

c = a==10 or b==10
print(c)

c = not a==10
print(c)

min1 = a<b and a or b
print(min1)
max1 = a>b and a or b
print("max number between a and b is",max1)

a =10
c = a and b # c = a==0 and a or b; return b if a!=0, otherwise return 0
print(c)

c = a or b # c = a==0 and b or a; return a if a!=0, return b otherwise
print(c)

# Lazy or non-strict evaluation
x = True and "right"
print("Line-33:",x)
x = False and "left"
print(x)
a,b = 5,10
x = a<b and "right"
print(x)
x = a>b and "right"
print(x)

