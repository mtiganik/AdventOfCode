
def findVal(nums, bits):
  result = nums[0]
  for i in range(len(bits)):
    if bits[i] == "0":
      result += nums[i+1]
    else:
      result *= nums[i+1]
  return result

def calculate(nums, expected):
  n = len(nums) -1

  for k in range(2**n):
    bits = f"{k:0{n}b}"
    res = findVal(nums, bits)
    if res == expected:
      return res
  return 0

# 0 00
# 1 01
# 2 10
# 3 11

res = 0
for x in open("input.txt"):
  k = x.strip().split(": ")
  expected = int(k[0])
  nums = [int(j) for j in k[1].strip().split(" ")]
  res += calculate(nums, expected)
  #print(expected, "|" , nums)

print(res)