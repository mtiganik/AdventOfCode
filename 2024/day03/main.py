import re

input = "input.txt"

def f(x): return sum(int(a)*int(b) for a,b in re.findall("mul\((\d+),(\d+)\)", x))
s=open(input).read()
p1,p2 = f(s),0
while "don't()" in s:
  ss = s.split("don't()",1)
  s, p2 = ss[1][ss[1].find("do()"):], p2 + f(ss[0])

print("Part 1: ",p1)
print("Part 2: ",p2 + f(s))

# https://youtu.be/NJ-WtNFrGnA