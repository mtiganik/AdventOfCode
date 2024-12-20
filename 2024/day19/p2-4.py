import copy
from collections import Counter

patterns = []
designs = []
with open("input.txt") as file: lines = file.readlines()


patterns = lines[0].strip().split(", ")
lines.pop(0)
lines.pop(0)
for k in lines:
    designs.append(k.strip())



def canMakeDesign(design):
    def start(p):
        if design.startswith(p):
            currElems.update([p])

    def canInclude(p,d,el):
        if d.startswith(p):
            currElems.update([el+p])
            return 1
        return 0
    currElems = Counter([])
    
    for p in patterns:
        start(p)

    while True:
        copyElems = currElems
        currElems = Counter()
        x = 5
        for el in copyElems:
            res = 0
            for k in patterns:
                res += canInclude(k,design[len(el):],el)
            if res == 0:
                currElems.remove(el)
        # if len()

cnt = 0
for k in designs:
    # availableSoFar = Counter([k])
    cnt += canMakeDesign(k)

print("p1: ", cnt)