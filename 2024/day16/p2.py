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

def checkp2(y,x,prevElScore):
  if dg[y][x] != "x":
    if dg[y][x] < prevElScore:
      p2Arr.append([y,x,dg[y][x]])
      p2grid[y][x] = "0"
      return 1
  return 0

p2Cnt = 1
p2grid = copy.deepcopy(grid)
p2Arr = [[ye,xe,checker]]
while True:

  p2Copy = copy.deepcopy(p2Arr)
  p2Arr = []
  for el in p2Copy:
    ny,nx,elScore = el[0],el[1],el[2]
    if elScore == 0:
      print("found ", p2Cnt)
      break
    p2Cnt += checkp2(ny-1 ,nx  ,elScore)
    p2Cnt += checkp2(ny   ,nx+1,elScore)
    p2Cnt += checkp2(ny+1 ,nx  ,elScore)
    p2Cnt += checkp2(ny   ,nx-1,elScore)

