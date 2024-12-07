import time
import copy
from itertools import product

start = time.time()


data = []
removals = []
for x in open("input.txt"):
  k = x.strip().split(":")
  res = int(k[0])
  nums = [int(j) for j in k[1].strip().split(" ")]
  data.append([res, nums])




# def generate_truth_table(n):
#     """Generate all possible combinations in base 3 for n elements."""
#     return list(product(range(3), repeat=n))

# # Example usage:
# n = 3  # Number of elements
# truth_table = generate_truth_table(n)

# # Print the results
# for row in truth_table:
#     print(row)



def p1Function(arr,idx):
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
          removals.append(idx)
          return result
  return 0

def combine_elements(input, bits):
  # if bits == "121":
  #    print("")
  inp = copy.deepcopy(input)
  result = inp[0]
  del inp[0]
  while bits != "":
    if bits[0] == "0":
      result += inp[0]
    elif bits[0] == "1":
      result *= inp[0]
    else:
      result = int(str(result) + str(inp[0]))
    del inp[0]
    bits = bits[1:]
  return result
        
res = 0
for i,j in enumerate(data):
  res += p1Function(j,i)

print("Part 1:", res)

for i in reversed(removals):
  del data[i]
p2Res = res




def getP2(arr):
  inp, expected = arr[1], arr[0]
  n = len(inp)-1
  truthTable = list(product(range(3), repeat=n))
  del truthTable[0]
  # for row in truthTable:
  #    print(row)
  for b in truthTable:
    bits = ''.join(str(x) for x in b)
    res = combine_elements(inp, bits)  
    if res == expected: 
      print("Found: ", expected, " with ", bits)
      return res
  return 0   

for i,k in enumerate(data):
  if i%40 == 0:
    print(i)

  p2Res += getP2(k)

print("Part2: ", p2Res)

end = time.time()
length = end - start

# Show the results : this can be altered however you like
print("It took", length, "seconds!")



