import function.func01 as func

x = func.f(1,2,3)
print(x)

# Change default keyword arguments for print
print(10, 13, 98, 123, end=":::")
print(10, 13, 98, 123) # multiple objects print out
x= abs(-12)
print(x)


# calculate rectangle area
width=14
length=5
area = width *  length

# print with placeholder (%d:integer, %s: string, %f: float, )
print("The rectangle area with width=%d and length=%d is %d." %(width, length, area))

# formated print out
print(f"The rectangle area with width={width} and length={length} is {area}.")
print(f"6 \u00F7 5 = {6/5}")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
name,age = 'John', 14
# %d is a second placeholder which holds an integer
# %s is a first placeholder which holds a string
format = "%s is %d years old."
print("%s is %d years old." %(name,age))
print(format %(name,age))
print("after 5 years you will be %d years old." %(age+5))

# homework sample code
x=2020
y=20
z=2020-20
print("Problem 01: %d - %d = %d" %(x, y, z))
print("Problem 02: %d + %d = %d" %(494, 18, 494+18))
print("Problem 03: I don't know how to do it.")

A=65
print(A)
print(bin(A))
print(hex(A))
print(type(A))
print(chr(A))
letter = 'A'
print(ord(letter))

file1 = open("test.csv",'+w')
print(1,2,3,4,file=file1)
file1.close()
file2 = open("test.csv")
print(file2.read())