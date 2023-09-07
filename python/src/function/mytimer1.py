import time

def myTimer(original):
    def wrapper(*args, **kargs):
        original(*args, **kargs)
    return wrapper

def display(name, age):
    start = time.time()
    print(f"display()...... the {name} is {age} years old.")
    time.sleep(1)
    end = time.time()
    print(f'this function spent {end-start} seconds.')

if __name__ == '__main__':
    myFunc = myTimer(display) 
    myFunc("Andrew", 13)     # wrapper function call, get same result
    display("Andrew", 13)    # direct call
