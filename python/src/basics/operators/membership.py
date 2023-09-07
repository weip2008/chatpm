"""
Membership operator: in, not in

Return True if the container contains the element, return False otherwise.

here is some container: str, tuple, list, set, dict
"""

s = "Hello, world!" # string container
print('s' in s)

t = (1,2,3,4,5)
print(6 not in t)

l1 = [1,2,3,4,5]
print(3 in l1)

set1 = {1,2,3,4,5,"hello"}
print('hello' in set1)

t1 = ((1,2),(3,4),(5,6))
d = dict(t1)
print(2 in d) # in operator only care about key NOT value