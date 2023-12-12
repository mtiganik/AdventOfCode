from itertools import permutations


def getCnt(string, cons):
  max = max(cons)
  if '#'*max in string:
    r = 1
  return 0
  
def generateDotsMap(dots, elements):
  # Kõik elemendid nii taga kui saavad
  vals = [dots-len(elements)+1] + [1]*(len(elements)-1) + [0]
  val = '.'*vals[0]
  for i in range(len(elements)):
    val += '#'*elements[i] + '.'*vals[i+1]
  # val = '.'*(dots - len(elements)+1) + ".".join(['#'*val for val in elements])
  print(val, " lenght: ", len(val))

  # Esimene üks koht eespool
  val = '.'*(dots - len(elements))

def makeOutPutLikeThis(string, cons):
  lenght = len(string)
  sumOfCons = sum(cons)
  maxDots = lenght - sumOfCons
  if maxDots < len(cons):
    return 1
  print("max dots ", maxDots," elements: ", cons, "str len: ", len(string) )
  generateDotsMap(maxDots, cons)
  return 0

f = open("input.txt").read().splitlines()
cnt = 0


def listOfElementsSum(elements, target_sum):
  all_permutations = list(permutations(range(1, elements + 1), elements))
  valid_permutations = [p for p in all_permutations if sum(p) == target_sum]

  result = []
  for p in valid_permutations:
      result.extend(list(permutations(p)))

  return result

combinations = listOfElementsSum(3, 9)
for combination in combinations:
    print(list(combination))

# for x in f:
#   # print(x)
#   x = x.split()
#   string = x[0]
#   cons = [int(var) for var in x[1].split(',')]
#   cnt += makeOutPutLikeThis(string, cons)


# for x in cons:
#   print(x)

