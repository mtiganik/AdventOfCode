from functools import cmp_to_key
f = open("input.txt")

labels = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]

items = []
for x in f:
  cards = x.split()[0]
  bid = int(x.split()[1])
  items.append([cards,bid])

def isFiveOfKind(string):
  first = string[0]
  if string.count(first) == 5:
    return True

def isFourOfKind(string):
  first = string[0]
  second = string[1]
  if string.count(first) == 4 or string.count(second) == 4:
    return True
  return False

def isFullHouse(string):
  if string.count(string[0]) == 3 and string.count(string[3]) == 2:
    return True
  return False
def isThreeOfAKind(string):
  if string.count(string[0]) == 3: return True
  return False
def isTwoPair(string):
  if string.count(string[0]) == 2 and string.count(string[2]) == 2:
    return True
  return False
def isOnePair(string):
  if string.count(string[0]) == 2:
    return True

def findType(string):
  if isFiveOfKind(string):
    return 10
  elif isFourOfKind(string):
    return 9
  elif isFullHouse(string):
    return 8
  elif isThreeOfAKind(string):
    return 7
  elif isTwoPair(string):
    return 6
  elif isOnePair(string):
    return 5
  return 0


def reorder_string(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        sorted_chars = sorted(char_counts, key=lambda x: char_counts[x], reverse=True)
        reordered_str = ''.join([char * char_counts[char] for char in sorted_chars])
    return reordered_str


def cust_sort(a,b):
  aType = findType(reorder_string(a[0]))
  bType = findType(reorder_string(b[0]))
  if(aType > bType):
    return 1
  elif (bType > aType): return -1

  for i in range(0,5):
    aIdx = labels.index(a[0][i])
    bIdx = labels.index(b[0][i])
    if(aIdx < bIdx):
      return 1
    elif (aIdx > bIdx): return -1

  return 0

cmp_items = cmp_to_key(cust_sort)
items.sort(key = cmp_items)

sum = 0
for idx,x in enumerate(items):
  print(x[0])
  sum += (idx+1)*x[1]
# My time and rank:
# 01:18:24   8647
print("Part1:", sum)


