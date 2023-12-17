import sys
import numpy as np
np.set_printoptions(edgeitems=3, linewidth=100, precision=2, suppress=True)

f = open("input.txt").read().splitlines()
max_ = 100000

grid = np.array([list(map(int,var)) for var in f])
tGrid = np.full_like(grid, max_)
tGrid[0][0] = 0
width = len(tGrid[0]) -1
height = len(tGrid) -1
currCnt = 0

def getCoordsOfCurrCnt(cnt):
  coords = []
  for i in range(len(tGrid)):
    for j in range(len(tGrid[0])):
      if tGrid[i][j] == cnt:
        coords.append([i,j])
  return coords



def appendAdjacent(curr,dir):
  i,j = curr
  currI = (i,j)
  if dir == 'DOWN':
    OoRI, OoRV = curr[0], height
    prev1I, prev2I, prev3I, prev4I = (i-1,j), (i-2,j), (i-3,j), (i-4,j)
    newValI = (i+1, j)
    prevValCheckI = i
  elif dir == "RIGHT":
    OoRI, OoRV = j, width
    prev1I, prev2I, prev3I, prev4I = (i,j-1), (i,j-2), (i,j-3), (i,j-4)
    newValI = (i, j+1)
    prevValCheckI = j
  elif dir == "UP":
    OoRI, OoRV = i, 0
    prev1I, prev2I, prev3I, prev4I = (i+1,j), (i+2,j), (i+3,j), (i-4,j)
    newValI = (i-1, j)
    prevValCheckI = height - i
  elif dir == "LEFT":
    OoRI, OoRV = j, 0
    prev1I, prev2I, prev3I, prev4I = (i,j+1), (i,j+2), (i,j+3), (i,j+4)
    newValI = (i, j-1)
    prevValCheckI = width - j

  if OoRI == OoRV: return
  if prevValCheckI > 4:
    prev1, prev2, prev3, prev4 = tGrid[prev1I], tGrid[prev2I], tGrid[prev3I], tGrid[prev4I]
    if currCnt - prev1 == grid[currI] and prev1 - prev2 == grid[prev1I]:
      if prev2 - prev3 == grid[prev2I] and prev3 - prev4 == grid[prev3I]:
        return
  if tGrid[newValI] > currCnt + grid[newValI]:
    tGrid[newValI] = currCnt + grid[newValI]
  
while(tGrid[height][width] == max_):
  coords = getCoordsOfCurrCnt(currCnt)
  for coord in coords:
    appendAdjacent(coord,'DOWN')
    appendAdjacent(coord,'RIGHT')
    appendAdjacent(coord,'UP')
    appendAdjacent(coord,'LEFT')
  currCnt += 1

print(currCnt)
