def f(a, b, /, c, d='50', *, e=100, f=200):
    print(a, b, c, d, e, f)

def f1(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

    """
    a, b are positional arguments.
    e, f are keyword-only arguments.
    / is the separator of positional arguments from others.
    * is the separator of keyword arguments from others.
    c, d are possible both positional or keywords arguments.
    """
f(1,2,3,4) # ignore key-word arguments
f(1,2,3)
f(1,2,3,4,e='hello',f='world') # override default value
f(1,2,3,4, f='world',e='hello') # order dose not matter for k-word
f(1,2, f='world',e='hello',c=3,d=4) # c and d are k-word

f1(1,2,3,4,e=5,f=6)
f(1,2,3,4,e=5)
# f(1,2, f='world',e='hello',3,4) # order dose not matter for k-word
