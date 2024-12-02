
def p2(inp):
  for i in range(len(inp)-1):
    if inp[i] >= inp[i+1] or inp[i+1]-inp[i] > 3:
      lr,fr,ir,ip1 = inp[:-1],inp[1:],inp[:i]+inp[i+1:],inp[:i+1]+inp[i+2:]
      if p1(lr) or p1(fr) or p1(ir) or p1(ip1): return 1
      return 0
  return 1

def p1(inp):
  for i in range(len(inp)-1):
    if inp[i] >= inp[i+1] or inp[i+1] - inp[i] > 3:return 0
  return 1


p1Sum, p2Sum = 0,0
for x in open("input.txt"):
  inp = [int(val) for val in x.strip().split()]
  if inp[0] > inp[len(inp)-1]: inp = list(reversed(inp))
  p1Sum += p1(inp)
  p2Sum += p2(inp)

print("Part 1: ", p1Sum) # 15min 20sec
print("Part 2: ", p2Sum) # 1h 10min

# Link to video
# https://youtu.be/u3WJc_EUI0Y