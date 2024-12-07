import math
import operator
import functools
import time
import copy
# Calculate the start time
start = time.time()


data = []
removals = []
for x in open("input.txt"):
  k = x.strip().split(":")
  res = int(k[0])
  nums = [int(j) for j in k[1].strip().split(" ")]
  data.append([res, nums])


def findRes(arr,idx):
  
  inp,expected = arr[1], arr[0]

  if sum(inp) == expected and idx == -1:
     return expected
  n = len(inp) - 1  
  for k in range(2**n):
      result = inp[0]
      for i in range(n):
          if (k >> i) & 1:  
              result *= inp[i + 1] 
          else:
              result += inp[i + 1]  
      if result == expected and idx != -1:
          removals.append(idx)
          return result
  return 0

res = 0
for i,j in enumerate(data):
  res += findRes(j,i)

print("Part 1:", res)

for i in reversed(removals):
  del data[i]
p2Res = res

def combine_elements(input, bits):
  inp = copy.deepcopy(input)
  c = []
  c.append(inp[0])
  del inp[0]
  while bits != "":
    if bits[0]=="1":
       c[len(c)-1] = int(str(c[len(c)-1]) + str(inp[0]))
    else:
       c.append(inp[0])
    bits = bits[1:]
    del inp[0]
  return c



def getP2(arr):
  inp, expected = arr[1], arr[0]
  n = len(inp)-1
  for k in range(1,2**n):
    bits = f"{k:0{n}b}"
    combined = combine_elements(inp, bits)  
    if sum(combined) > expected: 
      # print(combined, " bigger")
      return 0

    res = findRes([expected,combined],-1)
    if res != 0:
      print("Found ", expected, " with ", combined)
      return res
  return 0   

for k in data:
   p2Res += getP2(k)

print("Part2: ", p2Res)

end = time.time()
length = end - start

# Show the results : this can be altered however you like
print("It took", length, "seconds!")



