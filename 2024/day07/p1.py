import math
import operator
import functools

data = []

inp = [1, 2, 3, 4]
n = len(inp) - 1  # Number of bits required

def apply_operations(inp, operators):
    """Apply the operations to the input list based on the operators."""
    result = inp[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += inp[i + 1]
        elif op == '*':
            result *= inp[i + 1]
    return result

for k in range(2**n):
    operators = ['*' if (k >> i) & 1 else '+' for i in range(n)]  # Generate operators list
    result = str(inp[0])
    for i,op in enumerate(operators):
        result = result + op + str(inp[i+1])
    print(eval(result))



# for x in open("input.txt"):
#   k = x.strip().split(":")
#   res = int(k[0])
#   nums = [int(j) for j in k[1].strip().split(" ")]
#   data.append([res, nums])

# remInd = []
# print("Initial Len: ", len(data))
# def addUp(inp,i):
#   total,nums = inp[0], inp[1]
#   sums = sum(nums)
#   if sums > total:
#     remInd.append(i)
#     # print("remove: " , total)
#     return 0
#   if sums == total:
#     remInd.append(i)
#     # print("Sums total: " , total)
#     return total
#   return  0
  

# res = 0
# for j in range(len(data)):
#   res += addUp(data[j],j)

# print("removals: " , len(remInd))
# for i in reversed(remInd):
#   del data[i]

# print("New list: ", len(data))
# # for x in data:
# #   print(x)
# # print("P1: ", res)







# # def pFactors(n): 
# #         """Finds the prime factors of 'n'""" 
# #         from math import sqrt 
# #         pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n 
# #         if n == 1: return [1] 
# #         for check in range(2, limit): 
# #              while num % check == 0: 
# #                 pFact.append(check) 
# #                 num /= check 
# #         if num > 1: 
# #           pFact.append(num) 
# #         return pFact 
