import copy 
str0 = "0 1 10 99 999"
str1 = "125 17"
str2 = "92 0 286041 8034 34394 795 8 2051489"

stones = str2
stones = stones.split(" ")
stones = [ int(x) for x in stones ]


def ExecuteBlinksForThisDigit(num, n):
  cpyArr = [num]
  i = 0
  while i < n:
    workArr = cpyArr
    cpyArr = []
    for j,el in enumerate(workArr):
      if el == 0:
        cpyArr.append(1) 
      elif len(str(el)) % 2 == 0:
        tmp = str(el)
        hlnght = int(len(tmp)/2)
        n1 = tmp[:hlnght]
        n2 = tmp[hlnght:]
        cpyArr.append(int(n1))
        cpyArr.append(int(n2))
      else:
        cpyArr.append(el*2024)
    i += 1
  return len(cpyArr)

n = 25
sum = 0
for k in stones:
  #print("El: ", k)
  sum += ExecuteBlinksForThisDigit(k,n)
print(sum)