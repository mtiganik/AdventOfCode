
def analyziseInput(inp):
  if inp[len(inp)-1] < inp[0]:
    inp = list(reversed(inp))
  for i in range(len(inp)-1):
    if inp[i+1] <= inp[i] or inp[i+1] - inp[i] > 3:
      firstRemoved = inp[1:]
      lastRemoved = inp[:-1]
      iRemoved = inp[:i] + inp[i+1:]
      ip1Removed = inp[:i+1] + inp[i+2:]
      if awr(firstRemoved) or awr(lastRemoved) or awr(iRemoved) or awr(ip1Removed):
        return 1
      else: return 0
  return 1

def awr(inp):
  for i in range(len(inp)-1):
    if inp[i+1] <= inp[i] or inp[i+1] - inp[i] > 3:
      return 0
  return 1

sum = 0
for x in open("input.txt"):
  vals = x.strip().split()
  ints = [int(item) for item in vals]
  sum += analyziseInput(ints)

print(sum)