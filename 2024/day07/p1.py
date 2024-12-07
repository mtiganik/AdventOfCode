
def getRes(nums, bits):
  result = nums[0]
  for i,bit in enumerate(bits):
    if bit == "0":
      result += nums[i+1]
    else:
      result *= nums[i+1]
  return result

def calculate(expected, nums):
  n = len(nums)-1
  for k in range(2**n):
    bits = f"{k:0{n}b}"
    val = getRes(nums, bits)
    if val == expected:
      return val
  return 0

# 0 -> 00
# 1 -> 01
# 2 -> 10
# 3 -> 11

p1Res = 0
for x in open("input.txt"):
  k = x.strip().split(": ")
  res = int(k[0])
  nums = [int(j) for j in k[1].split(" ")]
  p1Res += calculate(res, nums)

print(p1Res)