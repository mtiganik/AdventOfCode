seq =[ ["7","8","9"]
      ,["4","5","6"]
      ,["1","2","3"]
      ,["x","0","A"]]

dir = [["x","^","A"], 
       ["<","v",">"]]


seqs = []
for k in open("input.txt"):
    seqs.append(k.strip())


def getRobot1Chars(seq):
    x,y  = 2,3
    def getDestCoords(c):
        j,i = 0,0
        j = 0 if c in ["7","8","9"] else 1 if c in ["4","5","6"] else 2 if c in ["1","2","3"] else 3
        i = 0 if c in ["7","4","1"] else 1 if c in ["8","5","2","0"] else 2
        return [j,i]

    currSeq = ""
    for k in seq:
        dy,dx = getDestCoords(k)
        while True:
            if y == dy and x == dx:
                currSeq = currSeq + "A"
                y,x = dy,dx
                break
            elif dy < y:
                y = y-1
                currSeq +=  "^"
            elif dy > y:
                y = y+1
                currSeq +=  "v"
            elif dx < x:
                x = x-1
                currSeq +=  "<"
            elif dx > x:
                x = x+1
                currSeq +=  ">"
            else:
                raise Exception("!")
    return currSeq
# <A^A^^>AvvvA

def getDestDirectional(c):
    x,y = 0,0
    y = 0 if c in ["^" ,"A" ] else 1
    x = 0 if c == "<" else 1 if c in ["^","v"] else 2
    return [y,x]
def getRobot2Chars(seq):
    x,y = 2,0
    currSeq = ""
    for k in seq:
        dy,dx = getDestDirectional(k)
        while True:
            if y == dy and x == dx:
                currSeq = currSeq + "A"
                y,x = dy,dx
                break
            elif dy < y:
                y = y-1
                currSeq +=  "^"
            elif dy > y:
                y = y+1
                currSeq +=  "v"
            elif dx < x:
                x = x-1
                currSeq +=  "<"
            elif dx > x:
                x = x+1
                currSeq +=  ">"
            else:
                raise Exception("!")
    return currSeq
finalSeqs = []
for seq in seqs:
    r1Seq = getRobot1Chars(seq)
    r2Seq = getRobot2Chars(r1Seq)
    r3Seq = getRobot2Chars(r2Seq)
    # r3Seq = getRobot2Chars(r3Seq)
    finalSeqs.append(r3Seq)
total = 0
for k in range(len(finalSeqs)):
    nis = seqs[k]
    nis = int(nis[:-1])
    finalStepsLen = len(finalSeqs[k])
    res = nis*finalStepsLen
    total += res
print(total)
print("!")     
# v<<A>>^A<A>AvA<^AA>A<vAAA>^A

# numeric keypad
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

# directional keybad
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+