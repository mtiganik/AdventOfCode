from collections import Counter


def mix(given, currSecret):
    return given ^ currSecret
def prune(currSecret):
    return currSecret % 16777216


def secret2kStep(n):
    secret = n
    given = secret*64
    secret = mix(given, secret)
    secret = prune(secret)
    given = int(secret /32)
    secret = mix(given, secret)
    secret = prune(secret)
    given = secret*2048
    secret = mix(given,secret)
    secret = prune(secret)
    return secret

p1Res = 0
p2ResCnt = Counter()
cnt = 0
for k in open("input.txt"):
    val = int(k.strip())
    cCnt = Counter()
    patVals = ["", "", "", "", ""]
    prevDigit = val % 10
    nValsSet = False
    for j in range(2000):
        val = secret2kStep(val)
        lastDigit =   val % 10
        digitToAdd = lastDigit - prevDigit  
        patVals = [digitToAdd] +patVals[:4]
        if not nValsSet:
            if all(isinstance(x,int) for x in patVals):
                nValsSet = True
        if nValsSet:
            cSeq = str(patVals[3])+","+str(patVals[2])+","+str(patVals[1])+","+str(patVals[0])
            if cSeq not in cCnt:
                cCnt.update({cSeq:lastDigit})
            
        prevDigit = lastDigit
    p1Res += val
    p2ResCnt.update(cCnt)
    if cnt % 400 == 0:
        print("Working:",cnt)
    cnt += 1

maxKey = max(p2ResCnt, key=p2ResCnt.get)
p2Res  = p2ResCnt[maxKey]

print("P1:", p1Res)
print("P2", p2Res)
