import copy

grid = []
for x in open("input.txt"):
  k = list(x.strip())
  k.insert(0,"*")
  k.append('*')
  grid.append(k)
xLen = len(grid[0])
yLen = len(grid)
grid.insert(0,['*']*xLen)
grid.append(['*']*xLen)
xLen += 2
yLen += 2

dg = []
dg = [[1000 for i in range(xLen) ] for j in range(yLen)]

# currArea = 1

def findCurrPlantPerimeter(plant, ys,xs):
  currArea = 1
  currPerimeter = 0

  ci = 0
  dg[ys][xs] = ci
  currElStack = [[ys,xs]]
  currAllCells = [[ys,xs]]
  intCorners = []
  extCorners = []
  corners = 0

  def isSamePlant(ys,xs):
    # global currArea
    if 0 <= ys < len(dg) and 0 <= xs < len(dg[0]):
      if grid[ys][xs] == plant:
        if dg[ys][xs] == 1000:
          # currArea += 1
          currElStack.append([ys,xs])
          currAllCells.append([ys,xs])
          dg[ys][xs] = ci
          return 1
    return 0

  def checkCorners(yc,xc, y1,x1,y2,x2):
    if grid[yc][xc] == plant: 
      if grid[y1][x1] != plant and grid[y2][x2] != plant:
        return 1
      return 0
    else:
      if grid[y1][x1] == plant and grid[y2][x2] == plant:
        intCorners.append([yc,xc])
        return 1
      elif grid[y1][x1] != plant and grid[y2][x2] != plant:
        extCorners.append([yc,xc])
        return 1
    return 0
  while True:
    ci += 1
    stackCpy = copy.deepcopy(currElStack)
    currElStack = []
    for k in stackCpy:
      y,x = k[0],k[1]
      currArea += isSamePlant(y-1,x  )
      currArea += isSamePlant(y  ,x+1)
      currArea += isSamePlant(y+1,x  )
      currArea += isSamePlant(y  ,x-1)
      corners += checkCorners(y-1,x+1,y-1,x,y,x+1) #up right
      corners += checkCorners(y+1,x+1,y,x+1,y+1,x) #down right
      corners += checkCorners(y+1,x-1,y,x-1,y+1,x) #down left
      corners += checkCorners(y-1,x-1,y-1,x,y,x-1) #up left
    if len(currElStack) == 0:
      for place in currAllCells:
        yi,xi = place[0], place[1]
        dg[yi][xi] = -1
      return corners*currArea


total = 0
fenceCosts = []
currPlant = grid[1][1]
total += findCurrPlantPerimeter(currPlant, 1,1)

for j in range(1,len(grid)-1):
  for i in range(1,len(grid[0])-1):
    if grid[j][i] != currPlant:
      currPlant = grid[j][i]
      if dg[j][i] == 1000:
        total += findCurrPlantPerimeter(currPlant,j,i)

print("p1: ", total)
    