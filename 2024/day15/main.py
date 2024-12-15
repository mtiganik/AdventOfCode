
p2grid = []
p1Grid = []
cmnds = ""
HasGotToCmnds = False
x,y = 0,0
indx = 0
i,j = 0,0


for k in open("input.txt"):
  if k == "\n":
    HasGotToCmnds = True
  if HasGotToCmnds:
    cmnds = cmnds + k.strip()
  else:
    m = k.strip()
    m = m.replace("#", "##")
    m = m.replace("O","[]")
    m = m.replace(".","..")
    m = m.replace("@","@.")
    p2Line = list(m)
    p1Line = list(k.strip())
    if "@" in p2Line:
      y,j = indx, indx
      x = p2Line.index("@")
      i = p1Line.index("@")
    p2grid.append(p2Line)
    p1Grid.append(p1Line)
    indx += 1

def checkAvailability(y,dy,ycnt,xs,xe):
  for i in [xs,xe]:
    elToCheck = p2grid[y+ycnt*dy][i] 
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
    if p2grid[y+ycnt*dy][i] == "#":
      raise Exception("shouldnt get here")
      return -1
    elif p2grid[y+ycnt*dy][i] == "[":
      moveY(y,dy,ycnt +1,i,i+1)
    elif p2grid[y+ycnt*dy][i] == "]":
      moveY(y,dy,ycnt +1,i-1,i)  
  p2grid[y+(ycnt-1)*dy][xs] = '.'
  p2grid[y+(ycnt-1)*dy][xe] = '.'
  p2grid[y+(ycnt)*dy][xs] = '['
  p2grid[y+(ycnt)*dy][xe] = ']'

def moveP2(char):
  global x,y
  dy = 1 if char == "v" else -1 if char == "^" else 0
  dx = 1 if char == ">" else -1 if char == "<" else 0

  if p2grid[y+dy][x+dx] == "#":
    return
  elif p2grid[y+dy][x+dx] == ".":
    p2grid[y][x] = "."
    p2grid[y+dy][x+dx] = "@"
    x,y = x +dx, y+dy
    return
  elif (char=="^" or char == "v"):
    ycnt = 2
    xs,xe = x,x
    if p2grid[y+dy][x] == "[": xe +=1
    else: xs -= 1
    res = checkAvailability(y,dy,ycnt,xs,xe)
    if res == -1: return
    else:
      # print("Got to move")
      if p2grid[y+dy][x] == "[":
        moveY(y,dy,ycnt,x,x+1)
      else:
        moveY(y,dy,ycnt,x-1,x)
      p2grid[y][x] = "."
      p2grid[y+dy][x] = "@"
      y = y+dy

      
  elif (char=="<" or char == ">"):
    cnt = 1
    while True:
      cnt += 1
      if p2grid[y][x+cnt*dx] == "#":
        return
      # left/right
      elif p2grid[y][x+cnt*dx] == ".":
        for i in range(x,x+cnt*dx,dx):
          if p2grid[y][i] == "[":p2grid[y][i] = "]"
          elif p2grid[y][i] =="]": p2grid[y][i] = "["
        p2grid[y][x+cnt*dx] = "[" if char == "<" else "]"
        p2grid[y][x] = "."
        p2grid[y+dy][x+dx] = "@"
        x,y = x +dx, y+dy
        return
  else:
    raise Exception("shouldnt get here")


def moveP1(char):
  global i,j
  dy = 1 if char == "v" else -1 if char == "^" else 0
  dx = 1 if char == ">" else -1 if char == "<" else 0

  if p1Grid[j+dy][i+dx] == "#":
    return
  elif p1Grid[j+dy][i+dx] == ".":
    p1Grid[j][i] = "."
    p1Grid[j+dy][i+dx] = "@"
    i,j = i +dx, j+dy
    return
  else:
    cnt = 1
    while True:
      cnt += 1
      if p1Grid[j+cnt*dy][i+cnt*dx] == "#":
        return
      elif p1Grid[j+cnt*dy][i+cnt*dx] == ".":
        p1Grid[j+cnt*dy][i+cnt*dx] = "O"
        p1Grid[j][i] = "."
        p1Grid[j+dy][i+dx] = "@"
        i,j = i +dx, j+dy
        return



for char in cmnds:
  moveP1(char)
  moveP2(char)


p1,p2 = 0,0

for j in range(len(p2grid)):
  for idx in range(len(p1Grid[0])):
    if p1Grid[j][idx] == "O":
        p1 += 100*j + idx

  for indx in range(len(p2grid[0])):
    if p2grid[j][indx] == "[":
        p2 += 100*j + indx

print("Part1: ",p1)
print("Part2: ",p2)
