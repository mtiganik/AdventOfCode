f = open("input.txt")
count = 0

def findInvalidIds(inp):
  res = 0
  if inp == "":
    return 0
  s,e = inp.split("-")
  if len(e) - len(s) > 2:
    raise Exception("too big number scale")
  if len(s) == len(e) and len(s) % 2 != 0:
    return 0
  if len(s) % 2 != 0 and len(e) %2 == 0:
    s = "1" + "0"*(len(e) -1)
  if len(s) % 2 == 0 and len(e) %2 != 0:
    e = "9"*(len(s))

  # split start to 2 elems
  halfSize = int(len(s) / 2)
  # s1,s2 = s[0:halfSize], s[halfSize:]
  # e1,e2 = e[0:halfSize], e[halfSize:]
  # print(s1, " - ", s2)
  start, stop = int(s), int(e)
  for i in range(start, stop+1):
    i1,i2 = str(i)[0:halfSize], str(i)[halfSize:]
    if i1 == i2:
      # print("valid: ", i1,i2)
      res += i
  return res

for x in f:
  elms = x.strip().split(",")
  for k in elms:
    count += findInvalidIds(k)

print("res:", count)