import re
import helpers.funs

raw = helpers.funs.getfile('input2.txt')
lines = raw

for i in range(0,len(lines)):
    lines[i] = re.sub('X','A', lines[i])
    lines[i] = re.sub('Y','B', lines[i])
    lines[i] = re.sub('Z','C', lines[i])
    lines[i] = re.sub('A','1', lines[i])
    lines[i] = re.sub('B','2', lines[i])
    lines[i] = re.sub('C','3', lines[i])
    lines[i] = re.sub(' ','', lines[i])
    lines[i] = int(lines[i])

stupidextremelylowiqdict = {
    11:3+1,
    12:6+2,
    13:0+3,
    21:0+1,
    22:3+2,
    23:6+3,
    31:6+1,
    32:0+2,
    33:3+3
}

stupidextremelylowiqdict2 = {
    11:0+3,
    12:3+1,
    13:6+2,
    21:0+1,
    22:3+2,
    23:6+3,
    31:0+2,
    32:3+3,
    33:6+1
}

#print(stupidextremelylowiqdict[33])
suma = 0
for i in range(0,len(lines)):
    lines[i] = stupidextremelylowiqdict2[lines[i]]
    suma += lines[i]

print(suma)

#part 2

