
data = []
for x in open("input.txt"):
  data.append(x.strip())


def findMas(y,x):
  pd, nd = data[y-1][x-1] + data[y+1][x+1], data[y-1][x+1] + data[y+1][x-1]
  matches = ["MS","SM"]
  if any(x in pd for x in matches) and any(x in nd for x in matches):
    return 1
  return 0

sum = 0
for y in range(1,len(data)-1):
  for x in range(1,len(data[0])-1):
    if data[y][x] == 'A':
      sum += findMas(y,x,)

print(sum)