import sys
f = open("input.txt").read().splitlines()

grid = [list(map(int,var)) for var in f]
max_ = sys.maxsize

tGrid = []
for x in grid:
  line = [max_ for _ in x]
  tGrid.append(line)
def getCoordsOfCurrCnt(cnt):
  coords = []
  for i in range(len(tGrid)):
    for j in range(len(tGrid[0])):
      if tGrid[i][j] == cnt:
        coords.append([i,j])
  return coords
width = len(tGrid[0]) -1
height = len(tGrid) -1
data = [[1,2,3],[4,5,6], [7,8,9]]
start = [1,1]
second = [1,2]
print(data[start])
print("")
def appendAdjacent(i,j,dir):
  curr = tGrid[i][j]
  if dir == 'DOWN':
    if i == height: return
    if i-4 > 0:
      prev1, prev2, prev3, prev4 = tGrid[i-1][j], tGrid[i-2][j], tGrid[i-3][j], tGrid[i-3][j]
      if curr-prev1 == grid[i][j] and prev1-prev2 == grid[i-1][j] and prev2-prev3 == grid[i-2][j] and prev3-prev4 ==grid[i-3][j]: 
        return
    if tGrid[i+1][j] > curr + grid[i+1][j]:
      tGrid[i+1][j] = curr + grid[i+1][j]
  
  elif dir == 'RIGHT':
    if j == width: return
    if j-4 > 0:
      prev1,prev2, prev3, prev4 = tGrid[i][j-1], tGrid[i][j-2], tGrid[i][j-3], tGrid[i][j-4]
      if curr-prev1 == grid[i][j] and prev1-prev2 == grid[i][j-1] and prev2-prev3 == grid[i][j-2] : 
        return
    if tGrid[i][j+1] > curr + grid[i][j+1]:
      tGrid[i][j+1] = curr + grid[i][j+1]
  elif dir == 'UP':
    if i == 0: return
    if height - i > 4:
      prev1,prev2, prev3, prev4 = tGrid[i+1][j], tGrid[i+2][j], tGrid[i+3][j], tGrid[i+4][j]
      if curr - prev1 == grid[i][j] and prev1-prev2 == grid[i+1][j] and prev2-prev3 == grid[i+2][j] and prev3-prev4 == grid[i+3]: 
        return
    if tGrid[i-1][j] > curr + grid[i-1][j]:
      tGrid[i-1][j] = curr + grid[i-1][j]
  elif dir == 'LEFT':
    if j == 0: return
    if width - j > 4:
      prev1, prev2, prev3, prev4 = tGrid[i][j+1], tGrid[i][j+2], tGrid[i][j+3], tGrid[i][j+4]
      if curr - prev1 == grid[i][j] and prev1-prev2 == grid[i][j+1] and prev2-prev3 == grid[i][j+2] and prev3-prev4 == grid[i][j+3]: 
        return
    if tGrid[i][j-1] > curr + grid[i][j-1]:
      tGrid[i][j-1] = curr + grid[i][j-1]

tGrid[0][0] = 0
currCnt = 0

while(tGrid[height][width] == max_):
  coords = getCoordsOfCurrCnt(currCnt)
  for coord in coords:
    i,j = coord[0], coord[1]
    appendAdjacent(i,j,'DOWN')
    appendAdjacent(i,j,'RIGHT')
    appendAdjacent(i,j,'UP')
    appendAdjacent(i,j,'LEFT')
  currCnt += 1

#debug
for i in range(len(tGrid)):
  for j in range(len(grid[0])):
    if tGrid[i][j] == max_:
      tGrid[i][j] == 0
for x in tGrid:
  print(x)
print(currCnt)
