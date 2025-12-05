f = open("input.txt")
fresh = []
freshBool = True
cnt = 0
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
        print("ID in range: ", available)
        cnt += 1
        break

print(cnt)