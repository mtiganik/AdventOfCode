import sys
import numpy as np
np.set_printoptions(edgeitems=3, linewidth=100, precision=2, suppress=True)

f = open("input.txt").read().splitlines()
max_ = 1000

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
    newValI = (i+1, j)
    prevValCheckI = i
  elif dir == "RIGHT":
    OoRI, OoRV = j, width
    newValI = (i, j+1)
    prevValCheckI = j

  if OoRI == OoRV: return
  if tGrid[newValI] > currCnt + grid[newValI]:
    tGrid[newValI] = currCnt + grid[newValI]
def getRightMovesCnt(coord):
  i, j = coord
  rightCnt = 0
  for k in range(j,0,-1):
    if tGrid[i][j] == tGrid[i][j-1] + grid[i][j]:
      rightCnt += 1
    else: return rightCnt
  return rightCnt
def getDownMovesCnt(coord):
  i,j = coord
  downCnt = 0
  for k in range(i,0,-1):
    if tGrid[i][j] == tGrid[i-1][j] + grid[i][j]:
      downCnt += 1
    else: return downCnt
  return downCnt
breaker = True
while(breaker):
  coords = getCoordsOfCurrCnt(currCnt)
  for coord in coords:
    i,j = coord
    print(coord)
    rightCnt, downCnt = getRightMovesCnt(coord), getDownMovesCnt(coord)
    if downCnt > 0 and rightCnt > 0:
      print("Error")
    if j <= 3 and i == 0:
      appendAdjacent(coord,'RIGHT')
    if i <= 3 and j== 0:
      appendAdjacent(coord,'DOWN')
    
    if downCnt == 0:
      if rightCnt < 4:
        appendAdjacent(coord,'RIGHT')
      elif rightCnt < 10:
        appendAdjacent(coord,'RIGHT')
        appendAdjacent(coord,'DOWN')
      else:
        appendAdjacent(coord,'DOWN')
    else:
      if downCnt < 4:
        appendAdjacent(coord,'DOWN')
      elif downCnt < 10:
        appendAdjacent(coord,'RIGHT')
        appendAdjacent(coord,'DOWN')
      else:
        appendAdjacent(coord,'RIGHT')
    if coord == [height, width]:
      breaker = False
  currCnt += 1

print(tGrid)
