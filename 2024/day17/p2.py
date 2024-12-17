A = B = C = 0
# program = []
# with open("input.txt") as file: lines = file.readlines()
A = 0
B = 0
C = 0
pg = [2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0]


outp = []
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
    outp.append(res)
  elif instr == 6:
    combo = getCombo(operand)
    res = A/(2**combo)
    B = int(res)
  elif instr == 7:
    combo = getCombo(operand)
    res = A/(2**combo)
    C = int(res)
elms = [
1000000,
1100000,
1200000,
1400000,
1600000,
1800000,
2000000,
2200000,
2400000,
2600000,
2800000,
3000000,
3200000,
3400000,
3600000,
3800000,
4000000,
4200000,
4400000,
4600000,
4800000,
5000000,
5200000,
5400000,
5600000,
5800000,
6000000,
6200000,
6400000,
6600000,
6800000,
7000000,
7200000,
7400000,
7600000,
7800000,
8000000,
8200000,
8400000,
8600000,
8800000,
9000000,
9200000,
9400000,
9600000,
9800000
]

# same len start and end:
# 36000000000000
# 280000000000090
#Same len end:

#Last digit same start/end:
# 176000000000000
# 211000000000000

#2nd last digit start/end
# 207000000000000
# 211000000000000

#3rd last digit start/end
# 207000000000000
# 211000000000000

# 4th last digit start/end:
# 207950000000000
# 208010000000000

# 5th last digit start/end:
# 207970950000000
# 207979450000000

# 6th last digit start/end:
# 207976300000000
# 207977320000000

# 7th last digit start/end:
# 207976680000000
# 207976810000000

# 8th last digit:
# 207976795500000
# 207976811700000

# 9th last digit:
# 207976801250000
# 207976801500000

# 10th last digit 5,4,5 end
# 207976801304580
# 207976801337340

# finding 7,5,4,5
# 207976801316870
# 207976801320950

# finding 2,7,4,5
m =   207976801316870
m = m+           3000

# 10th digit:
# 207976801250000
for k in range(m,m+200):
  A = k
  outp = []
  pt = 0
  while True:
    instr, operand = pg[pt], pg[pt+1]
    calculateRes(instr, operand)
    pt += 2
    if pt >= len(pg): break
  print("A:" , k," - ", outp)
  if len(outp) == len(pg):
    if outp == pg:
      print("found:", k)
      break
  # if k%10 == 0:
    # if len(outp) == len(pg):
    #   print("len same")