
def countLetters(x):
  searched = []
  doubleCnt = 0
  tripleCnt = 0
  for y in x:
    if y in searched: 
      continue
    searched.append(y)
    cnt = x.count(y)
    if cnt == 2: doubleCnt +=1
    if cnt == 3: tripleCnt +=1
  return [doubleCnt, tripleCnt]

double, triple = 0,0 
for x in open("day02/input.txt"):
  c1,c2 = countLetters(x)
  double += 1 if c1 > 0 else 0
  triple += 1 if c2 > 0 else 0

sum = double * triple
print(sum)