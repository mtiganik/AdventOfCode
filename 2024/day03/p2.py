import re

def findMultiplications(x):
  res = re.findall("mul\((\d+),(\d+)\)", x)
  total = 0
  for item in res:
    total += int(item[0])*int(item[1])
  return total

s = ""
for x in open("input.txt"):
  s = s + x


total = 0
while True:
  if s.find("don't()") == -1:
    total += findMultiplications(s)
    break
  subStr = s[:s.find("don't()")]
  total += findMultiplications(subStr)
  s = s[s.find("don't()"):]
  s = s[s.find("do()"):]

print(total)