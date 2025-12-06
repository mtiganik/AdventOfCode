f = open("input.txt")
fresh = []
freshBool = True
p1 = p2 = 0

for x in f:
  if x == "\n":
    freshBool = False
  elif freshBool:
    [s,e] = x.split("-")
    fresh.append([int(s),int(e)])
  else:
    available = int(x)
    for k in fresh:
      if available in range(k[0],k[1]+1):
        p1 += 1
        break
while True:
  wasMatch = False
  for i,k in enumerate(fresh):
    for j in range(0,i):
      r = fresh[j]
      if max(k[0],r[0]) <= min(k[1],r[1]):
        merged = [min(k[0],r[0]), max(k[1],r[1])]
        fresh.pop(i)
        fresh.pop(j)
        fresh.append(merged)
        wasMatch = True
        break
    if wasMatch: break
  if not wasMatch:
    break

for k in fresh:
  p2 += k[1]-k[0]+1

print("Part1:",p1)
print("Part2:",p2)
