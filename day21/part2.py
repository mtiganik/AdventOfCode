f = open("input.txt").read().splitlines()
grid = []
start = (0,0)
for idx,x in enumerate(f):
  vals = list(x)
  if 'S' in vals:
    start = (idx, vals.index("S"))
  grid.append(vals)

odd,even = 0,0
for i in range(131):
  for j in range(131):
    if grid[i][j] != "#":
      if (i+j)%2 == 0:even += 1
      else: odd += 1

# OK
#Up right
evenUpRight,oddUpRight = 0,0
for i in range(65):
  for j in range(65+i, 131):
    if grid[i][j] != "#":
      if (i+j)%2 == 0:evenUpRight += 1
      else: oddUpRight += 1

#DownRight
evenDownRight, oddDownRight = 0,0
for i in range(65,131):
  for j in range(131+65-i,131):
    if grid[i][j] != "#":
      if (i+j)%2 == 0:evenDownRight += 1
      else: oddDownRight += 1
#DownLeft
evenDownLeft, oddDownLeft = 0,0
for i in range(65,131):
  for j in range(0,i-65):
      if grid[i][j] != "#":
        if (i+j)%2 == 0:evenDownLeft += 1
        else: oddDownLeft += 1
#UpLeft
evenUpLeft, oddUpLeft = 0,0
for i in range(65):
  for j in range(65-i):
      if grid[i][j] != "#":
        if (i+j)%2 == 0:evenUpLeft += 1
        else: oddUpLeft += 1

#Check for unreachable points
for i in range(1,len(grid)-1):
  for j in range(1,len(grid[0])-1):
    if grid[i-1][j] == "#" and grid[i+1][j] == "#" and grid[i][j+1] == "#" and grid[i][j-1]=="#":
      if (i+j)%2 == 0:even -= 1
      else:odd -= 1
      # if (i+j) > 65:
      # elif 
      print("Unreachable point")
      


cnt = (evenDownLeft+evenDownRight+evenUpLeft+evenUpRight)*202300
cnt -=(oddDownLeft+oddDownRight+oddUpLeft+oddUpRight)*202300
cnt += 202301**2*even
cnt += 202300**2*odd
print("Part2:", cnt)

