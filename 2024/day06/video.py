x,y,data = 0,0,[]
iter = 0

for k in open("input.txt"):
  k = "*" + k.strip() + "*"
  if '^' in k:
    y = iter +1
    x = k.find("^")
    k = k.replace("^",".")
  data.append(list(k))
  iter += 1

data.insert(0,["*"]*len(data[0]))
data.append(["*"]*len(data[0]))

# modifies data, put some mark where guard has been to
# change x,y to new coordinates
def move(dir):
  global x
  global y
  cnt = 0
  dy = 1 if dir == 2 else -1 if dir == 0 else 0
  dx = 1 if dir == 1 else -1 if dir == 3 else 0
  while True:
    if data[y+ dy*cnt][x+dx*cnt] == "#":
      y = y+ dy*cnt -dy
      x = x+ dx*cnt -dx
      return
    if data[y+ dy*cnt][x+dx*cnt] == "*":
      y = y+ dy*cnt
      x = x+ dx*cnt
      return

    data[y+dy*cnt][x+dx*cnt] = "x"
    cnt += 1
  return
# 0: up
# 1: right
# 2: down
# 3: left
dir = 0
while True:
  move(dir % 4)
  dir += 1
  if data[y][x] == "*":
    break

sum = 0
for k in data:
  sum += k.count("x")
  print("".join(k))

print(sum)