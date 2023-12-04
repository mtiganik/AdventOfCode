f = open("input.txt")

list = [0]
part1Sum = 0
part2Sum = 0
index = 0
for z in f:
  z = " ".join(z.split()).split(": ")[1]

  winNumbs = [int(char) for char in z.split(" | ")[0].split(" ")]
  allNumbs = [int(char) for char in z.split(" | ")[1].split(" ")]

  winCnt = 0  
  for y in allNumbs:
    if y in winNumbs:
      winCnt += 1

  # Part 1
  part1CurrSum = 0
  if(winCnt > 0):
    part1CurrSum += 2 ** (winCnt - 1)
  part1Sum += part1CurrSum


  # Part 2
  index += 1
  if len(list) < index + 1:
    list.append(1)
  else:
    list[index] += 1
  currCopies = list[index]

  for x in range(index+1,index +1 + winCnt):
    if(len(list) < x +1):
      list.append(currCopies)
    else:
      currVal = list[x]
      list[x] = currVal + currCopies
  part2Sum += list[index]


# My time and rank:
print(part1Sum) # 00:41:04  12072
print(part2Sum) # 01:36:57  12756


