
a1 = (11,7)
a2 = (101,103)

ca = a2

middleX, middleY = ca[0]//2,ca[1]//2
# print(middleX,middleY)
secs = 100
arr = []
c1,c2,c3,c4 = 0,0,0,0
for k in open("input.txt"):
  arr1 = k.strip().split(" v=")
  initials = arr1[0].replace("p=","").split(",")
  xstart,ystart = int(initials[0]),int(initials[1])
  velocities = arr1[1].split(",")
  xvel,yvel = int(velocities[0]), int(velocities[1])
  xe = (xstart + (secs*xvel)%ca[0])%ca[0]
  ye = (ystart + (secs*yvel)%ca[1])%ca[1]
  if xe == middleX or ye == middleY: continue
  else:
    if  xe < middleX and ye < middleY: c1 += 1
    elif ye < middleY and xe > middleX: c2 += 1
    elif ye > middleY and xe > middleX: c3 += 1
    elif ye > middleY and xe < middleX: c4 += 1
    else:
      raise Exception("shouldnt get here")

print(c1*c2*c3*c4)