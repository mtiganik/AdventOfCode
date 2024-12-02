
def analyze(inp):
  if inp[0] > inp[len(inp)-1]:
    inp = list(reversed(inp))
  
  for i in range(len(inp)-1):
    if inp[i] >= inp[i+1] or inp[i+1] - inp[i] > 3:
      lastRemoved = inp[:-1]
      firstRemoved = inp[1:]
      ithRemoved = inp[:i] + inp[i+1:]
      iplus1Removed = inp[:i+1] +inp[i+2:]
      if awr(lastRemoved) or awr(firstRemoved) or awr(ithRemoved) or awr(iplus1Removed):
        return 1
      return 0
  return 1

def awr(inp):
  for i in range(len(inp)-1):
    if inp[i] >= inp[i+1] or inp[i+1] - inp[i] > 3:
      return 0
  return 1


sum = 0
for x in open("input.txt"):
  var = x.strip().split()
  ints = [int(val) for val in var]
  sum += analyze(ints)

print(sum)