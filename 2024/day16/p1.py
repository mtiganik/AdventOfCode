import copy

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

def checkAvailability(y,x,dir, cnt):
  if grid[y][x]== ".":
    if dg[y][x] =="x":
      dg[y][x] = cnt
      currCheckEls.append([y,x])
  if grid[y][x] == "E":
    return 1
  return 0


dg[y][x] = 0
currCheckEls = [[y,x]]
checkAvailability(y-1, x  ,0, 1)
checkAvailability(y  , x+1,1, 1)
currCnt = 1
while True:
  copyList = copy.deepcopy(currCheckEls)
  # currCheckEls = []
  checker = 0
  for k in copyList:
    ny,nx,dir, cnt = k[0],k[1],k[2], k[3]
    checker += checkAvailability(ny-1,nx  ,0, cnt if dir == 0 else cnt+1000)
    checker += checkAvailability(ny  ,nx+1,1, cnt if dir == 1 else cnt+1000)
    checker += checkAvailability(ny+1,nx  ,2, cnt if dir == 2 else cnt+1000)
    checker += checkAvailability(ny  ,nx-1,3, cnt if dir == 3 else cnt+1000)
    currCheckEls.remove([ny,nx,dir,cnt])
  if checker > 0:
    print("End: ", currCnt)
    break
  # currCnt += 1

print("End")