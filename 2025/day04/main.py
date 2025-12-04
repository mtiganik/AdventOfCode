f = open("input.txt")
grid = []
count = 0
for x in f:
  valToAdd = "." + x.strip() + "."
  grid.append(list(valToAdd))

firstLast = list("."*len(grid[0]))
grid.insert(0,firstLast)
grid.append(firstLast)

def isAccessable(i,j):
  nearbyRolls = 0
  places = [
    [i-1,j-1],[i-1,j],[i-1,j+1], 
    [i,j-1],[i,j+1],
    [i+1,j-1],[i+1,j],[i+1,j+1]]
  for k in places:
    if grid[k[0]][k[1]] in ["@","x"]:
      nearbyRolls += 1
  if nearbyRolls < 4:
    return True
  return False
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == "@":
      if isAccessable(i,j):
        # print(i, "-", j, " returned true")
        grid[i][j] = "x"
        count += 1
# for k in grid:
#   print("".join(k))
print(count)



#............
#...xx.xx@x.. ..xx.xx@x.
#.x@@.x.@.@@. x@@.@.@.@@
#.@@@@@.x.@@. @@@@@.x.@@
#.@.@@@@..@.. @.@@@@..@.
#.@@.@@@@.@x. x@.@@@@.@x
#..@@@@@@@.@. .@@@@@@@.@
#..@.@.@.@@@. .@.@.@.@@@
#.x.@@@.@@@@. x.@@@.@@@@
#..@@@@@@@@.. .@@@@@@@@.
#.x.x.@@@.x.. x.x.@@@.x. 
#............