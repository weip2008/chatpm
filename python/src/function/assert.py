"""
❗️⚡️User may pass wrong argument to function.
assert check before calculation.

assert: I swear this must be true, in case it happens, let me know. 
❌❗️Once it happens, you have big problem! 
👌✔️Debug aid for developer find root cause, 
❌not for handling run-time error. 
😢only give you one kind of error which is AssertionError.
"""
from math import pi

def circle_area(r):
    assert type(r) in [int, float], f"radius should be int or float, but radius={r}"
    return r * r * pi

if __name__ == '__main__': 
    try:
        x = circle_area(2-3j) # 😢without check the calling argument, give you meaningless output
        print(x)
    except Exception as err:
        print(err)
    print("Done.")