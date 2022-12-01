import os
import re

#input  = os.open('C:\\Users\\vhdl\\Desktop\\pp_adv\\input_1.txt',os.O_RDONLY)

with open('input_1.txt') as f:
    lines = f.readlines()

lines_added = []
added = 0
for i in range(0,len(lines)):
    lines[i] = re.sub('\\n','', lines[i])
    if lines[i] == '':
        lines_added.append(added)
        added = 0
    else:
        lines[i] = int(lines[i])
        added = added + lines[i]

max(lines_added) # wynik 1

## 2
lines_added.sort()
wynik2 = 65240 + 68996 + 70374






