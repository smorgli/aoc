import os

INPUT_FOLDER = 'inputs'

def getfile(filename,split = True):
    with open(str(os.path.join(INPUT_FOLDER,filename))) as f:
        if split:
            lines = f.read().splitlines()
        else:
            lines = f.readlines()
    return(lines)

#print(getfile('input2.txt'))
