
arr1, arr2 = [],[]
for x in open("input.txt"):
  num = x.split()
  arr1.append(int(num[0]))
  arr2.append(int(num[1]))

arr1.sort()
arr2.sort()
sum = 0
for i in range(len(arr1)):
  sum += abs(arr2[i] - arr1[i])
print(sum)

