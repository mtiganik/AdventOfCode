f = open("input.txt").read().splitlines()
f = list(map(list, zip(*f)))


for i,x in enumerate(f):
  for j,y in enumerate(x):
    if x[j] == 'O':
      jdx = j
      while True:
        if jdx == 0: break
        if x[jdx-1] != '.': break
        else:
          x[jdx] = '.'
          x[jdx-1] = 'O'
        jdx -= 1
for x in f:
  print("".join(x))
cnt = 0
for i,x in enumerate(f):
  for j in range(len(x)):
    if x[j] == 'O':
      cnt += len(x) -j

print(cnt)