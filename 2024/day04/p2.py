
data = []
for x in open("input.txt"):
  data.append(x.strip())


def findMas(y,x):
  ul,ur,dr,dl = data[y-1][x-1], data[y-1][x+1],data[y+1][x+1],data[y+1][x-1]
  if ul == dr or ur == dl: return 0
  if all(x in ul+dr for x in ["M","S"]) and all(x in ur+dl for x in ["M","S"]):
    return 1
  return 0

sum = 0
for y in range(1,len(data)-1):
  for x in range(1,len(data[0])-1):
    if data[y][x] == 'A':
      sum += findMas(y,x,)

print(sum)