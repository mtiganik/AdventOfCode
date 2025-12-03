def exec(inp,dx):
  r,id,inp = "",0,inp.rstrip()
  for n in range(dx,0,-1):
    ci = cm = 0
    for i in range(id, len(inp)):
      if int(inp[i]) > cm and len(inp[i:]) > n-1:
        cm, ci = int(inp[i]), i
    id,r = ci+1, r + str(cm)
  return int(r)

p1 = p2 = 0
for inp in open("input.txt"):
  p1,p2 = p1 + exec(inp,2), p2 + exec(inp,12)

print("Part1: ", p1)
print("Part2: ", p2)