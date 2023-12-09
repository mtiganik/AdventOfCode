f = open("input.txt").read().splitlines()
data = []
for x in f: 
  x = x.split()
  data.append([int(var) for var in x])

valsList = []
for x in data:
  enumerateList = []
  enumerateList.append(x)
  listToAppend = []
  while True:
    for i in range(len(x) -1):
      subtrack = x[i+1] - x[i]
      listToAppend.append(subtrack)
    x = listToAppend
    enumerateList.append(listToAppend)
    if all(v == 0 for v in listToAppend):
      wantedVal = 0
      for idx in range(len(enumerateList) -1, 0, -1):
        wantedVal +=  enumerateList[idx-1][-1]
      valsList.append(wantedVal)
      break
    listToAppend = []

print(sum(valsList))