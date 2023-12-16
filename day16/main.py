f = open("input.txt").read().splitlines()

data= [list(var) for var in f]
tData = []
for x in data:
  line = [False for _ in x]
  tData.append(line)

def move(i,j,dir,lim):
  if i < 0 or i > len(data[0]) or j < 0 or j > len(data):
    return
  lim += 1
  if lim > 200:
    return
  tData[i][j] = True
  
  if data[i][j] == ".":
    if dir == 2: i = i+1
    elif dir == 4: i = i-1
    if dir == 1: j = j+1
    elif dir == 4: j = j-1
    move(i,j,dir,lim)
  elif data[i][j] == '|':
    if dir in [2,4]:
      move(i-1,j, 1,lim)
      move(i+1,j, 3,lim)
    else:
      if dir == 1: j = j+1
      else: j = j-1
      move(i,j,dir,lim)
  elif data[i][j] == '-':
    if dir in [1,3]:
      move(i,j-1, 4,lim)
      move(i,j+1, 2,lim)
    else:
      if dir == 2: move(i+1,j,dir,lim)
      else: move(i-1, dir,lim)
  elif data[i][j] == '\\':
    if dir == 1: move(i,j-1, 4,lim)
    elif dir == 2: move(i+1,j,3,lim)
    elif dir == 3: move(i,j+1, 2,lim)
    elif dir == 4: move(i-1,j,1,lim)
  elif data[i][j] == '/':
    if dir == 1:   move(i,j+1,2,lim)
    elif dir == 2: move(i-1,j,1,lim)
    elif dir == 3: move(i,j-1,4,lim)
    elif dir == 4: move(i+1,j,3,lim)

# 1-north
# 2-east
# 3-south
# 4-west

move(0,0,2,0)
for x in tData:
  print(x)