import copy 
str0 = "125 17"
str1 = "48"
str2 = "92 0 286041 8034 34394 795 8 2051489"

stones = str0
stones = stones.split(" ")
stones = [ int(x) for x in stones ]


def getElementsforNumAfterKBlinks(num,k):
  cpyArr = [num]
  i = 0
  while i < k:
    workArr = cpyArr
    cpyArr = []
    for el in workArr:
      if el == 0:
        cpyArr.append(1) 
      elif len(str(el)) % 2 == 0:
        cpyArr.append(int(str(el)[:int(len(str(el))/2)]))
        cpyArr.append(int(str(el)[int(len(str(el))/2):]))
      else:
        cpyArr.append(el*2024)
    i += 1

  return cpyArr

def sortWithCount(arr):
    arr.sort()
    from itertools import groupby
    digit_generator = ((key, len(list(group))) for key, group in groupby(arr))
    return digit_generator


myNum = 3
# res = getElementsforNumAfter5Blinks(myNum)
# cache.append({"num":myNum, "blinks" : 5, "vals": res})
# print(res)
# MULTIPLIER = 5
# p2Iterations = 15
sum = 0
iterations = 2
cache = []

# get initial 5 element lengths
# currIteratorElements = []
# for stone in stones:
#   res = getElementsforNumAfterKBlinks(stone,5)
#   cache.append({"num":stone, "blinks" : 0, "vals": len(res)})
#   currIteratorElements = currIteratorElements + res

# stones = currIteratorElements
currIteratorElements = []
i = 1

ia15 = len(getElementsforNumAfterKBlinks(1,20))

ourNum = 1

nextIterElements = getElementsforNumAfterKBlinks(ourNum,5)
i = 0

for i in range(3):
  total = 0
  arrSorted = sortWithCount(nextIterElements)
  nextIterElements = []
  for el,cnt in arrSorted:
    match_entry = next((entry for entry in cache if entry["num"] == el and entry["blinks"] == i), None)
    if match_entry:
      total += match_entry["vals"]*cnt
    else:
      res = getElementsforNumAfterKBlinks(el,5)
      total += len(res)*cnt
      cache.append({"num":el, "blinks" : i, "vals": len(res)})
      nextIterElements = nextIterElements + res
  cache.append({"num": ourNum, "blinks": i+1, "vals": total})

print("")
# res = getElementsforNumAfterKBlinks(48,5)
# total1After10 += len(res)
# cache.append({"num":48, "blinks" : 0, "vals": len(res)})
# nextIterElements = nextIterElements + res


# res = getElementsforNumAfterKBlinks(2024,5)
# cache.append({"num":2024, "blinks" : 0, "vals": len(res)})
# total1After10 += len(res)
# nextIterElements = nextIterElements + res

# match_entry = next((entry for entry in cache if entry["num"] == 40 and entry["blinks"] == 0), None)
# if match_entry:
#   total1After10 += match_entry["vals"]

# match_entry = next((entry for entry in cache if entry["num"] == 48 and entry["blinks"] == 0), None)
# if match_entry:
#   total1After10 += match_entry["vals"]

# res = getElementsforNumAfterKBlinks(80,5)
# total1After10 += len(res)
# cache.append({"num":80, "blinks" : 0, "vals": len(res)})
# nextIterElements = nextIterElements + res

# res = getElementsforNumAfterKBlinks(96,5)
# total1After10 += len(res)
# cache.append({"num":95, "blinks" : 0, "vals": len(res)})
# nextIterElements = nextIterElements + res

# cache.append({"num":1, "blinks":1, "vals":total1After10})

for stone in stones:
  res = getElementsforNumAfterKBlinks(stone,5)
  currElSum = 0
  for el in res:
    if val := any(entry["num"] == el and entry["blinks"] == i-1 for entry in cache):
      currElSum += val["vals"]
    else:
      res = getElementsforNumAfterKBlinks(el,10)
      currElSum += len(res)
  if not any(entry["num"] == el and entry["blinks"] == i for entry in cache):
    cache.append({"num":stone, "blinks" : 1, "vals": currElSum})
  currIteratorElements = currIteratorElements + res

for i in range(iterations):
  for stone in stones:
    res = getElementsforNumAfterKBlinks(stone)
    # currBlinks = (i + 1) * 5
    if not any(entry["num"] == stone and entry["blinks"] == i for entry in cache):
      cache.append({"num":stone, "blinks" : i, "vals": len(res)})

print("")
print(cache)