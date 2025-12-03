# f = open("input.txt")

count = 0
def findLargest(inp):
  firstDigit = 0
  fdi = 0
  for i in range(len(inp)-1):
    currval = int(inp[i])
    if currval > firstDigit:
      firstDigit = currval
      fdi = i
  secondDigit = 0
  for i in range(fdi +1, len(inp)):
    currval = int(inp[i])
    if currval > secondDigit:
      secondDigit = currval
  res = 10*firstDigit+secondDigit
  print("Result: ", res)
  return 10*firstDigit+secondDigit

    

for x in open("input.txt"):
  inp = x.replace("\n", "")
  count+= findLargest(inp)

print("Part1: ", count)