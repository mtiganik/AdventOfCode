currNum = 50
count = 0
pointer = ""
for x in open("input.txt"):
  pointer,newNum = x[0:1],int(x[1:])
  # if newNum >100:
  #   count += int(newNum/100)
  #   newNum %=100
  if pointer == "L":
    newNum *=-1
  
  currNum += newNum
  currNum %= 100
  if not currNum:
    count += 1
  print("Current num:", currNum)
  

print(count)