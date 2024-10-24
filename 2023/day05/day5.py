f = open("input.txt")

def isNumber(val):
  if(ord(val) >= 48 and ord(val) <= 57):
    return True
  return False


s = open("input.txt").read().splitlines()

seeds = [int(numbs) for numbs in s[0].split()[1::]]
s = [value for value in s if value != ""]
s = s[2::]
s.append("end")

def getDestinationNum(mapNums, currNum):
  destinationNum =0
  rule = []
  for x in mapNums:
    destinationStart = x[0]
    sourceStart = x[1]
    range = x[2]
    if currNum >= sourceStart and currNum <= sourceStart + range:
      return x
  return -1

def getNewCategoryRanges(mapNums):
  for idx,x in enumerate(seeds):
    val = getDestinationNum(mapNums, x)
    if val == -1:
      seeds[idx] = x
    else:
      seeds[idx] = val[0] -val[1] + x

mapItems = []
for x in s:
  if not isNumber(x[0]):
    # print("End of category ")
    ranges = getNewCategoryRanges(mapItems)
    print("Seed vals are: ", seeds)
    mapItems = []
    continue
  else:
    mapItems.append([int(num) for num in x.split()])

for x in seeds:
  print(x)

# My time and rank:
# 01:42:24  11847
print("Part1:", min(seeds))
