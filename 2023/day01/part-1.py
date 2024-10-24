f = open("input.txt")

def isNumber(char):
  if ord(char) >= 48 and ord(char)<= 57:
    return True
  return False

firstDigit = 0
secondDigit = 0

sum = 0
currentNum =0
for x in f:
  for i in x:
    if isNumber(i):
      firstDigit = int(i)
      break
  x = x[::-1]
  for i in x:
    if isNumber(i):
      secondDigit = int(i)
      break
  
  currentNum = 10*firstDigit + secondDigit
  print(currentNum)
  sum += currentNum
        
# My time and rank:
# 00:16:21  7251
print("Part1:", sum)


