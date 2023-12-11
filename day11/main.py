f = open("input.txt").read().splitlines()
grid = []
for x in f:
  grid.append([*x])

# Vertical injection
for j in range(len(grid[0])-1,0,-1):
  needInjection = True
  for i in range(len(grid)):
    if grid[i][j] == '#':
      needInjection = False
  if needInjection:
    for i in range(len(grid)):
      val = grid[i]
      del val[j]
      val.insert(j,'*')
      del grid[i]
      grid.insert(i,val)


# Horisontal injection
Emptyhorizontal = ['*']*len(grid[0])
for ix in range(len(grid)-1,0,-1):
  if '#' not in grid[ix]:
    del grid[ix]
    grid.insert(ix, Emptyhorizontal)

starIndex = 0
starsList = []
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == "#":
      starIndex += 1
      starVal = [starIndex, i, j]
      starsList.append(starVal)

def getYEmptyRowCnts(id1, id2):
  cnt = 0
  for i in range(id1, id2, 1):
    if grid[i][0] == "*":
      cnt += 1
  return cnt

def getXEmptyRowCnts(id1,id2):
  cnt = 0
  for i in range(id1,id2,1):
    if grid[0][i] == "*":
      cnt += 1
  return cnt

def getDistance(star1, star2, Larger):
  emptyYRowCnt = getYEmptyRowCnts(min(star1[1], star2[1]), max(star1[1], star2[1]))
  emptyXRowCnt = getXEmptyRowCnts(min(star1[2], star2[2]), max(star1[2], star2[2]))
  ydist = abs(star1[1]-star2[1]) + emptyYRowCnt*(Larger-1)
  xdist = abs(star1[2]-star2[2]) + emptyXRowCnt*(Larger-1)
  return xdist + ydist

part1Sum = 0
part2Sum = 0
for i in range(len(starsList)-1):
  for j in range(i+1, len(starsList),1):
    part1Sum += getDistance(starsList[i], starsList[j],2)
    part2Sum += getDistance(starsList[i], starsList[j],1000000)

# My times and rank:
print("Part1: ", part1Sum) # 01:02:35   7196
print("Part2: ", part2Sum) # 01:45:23   7928

