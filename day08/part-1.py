
f = open("input.txt").read().replace("= (", "").replace(",","").replace(")","").splitlines()

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
    if(idx%1000000 == 0):
        print(idx)
    if dir == "R":
        newElement = currElement[2]
    else:
        newElement = currElement[1]
    if newElement == "ZZZ":
        break        
    currElement = next(x for x in data if x[0] == newElement)

print(idx)
