f = open("input.txt").read().splitlines()

# Part 1
def get_part_one():
  times = [int(numbs) for numbs in f[0].split()[1::]]
  distances = [int(numbs) for numbs in f[1].split()[1::]]

  sum = 1
  for i in range(len(times)):
    time = times[i]
    dist = distances[i]
    validMethod = 0
    for pushTime in range(time):
      if pushTime*(time-pushTime) > dist:
        validMethod += 1
    sum *= validMethod
  return sum

#Part 2
def get_part_two():
  time = int(''.join(f[0].split()[1::]))
  distance =  int(''.join(f[1].split()[1::]))

  loverTime=0
  upperTime = 0
  currTime = 0
  while(True):
    currTime += 1
    if(currTime*(time-currTime) > distance):
      loverTime = currTime
      break
  currTime = time
  while(True):
    currTime -= 1
    if(currTime*(time-currTime) > distance):
      upperTime = currTime
      break
  return upperTime - loverTime +1

# My times were:
print("Part1:", get_part_one()) # 01:02:53  12831
print("Part2:" ,get_part_two()) # 01:18:10  12959
