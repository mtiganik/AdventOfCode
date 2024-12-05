
rules = []
pages = []
isInRules = True
for x in open("input.txt"):
  if x.strip() == "": 
    isInRules = False
    continue
  if isInRules:
    data = x.split("|") 
    rules.append((int(data[0]), int(data[1])))
  else:
    data = x.split(",")
    pages.append([int(k) for k in data])


def findIfCorrect(book):
  for r in rules:
    if r[0] in book and r[1] in book:
      if book.index(r[0]) > book.index(r[1]):
        return 0
  return book[int((len(book) -1)/2)]


sum = 0
for p in pages:
  sum += findIfCorrect(p)

print(sum)
