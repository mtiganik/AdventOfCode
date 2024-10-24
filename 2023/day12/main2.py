import itertools
f = open("input.txt").read().splitlines()

def make_tt_ins(n):
   if n == 0:
      return []
   elif n == 1:
      return [False, True]
   else:
      prev_set = make_tt_ins(n - 1)
      full_set = cross_multiply(prev_set, [False, True])
      return full_set

def cross_multiply(s1, s2):
   rtn_set = []
   for i in range(len(s1)):
      for j in range(len(s2)):
         if type(s1[i]) == bool:
            nxt = [s1[i], s2[j]]
            rtn_set.append(nxt)
         else:
            nxt = []
            for x in range(len(s1[i])):
               nxt.append(s1[i][x])
               nxt.append(s2[j])
            rtn_set.append(nxt)
   return rtn_set

def isValidExpression(path, rule):
    if path.count("#") != sum(rule):
        return False
    for i in rule:
       subString = '#'*i
       while True:
            if path.startswith('.'):
                path = path[1:]
            elif path.startswith(subString):
                if len(path) > len(subString):
                    if path[len(subString)] == "#": return False
                path = path[len(subString):]
                break
            else: return False
    if '#' in path: return False
    return True
        
          
def generateExpressions(string, list, rule):
    expr = []
    validCnt = 0
    for x in list:
        val = ""
        qCnt = 0
        for i in range(len(string)):
            if string[i] != '?':
                val = val + string[i]
            else:
               bool = x[qCnt]
               qCnt += 1
               if bool == True: charToAdd = '#'
               else: charToAdd ='.'
               val = val + charToAdd
        isValid = isValidExpression(val, rule)
        print(val)
        if isValid:
            print(val, " - ", isValid)
            validCnt += 1
        # expr.append(val)
    return validCnt

              
def makeTrueFalseTable(n):
    l = [False, True]
    return [list(i) for i in itertools.product(l, repeat=n)]  

cnt = 0
for x in f:
    x = x.split()
    string = x[0]
    list = makeTrueFalseTable(string.count('?'))
    cons = [int(var) for var in x[1].split(',')]
    valids = generateExpressions(string, list, cons)
    print("Valids for ", string, ", ", valids, ", rule,", cons)
    cnt += valids

print(cnt)
