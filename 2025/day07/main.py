f = open("input.txt")
cnt = 0
grid = []
for x in f:
  arr = list(x.strip())
  grid.append(arr)

start = grid[0].index("S")
grid[0][start] = "|"

for i in range(1,len(grid)):
  for j in range(0,len(grid[0])):
    if grid[i-1][j] =="|":
      if grid[i][j] == "^":
        grid[i][j-1] = "|"
        grid[i][j+1] = "|"
        cnt += 1
      else:
        grid[i][j] = "|"

for k in grid:
  print("".join(k))

print(cnt)