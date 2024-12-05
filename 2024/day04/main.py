
d,p1,p2,dirs = [x.strip() for x in open("input.txt")],0,0, [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
def p1m(y,x,dy,dx): return 0 if y+3*dy > len(d)-1 or y+3*dy < 0 or x+3*dx > len(d)-1 or x+3*dx < 0 else 1 if d[y+dy][x+dx] == "M" and d[y+2*dy][x+2*dx] == "A" and d[y+3*dy][x+3*dx]=="S" else 0
def p2m(y,x): return 1 if all(any(x in dg for x in ["MS","SM"]) for dg in [d[y-1][x-1]+d[y+1][x+1],d[y-1][x+1]+d[y+1][x-1]]) else 0
p1 += sum(p1m(y,x,dx,dy) for y in range(len(d)) for x in range(len(d[0])) if d[y][x] == 'X' for dx,dy in dirs)
p2 += sum(p2m(y,x) for y in range(1,len(d)-1) for x in range(1, len(d[0])-1) if d[y][x] == 'A')

print("Part 1:", p1)
print("Part 2:", p2)
#https://youtu.be/BmNLq4ELuDI
