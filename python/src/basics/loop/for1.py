import sqlite3
class Fullname:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

# def create_connection(db_file):
#     """ create a database connection to a SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)
#     return conn

for element in [1, 2, 3]: # list
    print(element)
for element in (1, 2, 3): # tuple
    print(element)
for key in {'one':1, 'two':2}: # dict
    print(key)
for s in {'A','B','C','D'}: # set
    print(s)
for char in "123": # str
    print(char)
for line in open("data/students.csv"): # csv file
    print(line, end='')

l1 = [x for x in range(50) if x%2==0] # conditional
print(l1)

# database = "pythonsqlite.db"
# conn = create_connection(database)
# c = conn.cursor()

# for row in c.execute('select * from tasks'): # sqlite database
#     print(row)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
l = [weapon.strip() for weapon in freshfruit] # function call
print(l)


l = [(x, x**2) for x in range(6)] # generate tuple list
print(l)

l = [Fullname(first,last) for first in ["John","David","Elle"] for last in ["Bidden","Smith","Martin"]] # generate class object list
print(l)

vec = [[1,2,3], [4,5,6], [7,8,9]]
l = [num for elem in vec for num in elem]
print(l)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
l = [[row[i] for row in matrix] for i in range(4)]
print(l)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

transposed = list(zip(*matrix))
print(transposed)

for i in range(11):
    if i == 0:
        sum1 = 0
    sum1 = sum1 + i

print(sum1) # for loop does NOT block the sum1 variable.

nameList = [
    ('james', 'mary'),
    ('john', 'patricia'),
    ('michael', 'jennifer'),
    ('david', 'linda'),
    ('sucan', 'elizabeth'),
    ('nancy', 'barbara'),
]

for child, mom in nameList:
    print(f"{child}'s mom is {mom}.")


l = [(1,2),(3,4),(5,6)]
l1 = [t[0]+t[1] for t in l]
print(l1)