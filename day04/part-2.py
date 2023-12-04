f = open("input.txt")


thisDict = {
  "id" : 0,
  "copys": 0
}
list = []
list.append(thisDict)
sum = 0
for z in f:
  z = " ".join(z.split())
  gameId = int(z.split(":")[0].split(" ")[1])

  z = z.split(": ")[1]
  # winNumbs = 
  winNumbs = [int(char) for char in z.split(" | ")[0].split(" ")]
  allNumbs = [int(char) for char in z.split(" | ")[1].split(" ")]

  winCnt = 0  

  for y in allNumbs:
    if y in winNumbs:
      winCnt += 1
  if len(list) < gameId + 1:
    list.append({
      "id": gameId,
      "copys": 1
    })
  else:
    currCopies = list[gameId]["copys"]
    list[gameId] = {"id": gameId, "copys": currCopies +1}
  currCopies = list[gameId]["copys"]

  for x in range(gameId+1,gameId +1 + winCnt):
    if(len(list) < x +1):
      # list does not have this element, lets make it
      newElement = {
        "id": x,
        "copys": currCopies
      }
      list.append(newElement)
    else:
      currVal = list[x]["copys"]
      list[x] = {
        "id": x,
        "copys": currVal + currCopies
      }

sum = 0
for x in list:
  sum += x["copys"]

# My time and rank:
# 01:36:57  12756
print(sum)

