A = B = C = 0
program = []
with open("input.txt") as file: lines = file.readlines()
A = int(lines[0].split(":")[1].strip())
B = int(lines[1].split(":")[1].strip())
C = int(lines[2].split(":")[1].strip())
prg = lines[4].split(": ")[1]
pg = list(map(int, prg.split(",")))

outp = ""
pt = 0

def getCombo(operand):
  global A,B,C
  if operand < 4: return operand
  if operand == 4: return A
  if operand == 5: return B
  if operand == 6: return C
  else: raise Exception("Shouldnt be 7")
def calculateRes(instr, operand):
  global A,B,C,outp,pt
  if instr == 0:
    combo = getCombo(operand)
    res = A/(2**combo)
    A = int(res)
  elif instr == 1:
    res = B^operand
    B = res
  elif instr == 2:
    combo = getCombo(operand)
    B = combo%8
  elif instr == 3:
    if A !=0:
      pt = operand -2
  elif instr == 4:
    res = B^C
    B = res
  elif instr == 5:
    res = getCombo(operand) % 8
    outp = outp + "," + str(res)
  elif instr == 6:
    combo = getCombo(operand)
    res = A/(2**combo)
    B = int(res)
  elif instr == 7:
    combo = getCombo(operand)
    res = A/(2**combo)
    C = int(res)


print("hello")
while True:
  instr, operand = pg[pt], pg[pt+1]

  calculateRes(instr, operand)
  pt += 2
  if pt >= len(pg): break
print("out")
print(outp)