
a1 = (11,7)
a2 = (101,103)

ca = a2
xlen,ylen = 101,103
# middleX, middleY = ca[0]//2,ca[1]//2
# print(middleX,middleY)
# secs = 100
arr = []
for k in open("input.txt"):
  arr1 = k.strip().split(" v=")
  initials = arr1[0].replace("p=","").split(",")
  xstart,ystart = int(initials[0]),int(initials[1])
  velocities = arr1[1].split(",")
  xvel,yvel = int(velocities[0]), int(velocities[1])
  # xe = (xstart + (secs*xvel)%ca[0])%ca[0]
  # ye = (ystart + (secs*yvel)%ca[1])%ca[1]
  arr.append([xstart,ystart,xvel,yvel])

sec = 0
def IncrementAndCheckIfSomethingIsOnSameSpot():
  for el in arr:
    el[0] = (el[0] + (el[2])%xlen)%xlen
    el[1] = (el[1] + (el[3])%ylen)%ylen
  for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
      el1,el2 = arr[i],arr[j]
      if el1[0] == el2[0] and el1[1] == el2[1]:
        return 0
  return 1

while True:
  sec += 1
  res = IncrementAndCheckIfSomethingIsOnSameSpot()
  if res == 1:
    print("after ", sec," secs:")
    for i in range(ca[1]):
      currStr = "."*ca[0]
      for el in arr:
        if el[1] == i:
          if el[0] == xlen: currStr = currStr[:xlen-1] + "*"
          else: currStr = currStr[:el[0]-1] + "*" + currStr[el[0]:] 
      print(currStr)
    print("")
  if sec > 11000:
    print("shouldnt get here")
    break



