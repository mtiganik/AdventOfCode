


xArr, yArr = [],[]
total = 0
# store elements like this:
# [x1,x2,X] [y1,y2,Y]


def findAandB(x,y):
  divider = x[0]*y[1] - x[1]*y[0]
  Anom = x[2]*y[1] - x[1]*y[2]
  Bnom = x[0]*y[2] - x[2]*y[0]
  A = Anom / divider
  B = Bnom / divider
  print(A,B)
  if A.is_integer() and B.is_integer():
    return 3*int(A) + int(B)
  return 0
for k in open("input.txt"):
  if k.strip() == "": continue
  k = k.replace("=","+")
  f, k = k.split(": ")
  arr = k.split(", ")
  x = int(arr[0].split("+")[1])
  y = int(arr[1].split("+")[1])
  bnum = 10000000000000
  if "Prize" in f:
    # int(str(a) + str(b))
    xArr.append(10000000000000 + x)
    yArr.append(10000000000000 + y)
    total += findAandB(xArr,yArr)
    xArr, yArr = [],[]
  else:
    xArr.append(x)
    yArr.append(y)

  

print(total)