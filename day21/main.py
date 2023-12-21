f = open("input.txt").read().splitlines()
import numpy as np
grid = []
tGrid = []
max = 100
start = (0,0)
for idx,x in enumerate(f):
  vals = list(x)
  if 'S' in vals:
    start = (idx, vals.index("S"))
  grid.append(vals)
for x in grid:
  val = [max for _ in range(len(grid[0]))]
  tGrid.append(val)
tGrid[start[0]][start[1]] = 0

def makeMove(i,j,iter):
  if i in range(0,len(grid)) and j in range(0,len(grid[0])):
    if grid[i][j] == "." and tGrid[i][j] == max:
      tGrid[i][j] = iter
iter = 0
for i in range(64):
  iter +=1 
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if tGrid[i][j] == iter-1:
        makeMove(i+1,j,iter)
        makeMove(i-1,j,iter)
        makeMove(i,j-1,iter)
        makeMove(i,j+1,iter)
stepCnt = 0
for i in range(len(tGrid)):
  for j in range(len(tGrid[0])):
    if tGrid[i][j] != max:
      if tGrid[i][j] % 2 == 0:
        grid[i][j] = "O"
        stepCnt += 1

for x in grid:
  print("".join(x))
print(stepCnt)