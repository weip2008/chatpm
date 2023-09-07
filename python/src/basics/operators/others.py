"""
multiple times operator **, dict unpack
unpack operator *
"""
import numpy as np

a = np.array([[2,3],[5,6]], dtype=np.float64)
print(a.shape)
a += np.random.randn(*a.shape) * 0.1

print(a)
x = np.random.randn(2,3)
print(x)

date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info, **track_info,)
print(filename)

x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = {**x, **y}
print(z)

options = ["Monday","Tuesday",'Wednesday','Thursday','Friday','Saturday','Sunday']

t = (1,2,3,4)
print(*t)

def f1(a):
    print(a)

f1(t)

def f(a,b,c,d):
    print(a, b, c, d)

t = (5,6,7,8)
# f(t)
f(*t)

    