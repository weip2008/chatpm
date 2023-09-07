"""
the minumun unit of computer memory is byte which has 8 bits. 
(each bit can be considered as an electric switch which can have only 2 values (1, 0))

all computer calculation, operation, text, image are based on bit operation.

Bitwise Operator: 
& : bit and
| : bit or
^ : bit xor
<<: left shift
>>: right shift
"""
def binFormat(num):
    s = str(bin(num))
    s1 = s[:2] + s[2:].zfill(8)
    return s1

# one byte have 8 bit, bit is single binary digit, switch on/off
a = 0b00111100 # 1 byte which has 8 bits.
print(binFormat(a))

# left shift
b = a<<1 # move all bits to the left on 1 position
print(binFormat(b))
print()

# right shift
b = a>>3
print(binFormat(a))
print(binFormat(b))

# left shift 1 is equivalent to multiply by 2
print(a)
print(a<<1) # a*2
print(a>>1) # a/2

b = 0b00001111
print(b)

# & operator return 1 onless both are 1, otherwise 0
c = a & b
print(binFormat(a))
print('&')
print(binFormat(b))
print(binFormat(c))
print(c)

# | operator
a = 0b00001100
b = 0b00101110
c = a | b
print(binFormat(a))
print('|')
print(binFormat(b))
print(binFormat(c))
print(c)

# ^ operator
a = 0b00001100
b = 0b00101110
c = a ^ b
print(binFormat(a))
print('^')
print(binFormat(b))
print(binFormat(c))
print(c)