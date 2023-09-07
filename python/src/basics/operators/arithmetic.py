"""
 Arithmatic operator: +; -; *; /; %; **; //(floor divisor)
"""

a, b = 10, 20
c1 = a + b  # addition
c2 = a - b  # subtraction
c3 = a * b  # multiplication
c4 = a / b  # division
c5 = a % b  # modulus
c6 = a ** b # exponential
c7 = b // a # floor divisor

print(c1)
print(c5)
print(c6)
print(c7)

# Floor Divisor
print("11:", 9 // 2)  # 4
print("12:", 11 // 3)  # 3
print("13:", -11 // 3)  # -4, notice what mean by floor

# why we need //?
a = 20
b = 3
c = a//b # make c as an integer
print(type(c))
print(c)
for i in range(c):
    print(i)
