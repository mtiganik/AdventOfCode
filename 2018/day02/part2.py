data = []
for x in open("day02/input.txt"):
  data.append(x.strip())
def printRes():
  for i in range(len(data)):
    for j in range(i+1, len(data)):
      counter = 0
      for k in range(len(data[i])):
        if data[i][k] == data[j][k]: continue
        else: counter += 1
        if counter > 1:
          break
      if counter == 0:
        print(" shouldnt get here")
      if counter == 1:
        print("Found")
        print(data[i])
        print(data[j])
        return
printRes()

