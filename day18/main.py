f = open("input.txt").read().splitlines()

def getHex(inp):
  return int(inp[-2:-1:]), int(inp[2:7:], 16)

def getNewVertic(dir,cnt, prevIndex):
  i,j = prevIndex
  if dir in ['R',0] :
    return (i,j+cnt)
  elif dir in ['D',1]:
    return (i+cnt,j)
  elif dir in ['L',2]:
    return (i,j-cnt)
  elif dir in ['U',3]:
    return (i-cnt,j)


p1C,p2C = (0,0), (0,0)
p1v,p2v = [], []
p1ec,p2ec = 0, 0
for x in f:
  dir1, p1cnt = x.split()[0], int(x.split()[1])
  dir2, p2cnt = getHex(x.split()[2])
  p1ec, p2ec = p1ec+p1cnt, p2ec+p2cnt
  p1C = getNewVertic(dir1,p1cnt,p1C)
  p2C = getNewVertic(dir2,p2cnt,p2C)
  p1v.append(p1C)
  p2v.append(p2C)

def getArea(vertices):
  firstSum, secSum = 0,0
  for k in range(-1,len(vertices)-1, 1):
    x1,y1 = vertices[k]
    x2,y2 = vertices[k+1]
    firstSum += x1*y2
    secSum += y1*x2
  return abs(firstSum-secSum)/2

print("Part1:", int(getArea(p1v)+p1ec/2 +1))
print("Part2:", int(getArea(p2v) + p2ec/2 +1))
