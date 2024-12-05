
data = []
for x in open("input.txt"):
  data.append(x.strip())


def findMatch(y,x,dy,dx):
  if dy > 0:
    if y+3*dy > len(data)-1: return 0
  elif dy < 0:
    if y+3*dy < 0: return 0
  if dx > 0:
    if x+3*dx > len(data)-1: return 0
  elif dx < 0:
    if x+3*dx < 0: return 0
  if data[y+dy][x+dx] == "M" and data[y+2*dy][x+2*dx] == "A" and data[y+3*dy][x+3*dx]=="S":
    return 1
  return 0
sum = 0
for y in range(len(data)):
  for x in range(len(data[0])):
    if data[y][x] == 'X':
      sum += findMatch(y,x,-1, 1)
      sum += findMatch(y,x, 0, 1)
      sum += findMatch(y,x, 1, 1)
      sum += findMatch(y,x, 1, 0)
      sum += findMatch(y,x, 1,-1)
      sum += findMatch(y,x, 0,-1)
      sum += findMatch(y,x,-1,-1)
      sum += findMatch(y,x,-1, 0)

print("Part1: ", sum)
def checkXMAS(y,x):
  pd = data[y-1][x-1] + data[y+1][x+1]
  nd = data[y+1][x-1] + data[y-1][x+1]
  matches = ["MS","SM"]
  if any(x in pd for x in matches) and any(x in nd for x in matches):
    return 1
  return 0

sum = 0
for y in range(1,len(data)-1):
  for x in range(1, len(data[0])-1):
    if data[y][x] == "A":
      sum += checkXMAS(y,x)

print("Part2: ", sum)
