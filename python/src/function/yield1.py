"""
'yield' is similar to 'return', instead of return one value,
'yield' returns a squence of values when it is needed.

 We should use yield when we want to iterate over a sequence, 
 but don’t want to store the entire sequence in memory.

 The yield statement suspends function’s execution and sends 
 a value back to the caller, but retains enough state to enable 
 function to resume where it is left off. When resumed, 
 the function continues execution immediately after the last 
 yield run. This allows its code to produce a series of values 
 over time, rather than computing them at once and sending 
 them back like a list.

 Above statement is little hard to understand, to make it easy,
 try to debug the yield python program.
"""
def simpleGeneratorFunc(): # take advantage of saving memory space
    yield 1
    yield 2
    yield 3

def f1():
    return [1,2,3,4,5]

if __name__ == '__main__':
    x = f1() # function is called, x is stored in memory
    for i in x:
        print(i)

    g = simpleGeneratorFunc() # declare g as generator instance
    print(g)
    for i in g:
        print(i)

