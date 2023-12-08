from math import gcd
f = open("AdventOfCode2023\day08\input.txt").read().replace("= (", "").replace(",","").replace(")","").splitlines()


instructions = f[0]
f = f[2::]
data = []
for x in f:
    el = x.split(" ")
    data.append(el)
nodes = [el for el in data if el[0].endswith("A")]

newElement = ""
instrLen = len(instructions)
ourNode = nodes[1]
reachedsums = []
for i,ourNode in enumerate(nodes):
    idx = 0
    while True:
        dir = instructions[idx%instrLen]
        idx += 1
        if dir == "R":
            newElement = ourNode[2]
        else:
            newElement = ourNode[1]
        if newElement.endswith("Z"):
            print("node ",i," reached goal in: ", idx)
            reachedsums.append(idx)
            break
                
        ourNode = next(x for x in data if x[0] == newElement)
lcm = 1
for i in reachedsums:
    lcm = lcm*i//gcd(lcm, i)

# My time and rank:
# 04:04:41  14418
print("Part 2:",lcm)
