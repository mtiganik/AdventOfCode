data = []
x = 0
y = 0
iter = 0
for k in open("input.txt"):
  k = '*' + k.strip() + '*'
  if '^' in k:
    y = iter
    x = k.find('^')
    k = k.replace("^",'x')
  data.append(list(k))
  iter += 1
data.insert(0,['*']*len(data[0]))
data.append(['*']*len(data[0]))
y = y+1
def manipulate(d):
  cnt = 0
  global x
  global y
  dy = -1 if d == 0 else 1 if d == 2 else 0
  dx = 1 if d == 1 else -1 if d == 3 else 0
  while True:
    if data[y+dy*cnt][x+ dx*cnt] == '#':
      y = y + dy*cnt - dy
      x = x + dx*cnt - dx
      return
    if data[y+dy*cnt][x+ dx*cnt] == '*':
      y = y + dy*cnt
      x = x + dx*cnt
      return
    data[y+dy*cnt][x+ dx*cnt] = 'x'
    cnt += 1


dir = 0
while True:
  manipulate(dir%4)
  dir += 1
  if(data[y][x] == "*"): break

sum = 0
for k in data:
  # print("".join(k))
  sum += k.count("x")
print(sum)

