import sys
# from collections import defaultdict, deque
import collections

f = open("input.txt")
d = []
for x in f:
  x,y,z = x.split(",")
  d.append([int(x),int(y),int(z)])


dlist = []

for i in range(0, len(d)-1):
  for j in range(i+1,len(d)):
    dist = (d[i][0]-d[j][0])**2 + (d[i][1]-d[j][1])**2 + (d[i][2]-d[j][2])**2 
    dlist.append((dist,i,j))
dlist.sort()

nodes = set()
for _, i, j in dlist:
    nodes.add(i)
    nodes.add(j)
N = len(nodes)

# --- Union-Find ----
parent = {x: x for x in nodes}
rank = {x: 0 for x in nodes}

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False  # already merged
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

# --- Process edges in sorted order ---
components = N
lme = None

for dist, a, b in dlist:
    if union(a, b):
        components -= 1
        lme = (dist, a, b)
    if components == 1:
        break

p2 = d[lme[1]][0]*d[lme[2]][0]
print("LAST MERGE:", lme)
print(p2)

# print(p1Res)

