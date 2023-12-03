
f = open("input.txt")
grid = []
row = ["."] # left padding
chars = ['.']

def isNumber(val):
  if(ord(val) >= 48 and ord(val) <= 57):
    return True
  return False

for x in f:
  for y in x.strip():
      if y not in chars and not isNumber(y):
        chars.append(y)
      row.append(y)
  row.append(".") # right padding
  grid.append(row)
  row = ["."]
chars.pop(0)

# paddings for avoiding indexErrors
grid.append(['.'] * len(grid[0])) # bottom
grid.insert(0, ['.']*len(grid[0])) # top


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

  vals.append(int(valAsString))


vals = []
for i, row in enumerate(grid):
  for j, el in enumerate(grid[i]):
    if(el in chars):

      #Top checking
      if isNumber(grid[i-1][j-1]): getNumFromGrid(i-1,j-1)
      if isNumber(grid[i-1][j]): getNumFromGrid(i-1,j)
      if isNumber(grid[i-1][j+1]): getNumFromGrid(i-1,j+1)
      # Bottom checking
      if isNumber(grid[i+1][j-1]): getNumFromGrid(i+1,j-1)
      if isNumber(grid[i+1][j]): getNumFromGrid(i+1,j)
      if isNumber(grid[i+1][j+1]): getNumFromGrid(i+1,j+1)
      #Left check
      if isNumber(grid[i][j-1]): getNumFromGrid(i,j-1)
      # Right check
      if isNumber(grid[i][j+1]): getNumFromGrid(i,j+1)

# # DEBUG what is left from grid:
# for x in grid:
#   print("".join(x))

sum = 0
for x in vals:
  sum += x
print(sum)

