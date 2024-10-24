
def isNumber(val):
  if(ord(val) >= 48 and ord(val) <= 57):
    return True
  return False

def split_ranges(seed, rule, newSource):
    result = []
    
    # Find the starting point of the intersection
    start = max(seed.start, rule.start)
    
    # Find the ending point of the intersection
    end = min(seed.stop, rule.stop)
    
    # Case: Rule outside seed range
    if end <= start:
        result.append(seed)
    
    # Case: Rule coincides with the left side of the seed
    elif start == seed.start:
        result.append(range(start, end))
        result.append(range(end, seed.stop))
    
    # Case: Rule coincides with the right side of the seed
    elif end == seed.stop:
        result.append(range(seed.start, start))
        result.append(range(start, end))
    
    # Case: Rule is inside the seed range
    else:
        result.append(range(seed.start, start))
        result.append(range(start, end))
        result.append(range(end, seed.stop))
    
    return result


def getDestination(mapNums, currRange):
  newRanges = []
  for x in mapNums:
    ruleRange = range(x[1], x[1] + x[2])
    splitRange = split_ranges(currRange,ruleRange,x[0])
    if splitRange[0] != currRange:
      newRanges.append(splitRange)
  return newRanges



def getNewCategoryRanges(mapNums):
  for idx,x in enumerate(seeds):
    val = getDestination(mapNums, x)
    # if val == -1:
    #   seeds[idx] = x
    # else:
    #   seeds[idx] = val[0] -val[1] + x

s = open("input.txt").read().splitlines()

seedsStart = [int(numbs) for numbs in s[0].split()[1::]]
seeds = []
seed = 0


for idx,x in enumerate(seedsStart):
  if(idx%2 == 0): seed = x
  else: seeds.append(range(seed,seed+x))
s = [value for value in s if value != ""]
s = s[2::]
s.append("end")

mapItems = []
for x in s:
  if not isNumber(x[0]):
    ranges = getNewCategoryRanges(mapItems)
    print("Seed vals are: ", seeds)
    mapItems = []
    continue
  else:
    mapItems.append([int(num) for num in x.split()])

# TODO: Finish part 2
# print("Part2:", min(seeds))


