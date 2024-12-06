import time

start = time.time()
x,y, iter, moves, data = 0,0,0, [],[]

for k in open("input.txt"):
  k = '*' + k.strip() + '*'
  if '^' in k:
    y = iter +1
    x = k.find('^')
  data.append(list(k))
  iter += 1
moves.append((y,x,0))
data.insert(0,['*']*len(data[0]))
data.append(['*']*len(data[0]))


def isInMoves(y,x,mvs): return True if any(k[0] == y and k[1] == x for k in mvs) else False

sX,sY = x,y
def manipulate(d):
  cnt = 0
  global x
  global y
  dy = -1 if d == 0 else 1 if d == 2 else 0
  dx = 1 if d == 1 else -1 if d == 3 else 0
  while True:
    if data[y+dy*cnt][x+ dx*cnt] == '#':
      y = y + dy*cnt - dy
      x = x + dx*cnt - dx
      return
    if data[y+dy*cnt][x+ dx*cnt] == '*':
      y = y + dy*cnt
      x = x + dx*cnt
      return
    if not isInMoves(y+dy*cnt, x+ dx*cnt, moves):
      moves.append((y+dy*cnt, x+ dx*cnt, d))
    cnt += 1


dir = 0
while True:
  manipulate(dir%4)
  dir += 1
  if(data[y][x] == "*"): break
p1 = len(moves)

print("Part 1: ", p1)

def isSamePlaceAndDirection(y,x,dir,nm):
  for k in nm:
    if y== k[0] and x == k[1] and dir == k[2]:
      return True
  return False

def makeMove(y,x,dir, nms):
  cnt = 0
  dy = -1 if dir == 0 else 1  if dir == 2 else 0
  dx = 1  if dir == 1 else -1 if dir == 3 else 0
  while True:
    if data[y+dy*cnt][x+ dx*cnt] == '#':
      y = y + dy*cnt - dy
      x = x + dx*cnt - dx
      return (y,x, nms)
    if data[y+dy*cnt][x+ dx*cnt] == '*':
      y = y + dy*cnt
      x = x + dx*cnt
      return (y,x, nms)
    cnt += 1



p2Sum = 0
moves.pop(0)
for k in moves:
  j,i,d = k[0],k[1],k[2]
  data[j][i] = '#'
  y = j + 1 if d == 0 else j-1 if d == 2 else j
  x = i+1 if d == 3 else i-1 if d == 1 else i
  dir = 1 if d == 0 else 2 if d == 1 else 3 if d == 2 else 0

  nm = []
  while True:
    (y,x,nm) = makeMove(y,x,dir,nm)
    dir = (dir+1)%4
    if data[y][x] == "*": 
      break
    if isSamePlaceAndDirection(y,x,dir, nm):
      p2Sum += 1
      break
    nm.append((y,x,dir))
  data[j][i] = '.'



print("Part 2: ", p2Sum)

# https://youtu.be/x-igwLj5mXo