f = open("input.txt")
grid = []
row = ["."]

def isNumber(val):
  if(ord(val) >= 48 and ord(val) <= 57):
    return True
  return False

for x in f:
  for y in x.strip():
      row.append(y)
  row.append(".")
  grid.append(row)
  row = ["."]

grid.append(['.'] * len(grid[0]))
grid.insert(0, ['.']*len(grid[0]))


def getNumFromGrid(y,x):
  valAsString = grid[y][x]
  grid[y][x] = '.'
  xmin1 = grid[y][x-1]
  xplus1, xplus2 = '.', '.'
  if isNumber(xmin1):
    valAsString = xmin1 + valAsString 
    grid[y][x-1] = '.'
    xmin2 = grid[y][x-2]
    if isNumber(xmin2):
      valAsString = xmin2 + valAsString
      grid[y][x-2] = '.'
  xplus1 = grid[y][x+1]
  if isNumber(xplus1):
    valAsString = valAsString + xplus1
    grid[y][x+1] = '.'
    xplus2 = grid[y][x+2]
    if isNumber(xplus2):
      valAsString = valAsString + xplus2
      grid[y][x+2] = '.'
  return  int(valAsString)

sum = 0
vals = []
for i, row in enumerate(grid):
  for j, el in enumerate(grid[i]):
    if(el == '*'):
      currElems = []
      #Top checking
      if isNumber(grid[i-1][j-1]): currElems.append(getNumFromGrid(i-1,j-1))
      if isNumber(grid[i-1][j]):   currElems.append(getNumFromGrid(i-1,j))
      if isNumber(grid[i-1][j+1]): currElems.append(getNumFromGrid(i-1,j+1))

      # Bottom checking
      if isNumber(grid[i+1][j-1]): currElems.append(getNumFromGrid(i+1,j-1))
      if isNumber(grid[i+1][j]):   currElems.append(getNumFromGrid(i+1,j))
      if isNumber(grid[i+1][j+1]): currElems.append(getNumFromGrid(i+1,j+1))
      #Left check
      if isNumber(grid[i][j-1]):   currElems.append(getNumFromGrid(i,j-1))
      # Right check
      if isNumber(grid[i][j+1]):   currElems.append(getNumFromGrid(i,j+1))

      if len(currElems) == 2:
        sum += currElems[0]*currElems[1]


print(sum)