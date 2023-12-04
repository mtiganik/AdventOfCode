f = open("input.txt")

sum = 0
for x in f:
  x = " ".join(x.split())
  x = x.split(": ")[1]
  # winNumbs = 
  winNumbs = [int(char) for char in x.split(" | ")[0].split(" ")]
  allNumbs = [int(char) for char in x.split(" | ")[1].split(" ")]

  winCnt = 0  
  currSum = 0
  for y in allNumbs:
    if y in winNumbs:
      winCnt += 1
  if(winCnt > 0):
    currSum += 2 ** (winCnt - 1)
  sum += currSum

# My time and rank:
# 00:41:04  12072
print(sum)