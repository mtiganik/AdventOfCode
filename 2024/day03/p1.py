import re

total = 0
vals = []
for x in open("input.txt"):
  res = re.findall("mul\((\d+),(\d+)\)", x)
  for item in res:
    total += int(item[0])*int(item[1])

print(total)  



