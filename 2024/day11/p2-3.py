from collections import Counter,defaultdict

str0 = "0 1 10 99 999"
str1 = "125 17"
str2 = "92 0 286041 8034 34394 795 8 2051489"

stones = str2
stones = stones.split(" ")
stones = [ int(x) for x in stones ] 

def blink(c1: Counter):
  c2 = defaultdict(int)
  for stone, count in c1.items():
    if stone == 0:
      c2[1] += c1[0]
    elif len(str(stone)) % 2 == 0:
      s = str(stone)
      s1, s2 = int(s[:len(s) // 2]), int(s[len(s) // 2:])
      c2[s1] += c1[stone]
      c2[s2] += c1[stone]
    else:
      c2[stone*2024] += c1[stone]
  return c2

#Part 1
c = Counter(stones)
for _ in range(25):
  c = blink(c)
p1Sum = sum(c.values())
print("Sum")
print(p1Sum)

#Part 2
c = Counter(stones)
for _ in range(75):
  c = blink(c)
print("P2:", sum(c.values()))