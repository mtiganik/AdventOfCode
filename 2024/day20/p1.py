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
def getLen():
    def checkElem(y,x,cc):
        global maxCnt
        global ex,ey
        if y == ey and x == ex:
            maxCnt = cc
            dg[y][x] = cc
            return cc
        if g[y][x] == ".":
            if dg[y][x] == "x":
                dg[y][x] = cc
                currElems.append([y,x])
        return 0
                
    # cg = copy.deepcopy(dg)
    currElems = [[y,x]]
    # g[yr][xr] = "."
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
        # if res != 0:
        #     g[yr][xr] = "#"
        #     return cc
        if len(currElems) == 0:
            return
            # raise Exception("!")

getLen()

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

def cheat(cy,cx):
    # cc = dg[cy][cx]
    u,r,d,l = dg[j-1][i],dg[j][i+1],dg[j+1][i],dg[j][i-1]
    maxVal = max([x for x in [u,r,d,l] if isinstance(x,int)])
    minVal = min([x for x in [u,r,d,l] if isinstance(x,int)])
    return maxVal - minVal -2

data = Counter()
for j in range(1,len(g)-1):
    for i in range(1,len(g[0])-1):
        if g[j][i] == "#":
            if checkNeedToRemove(j,i):
                nl = cheat(j,i)
                if nl >= 100:
                    data.update([nl])

# print(data)
print("p1",sum(data.values()))