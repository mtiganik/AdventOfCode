
grid = []
cmnds = ""
HasGotToCmnds = False
x,y = 0,0
i = 0
for k in open("input.txt"):
  if k == "\n":
    HasGotToCmnds = True
  if HasGotToCmnds:
    cmnds = cmnds + k.strip()
  else:
    line = list(k.strip())
    if "@" in line:
      y = i
      x = line.index("@")
    grid.append(line)
    i += 1

def makeMove(char):
  global x,y
  dy = 1 if char == "v" else -1 if char == "^" else 0
  dx = 1 if char == ">" else -1 if char == "<" else 0

  if grid[y+dy][x+dx] == "#":
    return
  elif grid[y+dy][x+dx] == ".":
    grid[y][x] = "."
    grid[y+dy][x+dx] = "@"
    x,y = x +dx, y+dy
    return
  else:
    cnt = 1
    while True:
      cnt += 1
      if grid[y+cnt*dy][x+cnt*dx] == "#":
        return
      elif grid[y+cnt*dy][x+cnt*dx] == ".":
        grid[y+cnt*dy][x+cnt*dx] = "O"
        grid[y][x] = "."
        grid[y+dy][x+dx] = "@"
        x,y = x +dx, y+dy
        return

    


for char in cmnds:
  makeMove(char)

sum = 0

for j in range(len(grid)):
  for i in range(len(grid[0])):
    if grid[j][i] == "O":
        sum += 100*j + i


print(sum)
