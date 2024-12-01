a1, a2 = [],[]
for x in open("input.txt"):
  num = x.split()
  a1.append(int(num[0]))
  a2.append(int(num[1]))

a1.sort()
a2.sort()
p1sum, p2sum = 0, 0
for i in range(len(a1)):
  p1sum += abs(a2[i] - a1[i])
  occ = a2.count(a1[i])
  p2sum += a1[i] * occ

print("Part1: ", p1sum) # 16m19s @5913
print("Part2: ", p2sum) # 23m55s @5871

# Me solving it here:
# https://youtu.be/3iNDJ_hW-d4
