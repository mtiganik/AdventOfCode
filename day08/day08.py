
f = open("AdventOfCode2023\day08\input2.txt").read().replace("= (", "").replace(",","").replace(")","").splitlines()

instructions = f[0]
f = f[2::]
data = []
for x in f:
    el = x.split(" ")
    data.append(el)
idx = 0
currElement = data[0]
newElement = ""
instrLen = len(instructions)
while True:
    dir = instructions[idx%instrLen]
    idx += 1

    if dir == "R":
        newElement = currElement[2]
    else:
        newElement = currElement[1]
    if newElement == "ZZZ":
        break        
    currElement = next()[0]

print(idx)
