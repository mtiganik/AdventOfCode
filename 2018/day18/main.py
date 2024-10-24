f = open("input.txt")

for line in f:
  cmnds = [int(cmd) for cmd in line.split(" ")]
  break
metaSum = 0

#start:
stackList = []
newNodes = cmnds.pop(0)
newMetaCnt = cmnds.pop(0)
stackList.append([newNodes, newMetaCnt])

while len(cmnds) > 0:
  mulBwrdsCheck = True
  while mulBwrdsCheck:
    lastElem = stackList[len(stackList) -1]
    if lastElem[0] == 0:
      metaSum += sum(cmnds[:lastElem[1]])
      # cmnds = cmnds[:-lastElem[1]]
      cmnds = cmnds[lastElem[1]:]
      stackList.pop()
    else:
      lastElem[0] = lastElem[0] -1
      mulBwrdsCheck = False

  newNodes = cmnds.pop(0)
  newMetaCnt = cmnds.pop(0)

  if newNodes == 0:
    metaSum += sum(cmnds[:newMetaCnt])
    cmnds = cmnds[newMetaCnt:]
  else:
    stackList.append([newNodes, newMetaCnt])
print(metaSum)
