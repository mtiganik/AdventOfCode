import time
start = time.time()


f = open("input.txt").read().splitlines()
# brics1, brics2,brics3 = [],[],[],[]
brics = []
for x in f:
  b = x.split("~")
  s,e = [int(x) for x in b[0].split(",")], [int(x) for x in b[1].split(",")]
  brics.append([s,e, True])

print("btw:", start - time.time())
start = time.time()

def sortBrics(currBrics):
  for i in range(len(currBrics)):
    for j in range(i,len(currBrics),1):
      # k = currBrics[2]
      if currBrics[j][0][2] < currBrics[i][0][2]:
        temp = currBrics[j]
        currBrics[j] = currBrics[i]
        currBrics[i] = temp
sortBrics(brics)


def allBricsInLevelToConsider(z,idx, our):
  iter = idx
  oys,oye,oxs,oxe = our[0][1], our[1][1],our[0][0],our[1][0],
  oV, oX, oY = False, False,False
  if oys-oys == 0 and oxs == oxe: ourVertical = True
  elif oxs-oxe != 0: oX = True
  elif oys-oye != 0: oY = True
  while True:

    iter -= 1
    if iter < 0: return True
    cb = brics[iter]
    if cb[0][2] > z: continue
    if cb[0][2] < max(z-9,1):
      # print("Move ", our, " downwards")
      return True

    cys,cye,cxs,cxe = cb[0][1], cb[1][1],cb[0][0],cb[1][0],
    # Horizontal Bric
    if cb[0][2] == cb[1][2]:
      if cb[0][2] != z: continue
      # Both aligned in y axis:
      if oys-oye != 0 and cys-cye != 0:
        if oxs==cxs:
          #They collide
          return False
      #Both aligned in x axis:
      elif oxs-oxe != 0 and cxs-cxe != 0:
        if oys == cys:
          return False
      # our aligned in x axis, curr in y axis:
      elif oxs-oxe == 0:
        if oxs in range(min(cxs,cxe), max(cxs,cxe)+1):
          return False
      elif oys-oye == 0:
        if oys in range(min(cys,cye), max(cys,cye)+1):
          return False
      else: raise ValueError("Shoulldnt get here")
    # Vertical considered bric:
    else:
      if oX:
        if cxs in range(min(oxs,oxe),max(oxs,oxe)+1) and oys == cys:
          return False
      elif oY:
        if cys in range(min(oys,oye),max(oys,oye)+1) and oxs == cxs:
          return False
      else: 
        if cys == oys and cxs == oys:
          return False

canMoveDown = True
while canMoveDown:
  canMoveDown = False
  for idx, bric in enumerate(brics):
    if bric[0][2] == 1: continue
    z = bric[0][2]
    currMoves = allBricsInLevelToConsider(z-1,idx, brics[idx])
    if currMoves:
      canMoveDown = True
      bric[0][2], bric[1][2] = z-1, bric[1][2]-1

print("iteration complete")
      
def bricksBelowCnt(our, curr):
  res = []
  resCnt = 0
  oys,oye,oxs,oxe = our[0][1], our[1][1],our[0][0],our[1][0],
  oV, oX, oY = False, False,False
  if oys-oys == 0 and oxs == oxe: ourVertical = True
  elif oxs-oxe != 0: oX = True
  elif oys-oye != 0: oY = True
  for c in curr:
    cys,cye,cxs,cxe = c[0][1], c[1][1],c[0][0],c[1][0]
    cV,cX,cY = False,False,False
    if cys-cye == 0 and cxs-cxe == 0:cV = True
    elif cys-cye != 0: oY = True
    elif cxs-cxe != 0: oX = True
    if oV:
      #If our is vertical then it can only have one brick beneath it 
      if oxs in range(min(cxs,cxe),max(cxs,cxe)+1) and oys in range(min(cys,cye), max(cys,cye)):
        return [1,c]
    elif cV:
      if cxs in range(min(oxs,oxe),max(oxs,oxe)+1) or cys in range((min(oys,oye), max(oys,oye)+1)):
        resCnt += 1
    elif oY and cY:
      if oxs == cxs:
        resCnt += 1
    elif oX and cX:
      if oys == cys:
        resCnt += 1
    elif oY:
      if cys in range(min(oys,oye), max(oys,oye)+1):
        resCnt += 1
    elif oX:
      if cxs in range(min(oxs,oxe), max(oxs,oxe)+1):
        resCnt += 1
  return resCnt
def getBricsByZIndex(zdx):
  res = []
  max(z-9,1)
  for i in range(0,len(brics)):
    ys,ye,xs,xe = brics[i][0][1], brics[i][1][1],brics[i][0][0],brics[i][1][0]
    if ys-ye == 0 and xs -xe == 0:
      if brics[i][1][2] >= zdx:
        res.append(brics[i])
    if brics[i][0][2] == zdx:
      res.append(brics[i])
    elif brics[i][0][2] > zdx:
      return res

sortBrics(brics)
cnt = 0
for zid in range(2, brics[-1][0][2]):
  belowBrics = getBricsByZIndex(zid-1)
  currBrics = getBricsByZIndex(zid)
  for bric in currBrics:
    res = bricksBelowCnt(bric,belowBrics)
    if isinstance(res, int): 
      if res == 0: raise ValueError("Should be more than zero")
      continue
    else:
      cantRemove = res[1]
      for x in belowBrics:
        if x[0] == cantRemove[0] and x[1] == cantRemove[1]:
          x[2] = False
  for x in belowBrics:
    if x[2] == True:
      cnt += 1
print("Part1:", cnt )
start = time.time()
