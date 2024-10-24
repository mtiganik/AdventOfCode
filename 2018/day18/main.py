f = open("input.txt")

for line in f:
  cmnds = [int(cmd) for cmd in line.split(" ")]
  break
metaSum = 0
i = 0
dataStruck = []
isNewNode = True

#Base
newNodes = cmnds[i]
newMetaCnt = cmnds[i+1]
dataStruck = [[] for x in range(newNodes)]
newMeta = cmnds[-newMetaCnt:]
cmnds = cmnds[:-newMetaCnt]
metaSum += sum(newMeta)
dataStruck.append(newMeta)  

i = i+2
#First child:
newNodes = cmnds[i]
newMetaCnt = cmnds[i+1]
i = i+2
if newNodes > 0:
  newDataStruck = [[] for x in range(newNodes)]
  newDataStruck.append(-newMetaCnt)
  dataStruck[0] = newDataStruck
else:
  newMeta = cmnds[i:i+newMetaCnt]
  metaSum += sum(newMeta)
  dataStruck[0] = newMeta
  i = i + newMetaCnt

print(dataStruck)
print(metaSum)
# print(cmnds)