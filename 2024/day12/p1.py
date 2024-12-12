import copy

grid = []
for x in open("input.txt"):
  k = list(x.strip())
  grid.append(k)
xLen = len(grid[0])
yLen = len(grid)
# grid.insert(0,['*']*xLen)
# grid.append(['*']*xLen)
# xLen += 2
# yLen += 2

dg = []
dg = [[1000 for i in range(xLen) ] for j in range(yLen)]
# def getdGrid():
#   return [[1000 for i in range(xLen) ] for j in range(yLen)]
currArea = 1

def findCurrPlantPerimeter(plant, ys,xs):
  global currArea
  currArea = 1
  currPerimeter = 0
  # dg = getdGrid()
  ci = 0
  dg[ys][xs] = ci
  currElStack = [[ys,xs]]
  currAllCells = [[ys,xs]]

  def isSamePlant(y,x):
    global currArea
    if 0 <= y < len(dg) and 0 <= x < len(dg[0]):
      if grid[y][x] == plant:
        if dg[y][x] == 1000:
          currArea += 1
          currElStack.append([y,x])
          currAllCells.append([y,x])
          dg[y][x] = ci
        return 0
      else: return 1
    else: return 1

  while True:
    ci += 1
    stackCpy = copy.deepcopy(currElStack)
    currElStack = []
    for k in stackCpy:
      yc,xc = k[0],k[1]
      currPerimeter += isSamePlant(yc-1,xc  )
      currPerimeter += isSamePlant(yc  ,xc+1)
      currPerimeter += isSamePlant(yc+1,xc  )
      currPerimeter += isSamePlant(yc  ,xc-1)
    if len(currElStack) == 0:
      for place in currAllCells:
        yi,xi = place[0], place[1]
        dg[yi][xi] = -1
      return currPerimeter*currArea


total = 0
fenceCosts = []
currPlant = grid[0][0]
total += findCurrPlantPerimeter(currPlant, 0,0)

for j in range(len(grid)):
  for i in range(len(grid[0])):
    if grid[j][i] != currPlant:
      currPlant = grid[j][i]
      if dg[j][i] == 1000:
        total += findCurrPlantPerimeter(currPlant,j,i)

print("p1: ", total)
    