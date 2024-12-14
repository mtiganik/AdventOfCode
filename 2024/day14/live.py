
# xlen,ylen = 11,7
xlen, ylen = 101,103
middlex,middley = xlen//2, ylen//2
# print(middlex,middley)
sec = 100
c1,c2,c3,c4 = 0,0,0,0
for k in open("input.txt"):
  arr = k.strip().split(" v=")
  arr[0] = arr[0].replace("p=", "")
  initials = arr[0].split(",")
  xs,ys = int(initials[0]),int(initials[1])
  velocities = arr[1].split(",")
  vx,vy = int(velocities[0]), int(velocities[1])
  xend = (xs + (vx*sec)%xlen)%xlen
  yend = (ys + (vy*sec)%ylen)%ylen
  if xend == middlex or yend == middley: continue
  if xend < middlex and yend < middley: c1 += 1
  elif xend > middlex and yend < middley: c2 += 1
  elif xend > middlex and yend > middley: c3 += 1
  elif xend < middlex and yend > middley: c4 += 1
  else:
    raise Exception("Shouldnt get here")

print(c1*c2*c3*c4)

