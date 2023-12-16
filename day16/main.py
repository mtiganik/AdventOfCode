f = open("input.txt").read().splitlines()

data= [list(var) for var in f]
tData = []
for x in data:
  line = [0 for _ in x]
  tData.append(line)

prims = [2,3,5,7,11]

# move(0,0,2)

beams = [[0,0,2]]
def move(i,j,dir):

  if i < 0 or i > len(data[0])-1 or j < 0 or j > len(data)-1:
    return

  cellVal = tData[i][j]
  if cellVal == 0:
    tData[i][j] = prims[dir]
  else:
    mod = cellVal % prims[dir]
    if mod != 0:
      tData[i][j] *= prims[dir]
    else: return
  
  if data[i][j] == ".":
    if dir == 1:   return move(i-1,j, dir)
    elif dir == 2: return move(i,j+1, dir)
    elif dir == 3: return move(i+1,j, dir)
    elif dir == 4: return move(i,j-1, dir)
    
  elif data[i][j] == '|':
    if dir in [2,4]:
      move(i-1,j, 1)
      move(i+1,j, 3)
    else:
      if dir == 1: i = i-1
      else: i = i+1
      return move(i,j,dir)
  elif data[i][j] == '-':
    if dir in [1,3]:
      move(i,j-1, 4)
      move(i,j+1, 2)
    else:
      if dir == 2: return move(i,j+1,dir)
      else: return move(i,j-1, dir)
  elif data[i][j] == '\\':
    if dir == 1: return move(i,j-1, 4)
    elif dir == 2: return move(i+1,j,3)
    elif dir == 3: return move(i,j+1, 2)
    elif dir == 4: return move(i-1,j,1)
  elif data[i][j] == '/':
    if dir == 1:   return move(i,j+1,2)
    elif dir == 2: return move(i-1,j,1)
    elif dir == 3: return move(i,j-1,4)
    elif dir == 4: return move(i+1,j,3)


cnt = 0
for x in tData:
  line = ''
  for y in x:
    if y == 0: char = '.'
    else:
      cnt += 1
      if y in [3,5,7,11]: char = '#'
      elif y == 3*5*7*11: char = '!'
      else: char = 'X'
    line = line + char
  print(line)

print("Part1: ", cnt)