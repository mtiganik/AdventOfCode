
val = ["." for _ in range(33)]
data = []
for i in range(33):
  data.append(["." for _ in range(33)])

for i in range(16):
  for j in range(0,16-i):
    if (i+j) %2 == 1:
      data[i][j] = "/"
for i in range(0,17):
  for j in range(17+i,33):
    if(i+j) %2 == 1:
      data[i][j] ="\\"
for i in range(17,33):
  for j in range(0,i-16):
    if(i+j) %2 == 1:
      data[i][j] = "\\"
for i in range(17,33):
  for j in range(33+16-i,33):
    if(i+j) %2 == 1:
      data[i][j] = "/"
data[2][4] = "#"
data[5][31] = "#"
data[10][10] = "#"
data[15][10] = "#"
data[28][4] = "#"
data[27][26] = "#"

for i in range(0,33):
  for j in range(0,33):
    if data[i][j] == "#":
      if i+j < 16:
        print("In left up",i , " ", j)
      # elif j<17 and i> 17 and 16-i+j
# for x in data:
#   print("".join(x))
