from collections import defaultdict

antennas = []
xLen, yLen = 0,0
for x in open("input.txt"):
  k = list(x.strip())
  if yLen == 0: xLen = len(k)
  for i,a in enumerate(k):
    if a != ".":
      dictObject = {"name":a, "coords":[yLen, i]}
      antennas.append(dictObject)
  yLen += 1

antennas = sorted(antennas, key=lambda d: d['name'])
grouped = defaultdict(list)
for entry in antennas:
    grouped[entry['name']].append(entry['coords'])

groups = list(grouped.values())

antinodes = []

def getSign(y1,x1,y2,x2):
  y = 1 if y1 > y2 else -1
  x = 1 if x1 > x2 else -1
  return [y,x]

def getAntiNodes(group):
  for i in range(0,len(group)-1):
    for j in range(i, len(group)):
      y1,x1 = group[i]
      y2,x2 = group[j]
      ydist = abs(y2-y1)
      xdist = abs(x2-x1)

      ys,xs = getSign(y1,x1,y2,x2)
      m = 1
      while( 0<= y1 + ys*ydist*m <yLen and 0<= x1 + xs*xdist*m < xLen):
        newNode = [y1 + ys*ydist*m, x1 + xs*xdist]
        m += 1
        antinodes.append(newNode)
      ys,xs = -ys,-xs
      if 0<= y2 + ys*ydist <yLen and 0<= x2 + xs*xdist < xLen:
        newNode = [y2 + ys*ydist, x2 + xs*xdist]
        antinodes.append(newNode)


for group in groups:
  getAntiNodes(group)

for x in antinodes:
  print(x)
print(len(antinodes))