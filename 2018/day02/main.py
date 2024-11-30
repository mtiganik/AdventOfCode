
def countLetters(x):
  s,d,t = [],0,0
  for y in x:
    if y in s: continue
    s.append(y)
    c = x.count(y)
    if c == 2: d = 1
    if c == 3: t = 1
  return [d, t]

def getp2():
  for i in range(len(data)):
    for j in range(i+1, len(data)):
      counter = 0
      for k in range(len(data[0])):
        if data[i][k] == data[j][k]: continue
        else: counter += 1
        if counter > 1:
          break
      if counter == 1:
        r = ""
        for k in range(len(data[0])):
          if data[i][k] == data[j][k]:
            r = r + data[i][k]
          else:
            r = r + data[i][k+1:]
            return r

p1d, p1t, data= 0,0, [] 
for x in open("input.txt"):
  c1,c2 = countLetters(x)
  data.append(x.strip())
  p1d += c1
  p1t += c2

print("part1: ", p1d * p1t)
print("part2: ", getp2())