f = open("input.txt")

currentSum = 0
# max = 0
foods = []
for x in f:
  if(x == '\n'):
    foods.append(currentSum)

    currentSum = 0
  else: 
    currentSum += int(x)
foods.sort(reverse = True)
foods = foods[:3]
print("Part1:", foods[0])
print("Part2:", sum(foods))

