
xlen,ylen = 101,103

c1,c2,c3,c4 = 0,0,0,0
arr = []
for k in open("input.txt"):
  arr1 = k.strip().split(" v=")
  initials = arr1[0].replace("p=","").split(",")
  xstart,ystart = int(initials[0]),int(initials[1])
  velocities = arr1[1].split(",")
  xvel,yvel = int(velocities[0]), int(velocities[1])
  xe = (xstart + 100*xvel)%xlen
  ye = (ystart + 100*yvel)%ylen
  arr.append([xstart,ystart,xvel,yvel])
  if xe == xlen//2 or ye == ylen//2: continue
  else:
    if   ye < ylen//2 and xe < xlen//2: c1 += 1
    elif ye < ylen//2 and xe > xlen//2: c2 += 1
    elif ye > ylen//2 and xe > xlen//2: c3 += 1
    elif ye > ylen//2 and xe < xlen//2: c4 += 1

print("Part 1:", c1*c2*c3*c4)

sec = 0
def IncrementAndCheckIfSomethingIsOnSameSpot():
  for el in arr:
    el[0] = (el[0] + el[2])%xlen
    el[1] = (el[1] + el[3])%ylen
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
    print("Part 2:", sec)
    break

# https://youtu.be/hlcb8FnBKb0



