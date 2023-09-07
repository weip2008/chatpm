"""
Comparison Operators
== Equal
!= NotEqual
>  Greater than
<  Less than
>= Greater than or equal to
<= Less than or equal to

comparison operator always return True or False bool type.
"""
a, b = 10, 20
f=a==b # comparison operator has higher priority than assignment operator
 
print(type(f))
print(f)

print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
print(a > b)
print(a < b)
print()

if a < b:
    print("a is less than b.")
else:
    print("a is greater than b.")
