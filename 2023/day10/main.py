import sys
f = open('input.txt')
grid = []
lenGrid = []
max = sys.maxsize
for x in f:
  x = x.strip()
  x = "." + x + "."
  grid.append(list(x))
  lenGrid.append([max] * len(x))
grid.insert(0, ['.'] * len(grid[1]))
grid.append(['.'] * len(grid[1]))
lenGrid.insert(0, [max]*len(lenGrid[1]))
lenGrid.append([max]*len(lenGrid[1]))


for i in range(len(grid)):
  for j in range(len(grid[0])):
    if(grid[i][j] == 'S'):
      lenGrid[i][j] = 0
      # can you move up
      if(grid[i-1][j] in ['|', '7', 'F']):
        lenGrid[i-1][j] = 1
      # kas saad alla minna
      if(grid[i+1][j] in ['|', 'L', 'J']):
        lenGrid[i+1][j] = 1
      # kas paremale
      if(grid[i][j+1] in ['J', '-', '7']):
        lenGrid[i][j+1] = 1
      # kas vasakule
      if(grid[i][j-1] in ['-', 'L', 'F']):
        lenGrid[i][j-1] = 1
def changeLenGrid(i,j, wasChange):
  if lenGrid[i][j] == max:
    lenGrid[i][j] = steps+1
    return True
  return wasChange
steps = 0
wasChange = True
while wasChange:
  wasChange = False
  steps += 1
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if lenGrid[i][j] == steps:
        # can you move up
        if grid[i][j] in ['|', 'L', 'J'] and grid[i-1][j] in ['|', '7', 'F']:
          wasChange = changeLenGrid(i-1,j, wasChange)

        # can you move down:
        if grid[i][j] in ['|', '7', 'F'] and grid[i+1][j] in ['|', 'L', 'J']:
          wasChange = changeLenGrid(i+1,j,wasChange)

        # can you move right
        if grid[i][j] in ['-', 'L', 'F'] and grid[i][j+1] in ['J', '-', '7']:
          wasChange = changeLenGrid(i,j+1,wasChange)

        # kas vasakule
        if grid[i][j] in ['J', '-', '7'] and grid[i][j-1] in ['-', 'L', 'F']:
          wasChange = changeLenGrid(i,j-1,wasChange)


# Part 2:
#NB Check your input, if 'S' behaves like "|", "J", "L", then leave
# 'S' in array, otherwise remove it
array = ["|", "J", "L", "S"]

for i in range(len(grid)):
  for j in range(len(grid[0])):
    if lenGrid[i][j] == max:
      grid[i][j] = "."

def getNumberOfTilesLeft(i,j):
  cnt = 0
  for idx in range(j):
    if grid[i][idx] in array:
      cnt += 1
  return cnt 
part2Sum = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == ".":
      numOfTilesLeft = getNumberOfTilesLeft(i,j)
      if numOfTilesLeft % 2 == 1:
        part2Sum += 1

#My time and rank:
print("Part 1:", steps) # 01:10:56   5035
print("Part 2:", part2Sum) # 01:44:30   2019
