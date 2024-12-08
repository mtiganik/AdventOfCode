from collections import defaultdict

xLen = 0
antennas = []
yLen = 0
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

antinodes = []
def getAn1Sign(y1,x1,y2,x2):
  y = 1 if  y1 > y2 else -1
  x = 1 if  x1 > x2 else -1
  return [y,x]

def getAntiNodes(group):
  for i in range(len(group)-1):
    for j in range(i+1, len(group)):
      y1,x1 = group[i] 
      y2,x2 = group[j]

      ydist = abs(y1-y2)
      xdist = abs(x1-x2)

      y1s,x1s = getAn1Sign(y1,x1,y2,x2)

      m = 1
      while 0 <= x1 + xdist*x1s*m < xLen and 0 <= y1 + ydist*y1s*m < yLen:
        antinodes.append([y1 + ydist*y1s*m,x1+ xdist*x1s*m])
        m += 1
      m = 1
      y2s, x2s = -y1s, -x1s
      while 0 <=x2+ xdist*x2s*m < xLen and 0 <=y2 + y2s*ydist*m < yLen:
        antinodes.append([y2 + y2s*ydist*m,x2 + x2s*xdist*m])
        m += 1
  
for group in groups:
  getAntiNodes(group)

  for k in group:
    antinodes.append(k)

uniqueNodes = []
seen = set()
for node in antinodes:
  if tuple(node) not in seen:
    uniqueNodes.append(node)
    seen.add(tuple(node))

print(len(uniqueNodes))