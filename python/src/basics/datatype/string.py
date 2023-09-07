"""
str: python use '...', "...", '''...''', \"""...\""" for define string variable
"""

name="Ethan"
print(type(name)) # type() built-in function tell you what is the data type of the variable

name='Ethan'
print(type(name))
name='''Ethan'''
print(type(name))
name="""Ethan"""
print(type(name))

print(f"Hello, {name}!")
s = '''Ethan said: "I'm Ethan."'''
print(s)

# string is iterable
for i in s:  # so we can get each letter through the for loop
    print(i, end='; ')

print() # create a new line

# string slicing
s1 = s[6:10] # get part of the string
print(s1) #said

# s[start:stop:step], start=0, stop is all the way to the end, step 1
s1 = s[6:]  # return a string from index 6 to the end
print(s1)

s1 = s[::2] # return string from begining to the end step by 2
print(s1)

s1 = s[13] # return letter on index 13
print(s1)

s1 = s[::-1] # this will reverse the whole string
print(s1)

number = '14567'
s1 = number[::-1]
print(s1)

# what is the tenth digit for number?
print(f'the tenth digit of {number} is {number[-2]}.')

day = '2022-06-23' # '06/23/2022'
year = day[:4]
after4 = int(year)+4
print(year)
print(after4)

# string is immutable (once you define a string, there is no way to make change)

# day[0] = 3 #TypeError: 'str' object does not support item assignment


## string operator *, +, .
s1 = '123'
s2 = 4*s1
print(s2)
print("hello " + s1)
# s3 = s2 - s1   TypeError: unsupported operand type(s) for -: 'str' and 'str'

# string function
i = 1234
print(type(i))
s = str(i)
print(type(s))
s3 = "   hello world       "
print(s3.upper())
print(s3.strip())
print(s3.split())
print(s3.startswith(' '))


