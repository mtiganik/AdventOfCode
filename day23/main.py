import sys


f = open("input.txt").read().splitlines()
def checkmvnt(i,j,iter,Stc,oTGrid):
  if oTGrid[i][j] < Max: return False
  if grid[i][j] == "#": return False
  if grid[i][j] == ".":
    oTGrid[i][j] = iter + 1
    return True
  elif grid[i][j] == Stc:
    print(Stc, " ",i, ", ", j, " cnt: ",iter)
    if i == 10 and j == 21:
      print("")
    oTGrid[i][j] = iter + 1
    ntGrid = oTGrid.copy()
    movePath(i,j,iter+1,ntGrid)
    return True

def movePath(i,j,iter,ctgrid):
  wasMove = True
  while(wasMove):
    wasMove = False
    for i in range(0,len(grid[0])):
      for j in range(0,len(grid)):
        if ctgrid[i][j] == iter:
          if i == len(grid)-1 and j == len(grid[0])-2:
            print("Reached end, ", iter)
            results.append(iter)
            return True

          wasMove = checkmvnt(i+1,j,iter,"v",ctgrid) or wasMove 
          wasMove = checkmvnt(i-1,j,iter,"^",ctgrid) or wasMove
          wasMove = checkmvnt(i,j-1,iter,"<",ctgrid) or wasMove
          wasMove = checkmvnt(i,j+1,iter,">",ctgrid) or wasMove
    iter += 1
  print("node ended")

grid = [list(var) for var in f]
Max = sys.maxsize
tGrid = [[Max for i in range(len(grid[0]))] for j in range(len(grid)) ]
tGrid[0][1] = 0
# ci,cj,iter = 0,1,0
results = []
# print(len(grid))
# print(len(grid[0]))
movePath(0,1,0,tGrid)
print("Part1: ", max(results))
