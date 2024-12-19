import copy

patterns = []
designs = []
with open("input.txt") as file: lines = file.readlines()


patterns = lines[0].strip().split(", ")
lines.pop(0)
lines.pop(0)
for k in lines:
    designs.append(k.strip())

availableSoFar = []
def canMakeDesign(avail):

    def checkStartSuit(d,p):
        if d.startswith(p):
            if d == p:
                return 1
            newDesign = d[len(p):]
            avail.append(newDesign)
        return 0
    while True:
        availableCpy = copy.deepcopy(avail)
        avail = []
        res = 0
        for design in availableCpy:
            for p in patterns:
                res += checkStartSuit(design,p)
        if res != 0:
            return 1
        if len(avail) == 0:
            return 0
        # Remove duplicates:
        avail = list(dict.fromkeys(avail))
    


cnt = 0
for k in designs:
    availableSoFar = [k]
    cnt += canMakeDesign(availableSoFar)

print("p1: ", cnt)