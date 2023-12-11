f = open("input.txt").read().splitlines()
grid = []
for x in f:
  grid.append([*x])

# for x in grid:
#   print("".join(x))
print("len(grid[0]) start: ", len(grid[0]))
print("len(grid) start: ", len(grid))

for j in range(len(grid[0])-1,0,-1):
  needInjection = True
  for i in range(len(grid)):
    if grid[i][j] == '#':
      needInjection = False
  if needInjection:
    for i in range(len(grid)):
      val = grid[i]
      val.insert(j,'.')
      del grid[i]
      grid.insert(i,val)


# Horisontal injection
Emptyhorizontal = ['.']*len(grid[0])
for ix in range(len(grid)-1,0,-1):
  if '#' not in grid[ix]:
    grid.insert(ix, Emptyhorizontal)

print("len(grid[0]) end: ", len(grid[0]))
print("len(grid) end: ", len(grid))

for x in grid:
  print("".join(x))

