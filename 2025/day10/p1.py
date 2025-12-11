f = open("input.txt")
btnWiring = []


def getRes(indicator, btns):
    cnt = 0
    ids = [[[0]*len(indicator)]]
    while True:
        cnt += 1
        iterPaths = []
        lastPaths = ids[len(ids)-1]
        for currPath in lastPaths:
            
            for cbtn in btns:
                wPath = currPath.copy()
                for btnNo in cbtn:
                    wPath[btnNo] = 0 if wPath[btnNo] == 1 else 1
                if wPath == indicator:
                    return cnt
                else: iterPaths.append(wPath)
        ids.append(iterPaths)

cnt = 0
for x in f:
    indicator, btnWiring = x.split("] ")
    indicator,btnWiring = indicator[1:],btnWiring.split(" {")[0]
    btnWiring = btnWiring.strip().split(" ")
    btns = []
    for k in btnWiring:
        res = []
        k = k.replace("(", "")
        k = k.replace(")","")

        k = k.split(",")
        for i in k:
            res.append(int(i))
        btns.append(res)
    indicatorRes = []
    for i in range(len(indicator)):
        indicatorRes.append(0 if indicator[i] == "." else 1)
    res = getRes(indicatorRes, btns)
    # print(res)
    cnt += res

print(cnt)