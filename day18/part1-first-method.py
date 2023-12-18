f = open("input.txt").read().splitlines()
import numpy as np

grid = []
initialGrid = 3
for k in range(initialGrid):
    line = [0 for _ in range(initialGrid)]
    grid.append(line)
# grid[0][0] = 5
cmds = []
def addEmptyValsRight():
  for x in grid:
    x = x.append(0)
def addEmptyValsBottom():
   grid.append([0 for _ in range(len(grid[0]))])

def addEmptyValsLeft():
  for x in grid:
    x = x.insert(0,0)
def addEmptyValsUp():
  emptyLine = [0 for _ in range(len(grid[1]))]
  grid.insert(0,emptyLine)

def addValstoGrid(dir, steps, coord):
  i,j = coord
  moreNewRowsNeeded = False
  if dir == 'R':
    for k in range(steps):
      if j + k >= len(grid[0]):
        addEmptyValsRight() 
        moreNewRowsNeeded = True
      grid[i][k+j] += 1
    if moreNewRowsNeeded: addEmptyValsRight() 
    return (i, j+steps)
  elif dir == 'D':
    for k in range(steps):
      if i + k >= len(grid):
        addEmptyValsBottom()
        moreNewRowsNeeded = True
      grid[i+k][j] += 1
    if moreNewRowsNeeded: addEmptyValsBottom() 
    return (i+steps, j)
  elif dir == 'L':
    for k in range(steps):
      if j-k < 0:
        addEmptyValsLeft()
        j += 1
        moreNewRowsNeeded = True
      grid[i][j-k] += 1
    if moreNewRowsNeeded: 
      addEmptyValsLeft() 
      j += 1
    return (i,j-steps)

  elif dir == 'U':
    for k in range(steps):
      if i - k < 0:
        addEmptyValsUp()
        i += 1
        moreNewRowsNeeded = True
      grid[i-k][j] += 1
    if moreNewRowsNeeded: 
      addEmptyValsUp() 
      i += 1
    return (i-steps, j)

coord = (0,0)
for x in f:
  k = x.split()
  coord = addValstoGrid(k[0], int(k[1]), coord)
addEmptyValsBottom()
addEmptyValsLeft()
addEmptyValsRight()
addEmptyValsUp()

vertices = []
npGrid = np.array(grid)
def getNewVert(coord):
  i,j = coord[0]
  dir = coord[1]
  def getVals(idx,dir):
    if dir == "R":
      return [(i,j+idx+1),(i,j+idx), (i+1, j+idx), "D",(i-1,j+idx), "U"]
    elif dir == "D":
      return [(i+idx+1,j), (i+idx,j), (i+idx,j-1), "L", (i+idx,j+1), "R"]
    elif dir == "L":
      return [(i,j-idx-1), (i,j-idx), (i-1, j-idx),"U", (i+1,j-idx), "D"]
    elif dir == "U":
      return [(i-idx-1,j), (i-idx,j), (i-idx, j+1), "R", (i-idx,j-1), "L"]
  idx = 0
  while True:
    iterTuple, resTuple, clockWCheck, clockWVal, AClockWCheck,AClockVal = getVals(idx,dir)
    if npGrid[iterTuple] == 0:
      vertic = resTuple
      if npGrid[clockWCheck] == 1:
        newDir = clockWVal
      elif npGrid[AClockWCheck] == 1:
        newDir = AClockVal
      else: raise LookupError("Shouldnt get here")
      return [vertic, newDir]
    idx += 1
  # if dir == 

id = 1
jd = grid[1].index(1)
first = [(id, jd), 'R']
vertices.append(first)
newVert = getNewVert(first)
while newVert != first:
  vertices.append(newVert)
  newVert = getNewVert(newVert)
firstSum, secSum = 0,0
for k in range(-1,len(vertices)-1, 1):
  x1,y1 = vertices[k][0]
  x2,y2 = vertices[k+1][0]
  firstSum += x1*y2
  secSum += y1*x2
gridCnt = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == 1:
      gridCnt += 1
area = abs(firstSum-secSum)/2
for i,x in enumerate(grid):
  line = "".join(map(str, x))
  line= line.replace("1", "#")
  line = line.replace("0", ".")
  # if i == half:
  #   print()
  print(line)
for x in vertices:
  print(x)
print("Part1:", area+gridCnt/2 +1)

# for i,x in enumerate(grid):
#   for j,y in enumerate(x):
#     if grid[i][j] == 1:
#       if grid[i-1][j] == 1 and grid[i+1][j] == 1:
#         continue
#       elif grid[i][j-1] == 1 and grid[i][j+1] == 1:
#         continue
#       else:
#         vertices.append([i,j])
# half = (len(grid)) / 2

