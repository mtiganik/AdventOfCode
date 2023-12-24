f = open("input.txt").read().splitlines()

least = 200000000000000
most  = 400000000000000
def getHail(s): return [list(map(int,s.split("@")[0].split(","))), list(map(int, s.split("@")[1].split(",")))]

def findCollision(hail1, hail2):
  x1,y1,k1,vx1,vy1 =hail1[0][0],hail1[0][1], (hail1[1][1] / hail1[1][0]),hail1[1][0],hail1[1][1]
  x2,y2,k2, vx2,vy2 = hail2[0][0],hail2[0][1], (hail2[1][1] / hail2[1][0]), hail2[1][0],hail2[1][1]
  if k1 == k2:
    # print("parallel")
    return 0
  x = (k1*x1-k2*x2+y2-y1)/(k1-k2)
  y = k1*x-k1*x1 + y1
  y_ = k2*x-k2*x2 + y2
  t1 = (x-x1)/vx1
  t1_ = (y-y1)/vy1
  t2  = (x-x2)/vx2
  t2_ = (y-y2) / vy2
  if t1 <0 or t2 <0:
    return 0
  if x > least and x < most  and y > least and y < most:
    # print("paths will cross inside the test area")
    return 1
  else: 
    # print("paths will cross outside the test area")
    return 0
res = 0
for idx in range(len(f)-1):
  hail1 = getHail(f[idx])
  for jdx in range(idx+1, len(f)):
    res += findCollision(hail1, getHail(f[jdx]))

print("Part1: ", res)
