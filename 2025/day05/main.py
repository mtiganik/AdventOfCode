f = open("input.txt")
fresh = []
freshBool = True
cnt = 0

for x in f:
  if x == "\n":
    break
    freshBool = False
  elif freshBool:
    [s,e] = x.split("-")
    #fresh.append(range(int(s),int(e)))
    fresh.append([int(s),int(e)])

# y = range(5,5)
print(len(range(5,5)))

currCnt = 0
validRanges = []
for i,elemens in enumerate(fresh):
  # currRanges = []
  k = [elemens[0], elemens[1]]

  intesects = 0
  isMatch = False
  for r in validRanges:
    # r = fresh[j]
    if k[0] == r[0] and k[1] == r[1]:
      isMatch = True
      break

      # raise Exception("Shouldnt be here")
    #A
    if k[0] >= r[0] and k[1] <= r[1]:
      # all the elements in this range have already been checked sum is 0
      isMatch = True
      break
    #D
    elif k[0] < r[0] and k[1] > r[1]:
      r[0] = k[0]
      r[1] = k[1]
      isMatch = True
    #B
    elif k[0] >= r[0] and k[0] < r[1]:
      #split k elemens
      r[1] = k[1]
      isMatch = True 
    #C
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
  cnt += k[1]-k[0]+1

print(cnt)
print("Hello")