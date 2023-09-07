"""
Assignment Operators =; +=; -=; *=; /=; %=; **=; //=;

Each arithmetic operator has corresponding assignment operator.
"""

from numpy import *


a,b=10,20

print(a)
a += b  # equivalent to: a = a + b
print(a)
a //= b # equivalent to: a = a//b
print(a)

b **=a # b = b**a
print(b)

a = [[1,0],[1,1]]
b = [1,2]
print(matmul(a,b))

