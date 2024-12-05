input = "input.txt"

rules,books,ir,p1,p2  = [], [], True, 0,0
[rules.append(tuple(map(int, x.split("|")))) if (ir := ir if x.strip() else False) else (books.append([int(x) for x in x.split(",")]) if x.strip() else None)for x in open(input)]
def fc(b): return 0 if any(r[0] in b and r[1] in b and b.index(r[0]) > b.index(r[1]) for r in rules) else b[int((len(b)-1)/2)]
def sn(b):
  for rule in rules:
    if rule[0] in b and rule[1] in b and b.index(rule[0]) > b.index(rule[1]):
      b[b.index(rule[0])], b[b.index(rule[1])] = b[b.index(rule[1])], b[b.index(rule[0])]
      return 0
for b in books: p1 += (res := fc(b)); p2 += sum(fc(b) for _ in iter(lambda: fc(b) == 0 and not sn(b), False)) if res == 0 else 0

print("Part1: ", p1)
print("Part2: ", p2)

#https://youtu.be/70F8JCKwhsQ