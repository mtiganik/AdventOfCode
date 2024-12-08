
grid = []
antennas = []
jd = 1
for x in open("input.txt"):
  k = list(x.strip())
  k.insert(0,"*")
  for i,p in enumerate(k):
    if p not in [".","*"]:
      y,x = jd, i
      dictObject = {"name":p, "coords": [y,x]}
      antennas.append(dictObject)
  k.append("*")
  grid.append(k)
  jd += 1
grid.insert(0,["*"]*(len(grid[0])))
grid.append(["*"]*(len(grid[0])))
antennas = sorted(antennas, key=lambda d: d['name'])


def getP1Result(group):
  print(group)
  return 0


result = 0
antennas.append({"name":"end"})
group,i = [],1
gn = antennas[0]["name"]
group.append(antennas[0]["coords"])
while antennas[i]["name"] != "end":
  # ngn = antennas[i]["name"]
  if gn == antennas[i]["name"]:
    group.append(antennas[i]["coords"])
  else:
    result += getP1Result(group)
    gn = antennas[i]["name"]
    group = []
    group.append(antennas[i]["coords"])
  i += 1
result += getP1Result(group)