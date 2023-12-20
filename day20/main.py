f = open("input.txt").read().splitlines()

def appendConjucture(conName):
    listElems = []
    for x in f:
        module, receivers = x.split(" -> ")
        receivers = receivers.split(", ")
        if conName in receivers:
            listElems.append([module, False])
    return [conName, listElems]
ffs = []
conjs = []
broadcaster = []
for x in f:
    module, receivers = x.split(" -> ")
    if module[0] == '%':
        ffs.append([module[1::], False])
    elif module[0] == "&":
        conjs.append(appendConjucture(module[1::]))
    elif module == "broadcaster":
        broadcaster.append(receivers.split(", "))


def sendSignal():
    cycleList = broadcaster[1]
    while cycleList(list) != 0:
        cycleList = []
        for idx,x in enumerate(cycleList):
            print("")
            
# sendSignal()
for x in conjs:
    print(x)