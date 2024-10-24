f = open("input.txt").read().split(",")

def getResult(path):
    remainder = 0
    for x in path:
        currVal = ord(x)
        currVal += remainder
        currVal *= 17
        remainder = currVal % 256
    return remainder

cnt = 0
for x in f:
    result = getResult(x,0)
    cnt += result

print("Part1: ", cnt)