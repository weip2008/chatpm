filename = 'data/data1.csv'

runfile = open(filename,"r",encoding='utf-8')
for line in runfile:
    print(line.replaceAll(' ',''))
