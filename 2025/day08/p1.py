import sys
from collections import defaultdict, deque

f = open("input.txt")
d = []
for x in f:
  x,y,z = x.split(",")
  d.append([int(x),int(y),int(z)])

def build_connections(pairs):
    # Build adjacency list graph
    g = defaultdict(set)
    for a, b in pairs:
        g[a].add(b)
        g[b].add(a)

    seen = set()
    groups = []

    # Find connected components
    for node in g:
        if node not in seen:
            comp = []
            queue = deque([node])
            seen.add(node)

            while queue:
                x = queue.popleft()
                comp.append(x)
                for nxt in g[x]:
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)

            groups.append(sorted(comp))

    return groups

dlist = []

for i in range(0, len(d)-1):
  currDistList = []
  for j in range(i+1,len(d)):
    dist = (d[i][0]-d[j][0])**2 + (d[i][1]-d[j][1])**2 + (d[i][2]-d[j][2])**2 
    currDistList.append(dist)
  dlist.append(currDistList)

times = 1000
# print(dlist)
conList = []
for t in range(times):
  minDistance = sys.maxsize
  im = jm = 0
  for i in range(len(dlist)):
     for j in range(len(dlist[i])):
        if dlist[i][j] < minDistance and [i,i+j] not in conList:
           minDistance = dlist[i][j]
           im,jm = i,j+i
  conList.append([im,jm])
for k in conList:
   k[1] += 1
# print(conList)

con = build_connections(conList)
con.sort(key=len, reverse=True)
p1Res = len(con[0])*len(con[1])*len(con[2])
print(p1Res)

