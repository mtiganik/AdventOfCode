f = open("input.txt").read().splitlines()
times = [int(numbs) for numbs in f[0].split()[1::]]
distance = [int(numbs) for numbs in f[1].split()[1::]]

sum = 1
for i in range(len(times)):
  time = times[i]
  dist = distance[i]
  validMethod = 0
  for pushTime in range(time):
    if pushTime*(time-pushTime) > dist:
      validMethod += 1
  print(i, ".race: ", validMethod)
  sum *= validMethod
print(sum)