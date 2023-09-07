import time

def myTimer(original):
    def wrapper(*args, **kargs):
        start = time.time()
        result = original(*args, **kargs)
        end = time.time()
        print(f'this function spent {end-start} seconds.')
        if type(result) == str: 
            result += ' Hello.'
        if type(result) in [int, float]:
            result += 5
        return result
    return wrapper

@myTimer
def display(name, age):
    print(f"display()...... the {name} is {age} years old.")
    time.sleep(1)
    return name

if __name__ == '__main__':
    # age = myTimer(display)("wrapper call: Andrew", 13)     # wrapper function call, get same result
    # print(age)
    ori_age = display("original call: Andrew", 13)           # direct call
    print(ori_age)
