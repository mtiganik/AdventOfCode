
data = []
three = []

for k in open("input.txt"):
    data.append(k.strip())

for i in range(len(data)-1):
    e1,e2 = data[i].split("-")
    for j in range(i+1,len(data)):
        el2 = data[j]
        if e1 in el2 and e2 in el2:
            print(data[i],data[j], "duplicates")


def GetThree(cel, favs):
    cur1, cur2 = cel.split("-")
    for k in range(len(favs)):
        el = favs[k]
        el1,el2 = el.split("-")
        e1tolook = el1 if el2 in cel else el2
        e2tolook = cur1 if cur1 not in el else cur2
        thirdEl = cur1 if cur1 in el else cur2
        if e1tolook[0] == "t" or e2tolook[0] == "t" or thirdEl[0] == "t":
            for i in range(len(favs)):
                cel = favs[i]
                if e1tolook in cel and e2tolook in cel:
                    res = [e1tolook,e2tolook,thirdEl]
                    res.sort()
                    resAString = res[0]+","+res[1]+","+res[2]
                    if resAString not in three:
                        three.append(resAString)
                        return

for j in range(len(data)):
    cel = data[j]
    # if cel == "td-yn":
    #     print("!")
    cur1, cur2 = cel.split("-")
    favs = []
    # favs.append(data[j])
    favs = []
    for i in range(0,len(data)):
        if i == j: continue
        if cur1 in data[i] or cur2 in data[i]:
            favs.append(data[i])
    
    GetThree(cel, favs)
three.sort()
print(len(three))
# for k in three:
#     print(k)


    