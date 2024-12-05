
rules = []
books = []
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
    books.append([int(x) for x in data])


def findCorrectBooks(book):
  for rule in rules:
    if rule[0] in book and rule[1] in book:
      if book.index(rule[0]) > book.index(rule[1]):
        return 0
  return book[int((len(book)-1)/2)]

def swapNums(book):
  for rule in rules:
    if rule[0] in book and rule[1] in book:
      if book.index(rule[0]) > book.index(rule[1]):
        tmp = book[book.index(rule[0])]
        book[book.index(rule[0])] = book[book.index(rule[1])]
        book[book.index(rule[0])] = tmp
        return 0


total = 0
for book in books:
  if findCorrectBooks(book) == 0:
    while findCorrectBooks(book) == 0:
      swapNums(book)
      findCorrectBooks(book)
    total += findCorrectBooks(book)

print(total)

