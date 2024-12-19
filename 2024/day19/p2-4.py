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

availableSoFar = []
def canMakeDesign(avail,k):
    LastOnes = Counter()
    AllAvailables = Counter()
    def checkStartSuit(d,p):
        if d.startswith(p):
            if d == p:
                LastOnes.update([p])
                return 1
            newDesign = d[len(p):]
            avail.update([newDesign])
        return 0
    while True:
        availableCpy = Counter(avail)
        AllAvailables.update(avail)
        # copy.deepcopy(avail)
        avail = Counter()
        res = 0
        for design in availableCpy:
            for p in patterns:
                res += checkStartSuit(design,p)
        if len(avail) == 0:
            #correct_sum = sum(value for key, value in AllAvailables.items() if key in AvailableEnd)
            total = sum(LastOnes.values())
            return total
        # if res != 0:
        #     return 0
        # avail = list(dict.fromkeys(avail))
    


cnt = 0
for k in designs:
    availableSoFar = Counter([k])
    cnt += canMakeDesign(availableSoFar,k)

print("p1: ", cnt)