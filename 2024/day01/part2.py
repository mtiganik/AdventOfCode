
arr1, arr2 = [],[]
for x in open("input.txt"):
  num = x.split()
  arr1.append(num[0])
  arr2.append(num[1])

sum = 0
for i in range(len(arr1)):
  occurence = arr2.count(arr1[i])
  sum += int(arr1[i]) * occurence

print(sum)



