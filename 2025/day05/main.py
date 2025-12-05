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


validRanges = []
for i,elemens in enumerate(fresh):
  k = [elemens[0], elemens[1]]
  intesects = 0
  isMatch = False
  for r in validRanges:
    if k[0] == r[0] and k[1] == r[1]:
      isMatch = True
      break
    if k[0] >= r[0] and k[1] <= r[1]:
      isMatch = True
      break
    elif k[0] < r[0] and k[1] > r[1]:
      r[0] = k[0]
      r[1] = k[1]
      isMatch = True
    elif k[0] >= r[0] and k[0] < r[1]:
      r[1] = k[1]
      isMatch = True 
    elif k[1] > r[0] and k[1] <= r[1]:
      r[0] = k[0]
      isMatch = True
  if not isMatch:
    validRanges.append(k)
while True:
  wasMatch = False
  for i,k in enumerate(validRanges):
    for j in range(0,i):
      r = validRanges[j]
      if k[0] == r[0] and k[1] == r[1]:
        raise Exception("Shouldn't be here")
      if max(k[0],r[0]) <= min(k[1],r[1]):
        merged = [min(k[0],r[0]), max(k[1],r[1])]
        validRanges.pop(i)
        validRanges.pop(j)
        validRanges.append(merged)
        wasMatch = True
        break

    if wasMatch: break
  if not wasMatch:
    break

for k in validRanges:
  p2 += k[1]-k[0]+1

print("Part1:",p1)
print("Part2:",p2)
