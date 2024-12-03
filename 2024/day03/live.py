import re

# total = 0
# for x in open("input.txt"):
#   res = re.findall("mul\((\d+),(\d+)\)", x)
#   for vals in res:
#     total += int(vals[0])*int(vals[1])

def findMuls(str):
    res = re.findall("mul\((\d+),(\d+)\)", str)
    total = 0
    for vals in res:
      total += int(vals[0])*int(vals[1])
    return total


s = ""
for x in open("input.txt"):
  s = s + x
# st = "abc"
# st.find("g") # returns -1

total = 0
while True:
  if s.find("don't()") == -1:
     total += findMuls(s)
     break
  substr = s[:s.find("don't()")]
  total += findMuls(substr)
  s = s[s.find("don't()"):]
  s = s[s.find("do()"):]

print(total)