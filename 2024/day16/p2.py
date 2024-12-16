import copy
import sys
grid = []
x,y = 0,0
xe,ye = 0,0
idx = 0
for k in open("input.txt"):
  k = k.strip()
  if "E" in k:
    ye = idx
    xe = k.index("E")
  if "S" in k:
    y = idx
    x = k.index("S")
  idx += 1
  grid.append(list(k))


dg = [["x" for i in range(len(grid[0]))] for j in range(len(grid))]

def getFewestMovesList():
  res = []
  minElms = sys.maxsize
  for el in currCheckEls:
    if el[3]< minElms:
      minElms = el[3]
  for el in currCheckEls:
    if el[3] == minElms:
      res.append([el[0],el[1],el[2],el[3]])
  return res


def checkAvailability(y,x,dir, cnt):
  if grid[y][x]== ".":
    if dg[y][x] =="x":

      dg[y][x] = cnt
      currCheckEls.append([y,x,dir,cnt])
  if grid[y][x] == "E":
    return cnt
  return 0


dg[y][x] = 0
currCheckEls = [[y,x,1,0]]
currCnt = 1
while True:
  elToCheck = getFewestMovesList()
  checker = 0
  for k in elToCheck:
    ny,nx,dir, cnt = k[0],k[1],k[2], k[3]
    checker += checkAvailability(ny-1,nx  ,0, cnt+1 if dir == 0 else cnt+1001)
    checker += checkAvailability(ny  ,nx+1,1, cnt+1 if dir == 1 else cnt+1001)
    checker += checkAvailability(ny+1,nx  ,2, cnt+1 if dir == 2 else cnt+1001)
    checker += checkAvailability(ny  ,nx-1,3, cnt+1 if dir == 3 else cnt+1001)
    currCheckEls.remove([ny,nx,dir,cnt])
  if checker > 0:
    print("p1: ", checker)
    break

dg[ye][xe] = checker



def checkp2(y,x,prevElScore):
  if dg[y][x] != "x":
    if dg[y][x] < prevElScore:
      p2Arr.append([y,x,dg[y][x]])
      p2grid[y][x] = "0"
      return 1
  return 0

ShortestPath = 1
p2grid = copy.deepcopy(grid)
p2Arr = [[ye,xe,checker]]
while True:
  p2Copy = copy.deepcopy(p2Arr)
  p2Arr = []
  for el in p2Copy:
    ny,nx,elScore = el[0],el[1],el[2]
    if elScore == 0:
      print("shortest path ", ShortestPath)
      break
    ShortestPath += checkp2(ny-1 ,nx  ,elScore)
    ShortestPath += checkp2(ny   ,nx+1,elScore)
    ShortestPath += checkp2(ny+1 ,nx  ,elScore)
    ShortestPath += checkp2(ny   ,nx-1,elScore)
  if elScore == 0: break

# print("Hello")
def findDistance(y,x):

  def checkElems(cy,cx,cnt):
    nonlocal EFound
    nonlocal SFound
    if dg[cy][cx] != "x":
      if ldg[cy][cx] == "x":
        ldg[cy][cx] = cnt
        currElemens.append([cy,cx])
    if grid[cy][cx] == "S":
      SFound = True
    elif grid[cy][cx] == "E":
      EFound = True


  ldg = [["x" for i in range(len(grid[0]))] for j in range(len(grid))]
  ldg[y][x] = 0
  currElemens = [[y,x]]
  cnt = 1
  distToS,distToE,EFound,SFound, ESet,SSet = 0,0,False,False,False,False
  while True:
    elmsCpy = copy.deepcopy(currElemens)
    currElemens = []
    for el in elmsCpy:
      ny,nx = el[0],el[1]
      checkElems(ny-1,nx  , cnt)
      checkElems(ny  ,nx+1, cnt)
      checkElems(ny+1,nx  , cnt)
      checkElems(ny  ,nx-1, cnt)
    if SFound and not SSet:
      distToS = cnt
      SSet = True
    if EFound and not ESet:
      distToE = cnt
      ESet = True
    if EFound and SFound:
      return distToS + distToE 
    cnt += 1



p2Sum = 0
# y = 7
# x = 3
d1 = findDistance(2,15)
d2 = findDistance(3,15)
d3 = findDistance(4,15)
d4 = findDistance(5,15)
for j in range(len(dg)):
  for i in range(len(dg[0])):
    if isinstance(dg[j][i], (int)):
      dist_to_start_and_end = findDistance(j,i)

      if dist_to_start_and_end +1 == ShortestPath:
        p2Sum += 1
        p2grid[j][i] = 100

print("part2",p2Sum +2)

