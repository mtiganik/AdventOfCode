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
# print(getResult("HASH",0))

boxes = []
for i in range(256):
    boxes.append([i])
for x in f:
    if "=" in x:
        lenNo = int(x.split("=")[1])
        path = x.split("=")[0]
        remove = False
    else:
        lenNo = 0
        path = x.split("-")[0]
        remove = True
    boxNo = getResult(path)
    currBox = boxes[boxNo]
    for i in currBox:
        if i[0] == path:
            
    print(boxNo, " : " , path)

