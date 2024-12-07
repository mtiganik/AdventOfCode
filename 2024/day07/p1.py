import math
import operator
import functools

import time

# Calculate the start time
start = time.time()


data = []

for x in open("input.txt"):
  k = x.strip().split(":")
  res = int(k[0])
  nums = [int(j) for j in k[1].strip().split(" ")]
  data.append([res, nums])

def getRes(d):
  inp = d[1]
  expectedRes = d[0]
  n = len(inp) - 1  # Number of bits required
  
  # currSum = 0
  # for k in range(2**n):
  #     operators = ['*' if (k >> i) & 1 else '+' for i in range(n)]  # Generate operators list
  #     strRes = str(inp[0])
      
  #     for i,op in enumerate(operators):
  #         strRes = strRes + op + str(inp[i+1])
  #     res = eval(strRes)
  #     if res == expectedRes:
  #        print("Found: ", expectedRes, " - ", strRes)
  #        return res
  # return 0

res = 0
for i,j in enumerate(data):
  if i%40 == 0:
     print(i)
  res += getRes(j)

print(res)



end = time.time()
length = end - start

# Show the results : this can be altered however you like
print("It took", length, "seconds!")


