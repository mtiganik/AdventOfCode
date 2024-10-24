import itertools
f = open("input.txt").read().splitlines()

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
        if isValid:
            validCnt += 1
    return validCnt

              
def makeTrueFalseTable(n):
    l = [False, True]
    return [list(i) for i in itertools.product(l, repeat=n)]  

cnt = 0
for x in f:
    x = x.split()
    string = x[0]
    trueFalsetableLen = string.count('?')
    myList = makeTrueFalseTable(trueFalsetableLen)
    cons = [int(var) for var in x[1].split(',')]
    valids = generateExpressions(string, myList, cons)
    cnt += valids

# My time and rank
print("Part 1", cnt) # 09:56:01   18568