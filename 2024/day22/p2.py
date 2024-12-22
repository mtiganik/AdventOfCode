from collections import Counter


def mix(given, currSecret):
    return given ^ currSecret
def prune(currSecret):
    return currSecret % 16777216


def secret2kStep(n):
    secret = n
    # step1
    given = secret*64
    secret = mix(given, secret)
    secret = prune(secret)

    # step2
    given = int(secret /32)
    secret = mix(given, secret)
    secret = prune(secret)

    #step3
    given = secret*2048
    secret = mix(given,secret)
    secret = prune(secret)
    return secret


# cc = Counter()
# myKey = "Hello"
# cc.update({myKey: 3})

# print("!")
# res = 0
# cnt = 0
# n1,n2,n3,n4,n5 = "","","","",""
cn = 123
cone = cn % 10
resCnt = Counter()
for k in open("input.txt"):
    val = int(k.strip())
    cCnt = Counter()
    # fVal = val % 10
    # val = secret2kStep(val)
    patVals = ["", "", "", "", ""]
    prevDigit = val % 10
    ldVals = [prevDigit, "", "", "", ""]
    nValsSet = False
    # subtct = 0
    for j in range(2000):
        # do some Calculations
        val = secret2kStep(val)
        lastDigit =   val % 10
        digitToAdd = lastDigit - prevDigit  
        patVals = [digitToAdd] +patVals[:4]
        ldVals = [lastDigit] + ldVals[:4]
        if not nValsSet:
            if all(isinstance(x,int) for x in patVals):
                nValsSet = True
        if nValsSet:
            # CSum = patVals[4]
            CSum = lastDigit
            cSeq = str(patVals[3])+","+str(patVals[2])+","+str(patVals[1])+","+str(patVals[0])
            # mstr = "Hello"
            # if cSeq == "-2,1,-1,3":
            #     print("debug")
            if cSeq not in cCnt:
                cCnt.update({cSeq:CSum})
            
        prevDigit = lastDigit
    resCnt.update(cCnt)

maxKey = max(resCnt, key=resCnt.get)
maxValue = resCnt[maxKey]
print(maxKey)
print(maxValue)
print("!!")


