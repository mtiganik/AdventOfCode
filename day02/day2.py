
def getMaxCubeCounts(plays):
  maxRed = 0 
  maxGreen = 0 
  maxBlue = 0
  for play in plays:
    cubes = play.split(', ')
    for x in cubes:
      num = int(x.split(" ")[0])
      color = x.split(" ")[1]
      if color.startswith("blue") and maxBlue < num: maxBlue = num
      if color.startswith("red") and maxRed < num: maxRed = num
      if color.startswith("green") and maxGreen < num: maxGreen = num

  return maxBlue*maxRed*maxGreen


def isValidGame(str):
  cubes = str.split(', ')
  if len(cubes) > 3: print("Error, more than 3 numbers")
  for x in cubes:
    num = int(x.split(" ")[0])
    color = x.split(" ")[1]
    if color.startswith("blue") and num > maxblue: return False
    if color.startswith("red") and num > maxred: return False
    if color.startswith("green") and num > maxgreen: return False
  return True


# Entry
maxred = 12
maxgreen = 13
maxblue = 14

part1Sum = 0
part2Sum = 0

gameId = 0
games = []
validGame = True
f = open("input.txt")

for x in f:
  gameId = int(x.split(":")[0].split(" ")[1])
  games = x.split(": ")[1].split("; ")

  # Part 1 logic
  for y in games:
    if not isValidGame(y): validGame = False
  if validGame:
    part1Sum += gameId
  validGame = True

  # Part 2:
  part2Sum += getMaxCubeCounts(games)
  
print("Part1: ", part1Sum)
print("Part2: ", part2Sum)