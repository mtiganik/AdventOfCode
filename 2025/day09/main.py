from shapely.geometry import Polygon, box

dp = []
for k in open("input.txt"):
    x,y = k.strip().split(",")
    dp.append([int(x),int(y)])




col = []
for i in range(0,len(dp)-1):
    for j in range(i+1,len(dp)):
        x1,y1,x2,y2 = dp[i][0],dp[i][1],dp[j][0],dp[j][1]
        dist = (abs(x1-x2)+1)*(abs(y1-y2)+1)
        col.append((dist,[x1,y1],[x2,y2]))
col.sort(reverse=True)
print("Part 1: ", col[0][0])

p2 = 0
poly = Polygon(dp)
for i in range(len(dp)-1):
    for j in range(i, len(dp)):
        x1,y1,x2,y2 = dp[i][0],dp[i][1],dp[j][0],dp[j][1]
        minX,maxX,minY,maxY = min(x1,x2), max(x1,x2), min(y1,y2), max(y1,y2)
        subRect = box(minX,minY,maxX,maxY)
        if subRect.within(poly):
            dist = (abs(x1-x2)+1)*(abs(y1-y2)+1)
            if dist > p2:
                p2 = dist
print("Part 2: ", p2)