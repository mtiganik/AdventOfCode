from collections import defaultdict

xLen, yLen, antennas = 0, [],0

for x in open("input.txt"):
  k = list(x.strip())
  if yLen == 0: xLen = len(k)
  for i,p in enumerate(k):
    if p not in [".","*"]:
      y,x = yLen, i
      dictObject = {"name":p, "coords": [y,x]}
      antennas.append(dictObject)
  yLen += 1
antennas = sorted(antennas, key=lambda d: d['name'])

grouped = defaultdict(list)
for entry in antennas:
    grouped[entry['name']].append(entry['coords'])

groups = list(grouped.values())

p1Nodes, p2Nodes = [],[]

def getUnique(currNodes):
  uniques = []
  seen = set()
  for node in currNodes:
    if tuple(node) not in seen:
      uniques.append(node)
      seen.add(tuple(node))
  return uniques

def getAn1Sign(y1,x1,y2,x2):
  y = 1 if  y1 > y2 else -1
  x = 1 if  x1 > x2 else -1
  return [y,x]

def getAntiNodes(group):
  for i in range(len(group)-1):
    for j in range(i+1, len(group)):
      y1,x1 = group[i] 
      y2,x2 = group[j]
      ydist,xdist = abs(y1-y2), abs(x1-x2)
      ys,xs = getAn1Sign(y1,x1,y2,x2)
      for z in range(2):
        m = 1
        if z == 0: y,x = y1,x1
        else: 
          y,x = y2,x2
          ys, xs = -ys, -xs
        while 0 <= x + xdist*xs*m < xLen and 0 <= y + ydist*ys*m < yLen:
          node = [y + ydist*ys*m,x+ xdist*xs*m]
          if m == 1:
            p1Nodes.append(node)
          p2Nodes.append(node)
          m += 1
  
for group in groups:
  getAntiNodes(group)
  for k in group:
    p2Nodes.append(k)


p1Unique = getUnique(p1Nodes)
p2Unique = getUnique(p2Nodes)


print("Part 1: ", len(p1Unique))
print("Part 2: ", len(p2Unique))

#https://youtu.be/8VmPtq06kNg