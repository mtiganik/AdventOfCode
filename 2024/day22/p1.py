

def mix(given, currSecret):
    return given ^ currSecret
def prune(currSecret):
    return currSecret % 16777216


def secret2kStep(n):
    secret = n
    for _ in range(2000):
        # step1
        given = secret*64
        secret = mix(given, secret)
        secret = prune(secret)

        # step2
        given = int(secret /32)
        secret = mix(given, secret)
        secret = prune(secret)

        #step3
        given = secret*2048
        secret = mix(given,secret)
        secret = prune(secret)
    return secret

res = 0
cnt = 0
for k in open("input.txt"):
    val = int(k.strip())
    currRes = secret2kStep(val)
    # print(currRes)
    res += currRes
    cnt +=1
    if cnt % 300 == 0:
        print(cnt)
print(res)
# ourNum = 1
# ourNum = secret2kStep(ourNum)
# print(ourNum)
# for k in range(10):
#     ourNum = secretStep(ourNum)
#     print(ourNum)



# # step1
# num2 = num*64
# num2 = mix(num2, num)
# num2 = prune(num2)

# # step2
# num2 = int(num2 /32)
# num2 = mix(num2, num)
# num2 = prune(num2)

# #step3
# num2 = num2*2048
# num2 = mix(num2,num)
# num2 = prune(num2)


# print(num2)