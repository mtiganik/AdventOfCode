file ="input.txt"
p1Res, p2Res = 0,0

def p1Calc(inp):
  res = 0
  if inp == "":
    return 0
  s,e = inp.split("-")
  if len(s) == len(e) and len(s) % 2 != 0:
    return 0
  if len(s) % 2 != 0 and len(e) %2 == 0:
    s = "1" + "0"*(len(e) -1)
  if len(s) % 2 == 0 and len(e) %2 != 0:
    e = "9"*(len(s))

  halfSize = int(len(s) / 2)
  start, stop = int(s), int(e)
  for i in range(start, stop+1):
    i1,i2 = str(i)[0:halfSize], str(i)[halfSize:]
    if i1 == i2:
      res += i
  return res

def p2Calc(inp):
  res = 0
  if inp == "":
    return 0
  s,e = inp.split("-")
  if len(s) == 1:
    print("manual check for ", inp, " add results from ", inp, " manually to p2 result")
    return 0
  halfSize = int(len(s) / 2)
  start, stop = int(s), int(e)
  #print(inp, ":")
  for i in range(start, stop+1):
    for n in range(1,int(len(e)+1 / 2)):
      line = str(i)
      arr = [line[i:i+n] for i in range(0, len(line),n)]
      if arr.count(arr[0]) == len(arr):
        resStr = "".join(arr)
        #print(resStr)
        res += int(resStr)
        break
  return res


for x in open(file):
  elms = x.strip().split(",")
  for k in elms:
    p1Res += p1Calc(k)

print("Part 1:", p1Res)

for x in open(file):
  elms = x.strip().split(",")
  for k in elms:
    p2Res += p2Calc(k)


print("part 2:", p2Res, " (plus manual add)" )