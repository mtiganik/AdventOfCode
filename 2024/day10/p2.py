grid = []

for x in open("input.txt"):
  k = x.strip()
  arr = []
  for m in k:
    if m.isdigit():
      m = int(m)
    arr.append(m)
  
  arr.insert(0,"*")
  arr.append("*")
  grid.append(arr)
grid.insert(0,["*"]*len(grid[0]))
grid.append(["*"]*len(grid[0]))

for k in grid:
  print(k)


def generateStartGrid():
  endGrid = []
  for k in range(len(grid)):
    endGrid.append([1000]*len((grid[0])))
  return endGrid


def checkCoord(y,x,currNum,cg):
  if grid[y][x] == currNum:
    cg[y][x] = currNum
    return [y,x]
    # if cg[y][x] == 1000:
  return None

def findPaths(y,x,cg):
  cg[y][x] = 0
  currplaces = []
  currplaces.append([y,x])
  currNum = 0
  while True:
    currNum += 1
    newPlaces = []
    for k in currplaces:
      newPlaces.append(checkCoord(k[0]-1 ,k[1]  ,currNum,cg))
      newPlaces.append(checkCoord(k[0]   ,k[1]+1,currNum,cg))
      newPlaces.append(checkCoord(k[0]+1 ,k[1]  ,currNum,cg))
      newPlaces.append(checkCoord(k[0]   ,k[1]-1,currNum,cg))
    
    currplaces = []
    for m in newPlaces:
      if m != None:
        currplaces.append(m)
    
    if len(currplaces) == 0:
      return 0
    if currNum == 9:
      return len(currplaces)



stGrid = generateStartGrid()
total = 0
for j in range(len(grid)):
  for i in range(len(grid[0])):
    if grid[j][i] == 0:
      cg = generateStartGrid()
      
      total += findPaths(j,i,cg)

print(total)