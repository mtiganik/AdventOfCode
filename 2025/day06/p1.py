f = open("input.txt")
cnt = 0
data = []
ops = []
for x in f:
  line = ' '.join(x.split())
  line = line.split(" ")
  dataToAdd = []
  if line[0] not in ["+", "*"]:
    for k in line:
      k = k.strip()
      dataToAdd.append(int(k))
    data.append(dataToAdd)
  else:
    ops.append(line)
  
opCnt = len(data)
for i in range(0, len(data[0])):
  operator = ops[0][i]
  curRes = 0 if operator == "+" else 1
  for j in range(0,opCnt):
    if operator == "+":
      curRes += data[j][i]
    else:
      curRes *= data[j][i]
  cnt += curRes

print(cnt)
  