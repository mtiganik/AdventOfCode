f = open("input.txt")
p1 = 0
grid = []
for x in f:
  arr = list(x.strip())
  grid.append(arr)

start = grid[0].index("S")
dict = {}
for i in range(len(grid[0])):
  dict[i] = 0

dict[start] = 1
for i in range(2, len(grid),2):
  for j in range(len(grid[0])):
    if grid[i][j] == "^" and dict[j] != 0:
      for y in (j-1,j+1):
        dict[y] += dict[j]
      dict[j] = 0

sum = 0
for i,j in enumerate(dict):
  sum += dict[i]
print(sum)


