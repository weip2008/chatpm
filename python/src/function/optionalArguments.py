def f(*psargs, **kwargs):
    print(len(psargs), len(kwargs))
    print('\nPositional...')
    for i in psargs:
        print(i,end=', ')
    print("\nKeywords...")
    print(type(psargs), type(kwargs))
    for k,v in kwargs.items():
        print(f'{k}={v}', end=', ')


f(1,2,3,4,a=4,b=6,c=9,d='hello')
