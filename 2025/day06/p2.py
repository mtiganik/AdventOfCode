f = open("input.txt")
cnt = 0
data = []
ops = []
for x in f:
  if x[0] in ["+","*"]:
    ops.append(x + " e")
  else:
    data.append(x.rstrip() + " e")
# if len(ops[0]) != len(data[0]):
#   raise Exception("!!!")

operator = ops[0][0]
nums = []
curRes = 0 if operator == "+" else 1

for i in range(0,len(data[0])):
  if ops[0][i+1] in ["+","*",'e']:
    for t in nums:
      curRes = t+curRes if operator == "+" else t*curRes
    cnt += curRes
    nums = []
    if ops[0][i+1] == "e": break
    operator = ops[0][i+1]
    i = i+1
    curRes = 0 if operator == "+" else 1
  else:
    currNum = ""
    for j in range(0,len(data)):
      if data[j][i] != " ":
        currNum += data[j][i]
    nums.append(int(currNum))

print(cnt)
  