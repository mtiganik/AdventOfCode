# import time
import copy
# start = time.time()

# end = time.time()
# length = end - start

# print("It took", length, "seconds!")


data = []
x = 0
y = 0
iter = 0
for k in open("input.txt"):
  k = '*' + k.strip() + '*'
  if '^' in k:
    y = iter
    x = k.find('^')
    # k = k.replace("^",'s')

  data.append(list(k))
  iter += 1
data.insert(0,['*']*len(data[0]))
data.append(['*']*len(data[0]))
eData = copy.deepcopy(data)
y = y+1
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
    data[y+dy*cnt][x+ dx*cnt] = '^' if d == 0 else '>' if d == 1 else 'v' if d == 2 else '<'
    cnt += 1




dir = 0
while True:
  manipulate(dir%4)
  dir += 1
  if(data[y][x] == "*"): break

p1Sum = 0
for k in data:
  print("".join(k))
  p1Sum += k.count("^") + k.count(">")+k.count("v")+k.count("<")
print(p1Sum)
dirs = ["^",">","v","<"]


def makeMove(d,y,x,dir):
  cnt = 0
  dy = -1 if dir == 0 else 1  if dir == 2 else 0
  dx = 1  if dir == 1 else -1 if dir == 3 else 0
  prev = d[y][x]
  while True:
    if d[y+dy*cnt][x+ dx*cnt] == '#':
      y = y + dy*cnt - dy
      x = x + dx*cnt - dx
      d[y][x] = prev
      return (y,x)
    if d[y+dy*cnt][x+ dx*cnt] == '*':
      y = y + dy*cnt
      x = x + dx*cnt
      return (y,x)
    prev = d[y+dy*cnt][x+ dx*cnt]
    d[y+dy*cnt][x+ dx*cnt] = '^' if dir == 0 else '>' if dir == 1 else 'v' if dir == 2 else '<'
    cnt += 1


def checkForCycle(d, y,x,dir):
  while True:
    (y,x) = makeMove(d,y,x,dir)
    dir = (dir+1)%4
    npv = d[y][x]
    if(npv == "*"): return 0
    if (npv == "^" and dir == 0) or (npv == ">" and dir == 1) or (npv == "v" and dir == 2) or (npv=="<" and dir == 3):
      return 1


p2Sum = 0
for j in range(len(data)):
  for i in range(len(data[0])):
    if data[j][i] in dirs and not (j == sY and i == sX):
      nd = copy.deepcopy(eData)
      el = data[j][i]
      nd[j][i] = "#"
      # sj = j+1 if el == "^" else j-1 if el == "v" else j
      # si = i+1 if el == "<" else i-1 if el == ">" else i
      # dir = 1 if el == "^" else 2 if el == ">" else 3 if el == "v" else 0
      # if (j == 7 and i == 4):
      #   print("db")
      # if (j == 8 and i == 7):
      #   print("")
      # if (j == 8 and i == 8):
      #   print("")
      # if j == 9 and i == 2:
      #   print("")
      # if j == 9 and i == 4:
      #   print("")
      # if j== 10 and i == 8:
      #   print("")
      p2Sum += checkForCycle(nd,sY,sX,0)

print(p2Sum)
