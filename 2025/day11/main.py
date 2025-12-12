f = open("input.txt")

# DFS Approach!

data = {}
for x in f:
    device, out = x.strip().split(": ")
    out = out.split(" ")
    if device in data:
        raise Exception
    data.update({device: out})

completed = []

start = data["svr"]
stack = []
for k in start:
    res = [False, "svr", k]
    stack.append(res)
def doesItContainUnCheckedChilds(path,id):
    for i in range(id+1, len(stack)-1):
        element = stack[i]
        if element[0] == False:
            return True
        return False


while True:
    sl = len(stack)-1
    curr = stack[sl] 
    while curr[0] == True:
        sl -=1
        new = stack[sl]
        if len(new) < len(curr):
            curr = stack[sl]
            if curr[0] == False:
                if not doesItContainUnCheckedChilds(curr,sl):
                    for i in range(sl,len(stack)-1):
                        stack.pop()
                    # Delete itself with all checked childs
        a=1
    
    # From 
    #newPaths = data[curr[len(curr)-1]]
    dataElment = curr[sl]
    newPaths = data[dataElment]

    if newPaths[0] == "out":
        if "fft" in curr and "dac" in curr:
            completed.append(newStack)
        stack[sl][0] = True
    else:
        for k in newPaths:
            newStack  = curr + [k]
            newStack[0] = True
            if newStack not in stack:
                newStack[0] = False
                stack.append(curr + [k])



while True:
    lastElms = stack[len(stack)-1]
    newElemens = []
    wasUpdate = False
    for i,paths in enumerate(lastElms):
        newData = data[paths[len(paths)-1]]
        for j,p in enumerate(newData):
            resultPath = paths + [p]
            if p == "out":
                if "fft" in resultPath and "dac" in resultPath:
                    completed.append(resultPath)
            else:
                if p in paths:
                    raise Exception
                wasUpdate = True
                newElemens.append(resultPath)
    if len(newElemens) > 3:
        if not isCounterOn: 
            isCounterOn = True
    stack.append(newElemens)
    if not wasUpdate:
        break

print(len(completed))
print("Hello")