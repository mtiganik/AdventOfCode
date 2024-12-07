import math
import operator
import functools
import time

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
  n = len(inp) - 1  
  for k in range(2**n):
      result = inp[0]
      for i in range(n):
          if (k >> i) & 1:  
              result *= inp[i + 1] 
          else:
              result += inp[i + 1]  
      if result == expected:
          # print("Found: ", result)
          removals.append(idx)
          return result
  return 0

res = 0
for i,j in enumerate(data):

  res += findRes(j,i)

print("Part 1:", res)

print("removals: " , len(removals))
for i in reversed(removals):
  del data[i]

print(len(data))



end = time.time()
length = end - start

# Show the results : this can be altered however you like
print("It took", length, "seconds!")




