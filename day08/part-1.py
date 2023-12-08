
f = open("input.txt").read().replace("= (", "").replace(",","").replace(")","").splitlines()
instructions = f[0]
f = f[2::]
data = []
for x in f:
    el = x.split(" ")
    data.append(el)
idx = 0

currElement = currElement = [el for el in data if el[0] == "AAA" ][0]
newElement = ""
instrLen = len(instructions)
instructionNo = 0
while True:
    dir = instructions[instructionNo]
    instructionNo += 1
    if instructionNo >= instrLen:
        instructionNo = 0
    idx += 1
    if dir == "R":
        newElement = currElement[2]
    else:
        newElement = currElement[1]
    if newElement == 'ZZZ':
        break        
    currElement = next(x for x in data if x[0] == newElement)

# My time and rank:
# 02:18:56  16903
print(idx)
