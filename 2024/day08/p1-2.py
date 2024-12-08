from collections import defaultdict

grid = []
antennas = []
jd = 0
for x in open("input.txt"):
  k = list(x.strip())
  # k.insert(0,"*")
  for i,p in enumerate(k):
    if p not in [".","*"]:
      y,x = jd, i
      dictObject = {"name":p, "coords": [y,x]}
      antennas.append(dictObject)
  # k.append("*")
  grid.append(k)
  jd += 1
# grid.insert(0,["*"]*(len(grid[0])))
# grid.append(["*"]*(len(grid[0])))
antennas = sorted(antennas, key=lambda d: d['name'])

# for x in antennas:
#   print(x)


grouped = defaultdict(list)
for entry in antennas:
    grouped[entry['name']].append(entry['coords'])

groups = list(grouped.values())

antinodes = []
def getAntiNodes(group):
  for i in range(len(group)-1):
    for j in range(i+1, len(group)):
      y1, y2 = group[i][0], group[j][0]
      x1, x2 = group[i][1], group[j][1]
      ydist = abs(y1-y2)
      xdist = abs(x1-x2)
      if y1 == y2 or x1 == x2:
        Exception("shouldnt get here")
      an1y = (y2 - ydist) if y1 > y2 else (y1 - ydist)
      an2y = (y1 + ydist) if y1 > y2 else (y2 + ydist)
      an1x = (x2 - xdist) if x1 > x2 else (x1 - xdist)
      an2x = (x1 + xdist) if x1 > x2 else (x2 + xdist)
      if (x2 > x1 and y2 < y1) or (x1 > x2) and (y1 < y2):
        # if upwards diagonal then just swith y vals
        temp = an1y
        an1y = an2y
        an2y = temp

      if (an1x >= 0 and an1y >= 0) and (an1x < len(grid[0]) and an1y < len(grid)):
        antinodes.append([an1y,an1x])
      if (an2x < len(grid[0]) and an2y < len(grid)) and (an2x >= 0 and an2y >= 0) :
        antinodes.append([an2y,an2x])
  
for group in groups:
  getAntiNodes(group)

# for an in antinodes:
#   print(an)
# print(result)
uniqueNodes = []
seen = set()
for node in antinodes:
  if tuple(node) not in seen:
    uniqueNodes.append(node)
    seen.add(tuple(node))
# for node in uniqueNodes:
#   print(node)
print(len(uniqueNodes))