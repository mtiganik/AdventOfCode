
lines = open("input.txt").read().split("\n")

keys = []
locks= []

while len(lines) > 0:
    els = []
    res = [-1,-1,-1,-1,-1]
    char = ""
    for _ in range(7): els.append(lines.pop(0))
    if len(lines) > 0:lines.pop(0)
    islock = True if "#" in els[0] else False
    els.pop(0)
    char = "." if islock else "#"
    for j,row in enumerate(els):
        for i in range(5):
            if row[i] == char and res[i] == -1:
                res[i] = j
    if islock: locks.append(res)
    else: 
        for i in range(5):
            res[i] = 5 - res[i]
        keys.append(res)

def canFit(key,lock):
    for t in range(5):
        if key[t] + lock[t] > 5: return 0
    return 1


total = 0
for lock in locks:
    for key in keys:
        total += canFit(key,lock)
print(total)

