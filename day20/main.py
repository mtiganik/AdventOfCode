f = open("input.txt").read().splitlines()

def appendConjucture(conName):
    listElems = []
    for x in f:
        module, receivers = x.split(" -> ")
        receivers = receivers.split(", ")
        if conName in receivers:
            listElems.append([module, False])
    return ["&"+conName, listElems]
modules = []
broadcaster =[]
input = []
for x in f:
    module, receivers = x.split(" -> ")
    input.append([module, receivers.split(", ")])
    if module[0] == '%':
        modules.append([module, False])
    elif module[0] == "&":
        modules.append(appendConjucture(module[1::]))
    elif module == "broadcaster":
        broadcaster = [["broadCast" , False] + [[val for val in receivers.split(", ")]]]

def findModule(moduleName):
    for idx,x in enumerate(modules):
        if x[0][1::] == moduleName:
            return [x, idx]
    return [-1,-1]

def sendffSignal(input,idx):
    if input == True:
        return -1
    else: 
        modules[idx][1] = not modules[idx][1]
        return modules[idx][1]
    
def sendconjSignal(senderName, signalVal, idx):
    conjInputs = modules[idx][1]
    for i,x in enumerate(conjInputs):
        if x[0] == senderName:
            modules[idx][1][i][1] = signalVal
    # conjInputs = modules[idx][1]
    for x in modules[idx][1]:
        if x[1] == False: return True
    return False


def sendSignal():
    posSum,negSum = 0,0
    for i in range(1000):
        signals = broadcaster
        posCnt,negCnt = 0,1
        # print("button -low-> broadcaster")
        while len(signals) > 0:
            iterSignals = signals
            signals = []
            for x in iterSignals:
                conjSender, signalVal, currModules =x[0],x[1],x[2]
                for senderName in currModules:
                    if signalVal == False: checker, negCnt = "-low->", negCnt+1
                    else: checker, posCnt = "-high->", posCnt+1
                    # print(conjSender,checker,senderName)
                    [module,idx] = findModule(senderName)
                    if module == -1: continue
                    if module[0].startswith("%"):
                        senderName = "%" + senderName
                        output = sendffSignal(signalVal,idx)
                    else: 
                        senderName = "&" + senderName
                        output = sendconjSignal(conjSender,signalVal,idx)
                    if output != -1:
                        vals = [el for el in input if el[0]==module[0]][0][1]
                        signals.append([senderName, output, vals])
                    # if output == True: posCnt += 1
                    # else: negCnt += 1
        # print("pos cnt:", posCnt, ", neg cnt:",negCnt)
        # print("----------")
        posSum,negSum = posCnt+posSum, negCnt+negSum
    return posSum*negSum


print(sendSignal())
# for x in input:
# def sendSignal():
#     for i in range(10):
#         cycleList = broadcaster[2]
#         senderName = broadcaster[0]
#         signalToSend = broadcaster[1]
#         posSignalCnt, negSignalCnt = 0,0
#         senders = broadcaster
#         while len(senders) != 0:
#             senders = []
#             newCycleList = []
#             for y in senders:
#                 for x in cycleList:
#                     module, idx = findModule(x)
#                     if module[0].startswith("%"):
#                         output = sendffSignal(module,signalToSend,idx)
#                     else: 
#                         output = sendconjSignal(module,x,idx)
#                     if output != -1:
#                         modelsToNewSignal = [el for el in input if el[0]==module[0]]
#                         if len(modelsToNewSignal) != 1: raise ValueError("shouldnt be other than 1")
#                         vals = modelsToNewSignal[0][1]
#                         newCycleList = [x,output, [[el, output] for el in vals]]
#                     if output == True: posSignalCnt += 1
#                     else: negSignalCnt += 1
#             senders.append(newCycleList)
#         print("pos:", posSignalCnt, " neg:", negSignalCnt)


# def sendconjSignal2(senderName, signalVal,idx):
#     inputs = input[idx][1]
#     # currIputName = conjecture[0]
#     for i,x in enumerate(inputs):
#         if inputs[i][0]== senderName:
#             input[idx][1][i][1] = signalVal
#             inputs[i] = signalVal
#     for i,x in enumerate(inputs):
#         if x[1] == False:
#             return True
#     return False
    # print(x)

