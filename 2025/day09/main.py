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
print(col[0][0])