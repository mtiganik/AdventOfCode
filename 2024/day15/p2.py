
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
    k = k.strip()
    k = k.replace("#", "##")
    k = k.replace("O","[]")
    k = k.replace(".","..")
    k = k.replace("@","@.")
    line = list(k)
    if "@" in line:
      y = i
      x = line.index("@")
    grid.append(line)
    i += 1

def checkAvailability(y,dy,ycnt,xs,xe):
  for i in [xs,xe]:
    elToCheck = grid[y+ycnt*dy][i] 
    res = 0
    if elToCheck== "#": return -1
    elif elToCheck == "[":
      res = checkAvailability(y, dy, ycnt+1, i, i+1)
    elif elToCheck == "]":
      res = checkAvailability(y, dy, ycnt+1, i-1, i)
    if res == -1:
      return -1
  return 1

def moveY(y,dy,ycnt,xs,xe):

  for i in [xs,xe]:
    if grid[y+ycnt*dy][i] == "#":
      raise Exception("shouldnt get here")
      return -1
    elif grid[y+ycnt*dy][i] == "[":
      moveY(y,dy,ycnt +1,i,i+1)
    elif grid[y+ycnt*dy][i] == "]":
      moveY(y,dy,ycnt +1,i-1,i)  
  grid[y+(ycnt-1)*dy][xs] = '.'
  grid[y+(ycnt-1)*dy][xe] = '.'
  grid[y+(ycnt)*dy][xs] = '['
  grid[y+(ycnt)*dy][xe] = ']'

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
  elif (char=="^" or char == "v"):
    ycnt = 2
    xs,xe = x,x
    if grid[y+dy][x] == "[": xe +=1
    else: xs -= 1
    res = checkAvailability(y,dy,ycnt,xs,xe)
    if res == -1: return
    else:
      # print("Got to move")
      if grid[y+dy][x] == "[":
        moveY(y,dy,ycnt,x,x+1)
      else:
        moveY(y,dy,ycnt,x-1,x)
      grid[y][x] = "."
      grid[y+dy][x] = "@"
      y = y+dy

      
  elif (char=="<" or char == ">"):
    cnt = 1
    while True:
      cnt += 1
      if grid[y][x+cnt*dx] == "#":
        return
      # left/right
      elif grid[y][x+cnt*dx] == ".":
        for i in range(x,x+cnt*dx,dx):
          if grid[y][i] == "[":grid[y][i] = "]"
          elif grid[y][i] =="]": grid[y][i] = "["
        grid[y][x+cnt*dx] = "[" if char == "<" else "]"
        grid[y][x] = "."
        grid[y+dy][x+dx] = "@"
        x,y = x +dx, y+dy
        return
  else:
    raise Exception("shouldnt get here")

    


for char in cmnds:
  makeMove(char)

sum = 0

for j in range(len(grid)):
  for i in range(len(grid[0])):
    if grid[j][i] == "[":
        sum += 100*j + i


print(sum)
