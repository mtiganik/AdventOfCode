# f = open("input.txt")

count = 0
def findLargest(inp):
  res = ""
  lastIndex = 0
  digits = 2
  for n in range(digits,0,-1):
    currIndex = 0
    currMax = 0
    for i in range(lastIndex, len(inp)):
      if int(inp[i]) > currMax and len(inp[i:]) > n-1:
        currMax, currIndex = int(inp[i]), i
    lastIndex = currIndex +1
    res += str(currMax)
  print(res)
  return int(res)

    

for x in open("input.txt"):
  inp = x.replace("\n", "")
  count+= findLargest(inp)

print("Part2: ", count)