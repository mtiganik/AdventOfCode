
currx,curry = [],[]
total = 0

def calcResult(x,y):
  A = (x[2]*y[1]-x[1]*y[2])/(x[0]*y[1]-x[1]*y[0])
  B = (x[0]*y[2]-x[2]*y[0])/(x[0]*y[1]-x[1]*y[0])
  if A.is_integer() and B.is_integer():
    return 3*int(A) + int(B)
  else:
    return 0
  print(A,B)
for k in open("input.txt"):
  if k.strip() == "":continue
  k = k.replace("=","+")
  f,k = k.split(": ")
  arr = k.split(", ")
  x = int(arr[0].split("+")[1])
  y = int(arr[1].split("+")[1])
  currx.append(x)
  curry.append(y)
  if("Prize" in f):
    total += calcResult(currx,curry)
    currx,curry = [],[]

print(total)