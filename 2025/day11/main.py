f = open("input.txt")


data = {}
for x in f:
    device, out = x.strip().split(": ")
    out = out.split(" ")
    if device in data:
        raise Exception
    data.update({device: out})

# for k in data:
#     print(k, " | ", data[k])
# pathList = [[data["you"],0]]
results = [[["you"]]]

completed = []
iterator = 0
while True:
    iterator += 1 
    lastElms = results[len(results)-1]
    newElemens = []
    wasUpdate = False
    for i,paths in enumerate(lastElms):
        newData = data[paths[len(paths)-1]]
        for j,p in enumerate(newData):
            resultPath = paths + [p]
            if p == "out":
                completed.append(resultPath)
            else:
                if p in paths:
                    raise Exception
                wasUpdate = True
                newElemens.append(resultPath)
    results.append(newElemens)
    if not wasUpdate:
        break

print(len(completed))