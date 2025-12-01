inp = "input.txt"

def p1(f):
    count,currNum = 0,50
    for x in open(f):
      pointer,newNum = x[0],int(x[1:])
      if pointer == "L":
        newNum *=-1
      currNum += newNum
      currNum %= 100
      if not currNum:
        count += 1
    return count

def p2(f):
    count,currNum = 0,50
    for x in open(f):
        pointer,newNum = x[0],int(x[1:])
        for i in range(newNum):
            if pointer == "L":
                currNum -= 1
            else:
                currNum += 1
            currNum %= 100
            if not currNum:
                count += 1
    return count


print("Part 1", p1(inp))
print("Part 2", p2(inp))