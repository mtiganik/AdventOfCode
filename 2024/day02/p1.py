
def analyziseInput(inp):
  if inp[1] < inp[0]:
    inp = list(reversed(inp))
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