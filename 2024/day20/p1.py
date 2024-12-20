import copy
from collections import Counter

g = []
x,y,ex,ey = 0,0,0,0
cnt = 0
for k in open("input.txt"):
    arr = list(k.strip())
    g.append(arr)
    if "S" in k:
        y = cnt
        x = k.find("S")
        g[y][x] = "."
    if "E" in k:
        ey = cnt
        ex = k.find("E")
        g[ey][ex] = "."
    cnt += 1
dg = [["x" for k in range(len(g[0]))] for i in range(len(g))]
dg[y][x] = 0

maxCnt = 1
def getLen(yr,xr):
    global maxCnt
    def checkElem(y,x,cc):
        global ex,ey
        if y == ey and x == ex:
            return cc
        if g[y][x] == ".":
            if cg[y][x] == "x":
                cg[y][x] = cnt
                currElems.append([y,x])
        return 0
                
    cg = copy.deepcopy(dg)
    currElems = [[y,x]]
    g[yr][xr] = "."
    res = 0
    cc = 0
    while True:
        cpyElms = currElems
        currElems = []
        cc += 1
        for el in cpyElms:
            cy,cx = el[0],el[1]
            res += checkElem(cy-1,cx  ,cc)
            res += checkElem(cy  ,cx+1,cc)
            res += checkElem(cy+1,cx  ,cc)
            res += checkElem(cy  ,cx-1,cc)
        if res != 0:
            g[yr][xr] = "#"
            return cc
        if len(currElems) == 0:
            raise Exception("!")

ncl = getLen(0,0)

def checkNeedToRemove(j,i):
    u,r,d,l = g[j-1][i],g[j][i+1],g[j+1][i],g[j][i-1]
    ul,ur,dr,dl = g[j-1][i-1],g[j-1][i+1],g[j+1][i+1],g[j+1][i-1]
    diagCnt = [ul,ur,dr,dl].count("#")
    straigCnt = [u,r,d,l].count("#")
    if straigCnt <= 1: return 0
    if straigCnt >= 3: return 0
    upwall = [u,d].count("#")
    horwall = [l,r].count("#")
    if upwall and horwall: return 0

    return 1

data = Counter()
for j in range(1,len(g)-1):
    for i in range(1,len(g[0])-1):
        if g[j][i] == "#":
            if checkNeedToRemove(j,i):
                nl = getLen(j,i)
                if nl +100 <= ncl:
                    data.update([ncl-nl])
                    # print("Cheat " ,i,j, "saves", ncl-nl)
    print("Row", j)

print(data)
print("p1",sum(data.values()))