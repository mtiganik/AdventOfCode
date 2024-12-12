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


def findCurrPlantPerimeter(plant, ys,xs, p1,p2):

  Area = 1
  perimeter = 0
  corners = 0
  ci = 0
  dg[ys][xs] = ci
  currElStack = [[ys,xs]]
  currAllCells = [[ys,xs]]

  def isSamePlant(ys,xs):
    nonlocal Area
    if 0 <= ys < len(dg) and 0 <= xs < len(dg[0]):
      if grid[ys][xs] == plant:
        if dg[ys][xs] == 1000:
          Area += 1
          currElStack.append([ys,xs])
          currAllCells.append([ys,xs])
          dg[ys][xs] = ci
        return 0
    return 1

  def checkCorners(yc,xc, y1,x1,y2,x2):
    if grid[yc][xc] == plant: 
      if grid[y1][x1] != plant and grid[y2][x2] != plant:
        return 1
      return 0
    else:
      return int((grid[y1][x1] == plant) == (grid[y2][x2] == plant))
    
  while True:
    ci += 1
    stackCpy = copy.deepcopy(currElStack)
    currElStack = []
    for k in stackCpy:
      y,x = k[0],k[1]
      for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
        perimeter += isSamePlant(y+dy,x+dx)
      for dy,dx,y1,x1,y2,x2 in [(-1,1,-1,0,0,1),(1,1,0,1,1,0),(1,-1,0,-1,1,0),(-1,-1,-1,0,0,-1)]:
        corners += checkCorners(y+dy,x+dx,y+y1,x+x1,y+y2,x+x2)
    if len(currElStack) == 0:
      for place in currAllCells:
        yi,xi = place[0], place[1]
        dg[yi][xi] = -1
      return [p1+perimeter*Area,p2+corners*Area]



p1,p2 = findCurrPlantPerimeter(currPlant := grid[1][1], 1,1,0,0)

for j in range(1,len(grid)-1):
  for i in range(1,len(grid[0])-1):
    if grid[j][i] != currPlant:
      currPlant = grid[j][i]
      if dg[j][i] == 1000:
        p1,p2 = findCurrPlantPerimeter(currPlant,j,i, p1, p2)

print("Part1:", p1)
print("Part2:", p2)
    