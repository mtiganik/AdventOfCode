import copy

grid = [["*"] + list(x.strip()) + ["*"] for x in open("input.txt")]
grid.insert(0,['*']*len(grid[0]))
grid.append(['*']*len(grid[0]))
dg = [[1000 for i in range(len(grid[0])) ] for j in range(len(grid))]


def findCurrPlantPerimeter(plant, ys,xs, p1,p2):
  Area, perimeter,corners,ci,dg[ys][xs], currElStack,currAllCells = 1,0,0,0,0,[[ys,xs]],[[ys,xs]]
  
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
    return int(grid[yc][xc] == plant and grid[y1][x1] != plant and grid[y2][x2] != plant) or int((grid[yc][xc] != plant) and (grid[y1][x1] == plant) == (grid[y2][x2] == plant))

  while True:
    stackCpy = copy.deepcopy(currElStack)
    currElStack,ci = [], ci+1
    for [y,x] in stackCpy:
      for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]: perimeter += isSamePlant(y+dy,x+dx)
      for dy,dx,y1,x1,y2,x2 in [(-1,1,-1,0,0,1),(1,1,0,1,1,0),(1,-1,0,-1,1,0),(-1,-1,-1,0,0,-1)]:corners += checkCorners(y+dy,x+dx,y+y1,x+x1,y+y2,x+x2)
    if len(currElStack) == 0:
      for p in currAllCells: dg[p[0]][p[1]] = -1
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
    