f = open("input.txt")

def isNumber(char):
  if ord(char) >= 48 and ord(char)<= 57:
    return True
  return False

def isWrittenNumber(string):
  if string.startswith("one"): return 1
  if string.startswith("two"): return 2
  if string.startswith("three"): return 3
  if string.startswith("four"): return 4
  if string.startswith("five"): return 5
  if string.startswith("six"): return 6
  if string.startswith("seven"): return 7
  if string.startswith("eight"): return 8
  if string.startswith("nine"): return 9
  return -1

def isWrittenNumberReverse(string):
  if string.startswith("eno"): return 1
  if string.startswith("owt"): return 2
  if string.startswith("eerht"): return 3
  if string.startswith("ruof"): return 4
  if string.startswith("evif"): return 5
  if string.startswith("xis"): return 6
  if string.startswith("neves"): return 7
  if string.startswith("thgie"): return 8
  if string.startswith("enin"): return 9
  return -1

firstDigit = 0
secondDigit = 0

sum = 0
currentNum =0
for x in f:
  for i,c in enumerate(x):
    if isNumber(c):
      firstDigit = int(c)
      break
    if isWrittenNumber(x[i::]) != -1:
      firstDigit = isWrittenNumber(x[i::])
      break

  x = x[::-1]
  for i,c in enumerate(x):
    if isNumber(c):
      secondDigit = int(c)
      break
    if isWrittenNumberReverse(x[i::]) != -1:
      secondDigit = isWrittenNumberReverse(x[i::])
      break

  currentNum = 10*firstDigit + secondDigit
  print(currentNum)
  sum += currentNum
        

print("Part2:", sum)
# print("Part2:", sum(foods))

