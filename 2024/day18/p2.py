import copy

# Import the time library
import time

# Calculate the start time
start = time.time()

b = 12
xlen, ylen = 6,6

b = 1024 
xlen,ylen = 70,70


g = [["." for i in range(xlen +1)] for j in range(ylen +1)]

ncells = []
cnt = 0
for k in open("input.txt"):
  x,y = k.strip().split(",")
  ncells.append([int(y),int(x)])
  g[int(y)][int(x)] = "#"




def checkIfPathAvailable():

  def checkEl(y,x,cnt):
    global xlen,ylen
    if 0<=y <=ylen and 0 <= x <= xlen:
      if g[y][x] == ".":
        if dg[y][x] == "x":
          dg[y][x] = cnt
          currEls.append([y,x])
          if y == ylen and x == xlen:
            return cnt
          return 0
    return 0

  cnt = 0
  dg = [["x" for i in range(xlen +1)] for j in range(ylen +1)]
  dg[0][0] = 0
  currEls = [[0,0]]
  while True:
    cpyEms = copy.deepcopy(currEls)
    currEls = []
    cnt += 1
    rs = 0
    for k in cpyEms:
      y,x = k[0],k[1]
      rs += checkEl(y-1 ,x  , cnt)
      rs += checkEl(y   ,x+1, cnt)
      rs += checkEl(y+1 ,x  , cnt)
      rs += checkEl(y   ,x-1, cnt)
    if rs != 0:
      return "Found"
    if len(currEls) == 0:
      return ""

el = 2
while True:
  res = checkIfPathAvailable()
  prev = el
  el = ncells.pop()
  if res == "":
    y,x = el[0],el[1]
    g[y][x] = "."
  else:
    sol = [prev[1],prev[0]]
    print("P2: ", sol )
    break



end = time.time()
length = end - start

# Show the results : this can be altered however you like
print("It took", length, "seconds!")
