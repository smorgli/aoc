import os

INPUT_FOLDER = 'inputs'

def getfile(filename):
    with open(str(os.path.join(INPUT_FOLDER,filename))) as f:
        lines = f.readlines()
    return(lines)
