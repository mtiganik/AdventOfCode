import copy

lenx = 6
bites = 12

lenx = 70
bites = 1024

g = [["." for i in range(lenx +1)] for j in range(lenx+1)]
dg = [["x" for i in range(lenx +1)] for j in range(lenx+1)]

cnt = 0
for k in open("input.txt"):
  cnt += 1
  x,y = k.strip().split(",")
  g[int(y)][int(x)] = "#"
  if cnt >= bites:
    break

def checkElms(y,x,cnt):
  global lenx
  if 0 <= y <= lenx and 0 <= x <= lenx:
    if g[y][x] == ".":
      if dg[y][x] == "x":
        dg[y][x] = cnt
        currElms.append([y,x])
        if y == lenx and x == lenx:
          return cnt
  return 0

dg[0][0] = 0
currElms = [[0,0]]
cnt = 0
while True:
  copyEl = copy.deepcopy(currElms)
  currElms = []
  res = 0
  cnt += 1
  for el in copyEl:
    y,x = el[0],el[1]
    res += checkElms(y-1,x  ,cnt)
    res += checkElms(y  ,x+1,cnt)
    res += checkElms(y+1,x  ,cnt)
    res += checkElms(y  ,x-1,cnt)
  if res != 0:
    print("Found:",cnt)
    break
  if len(currElms) == 0:
    raise Exception("!")