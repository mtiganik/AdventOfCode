

num = 123
mod = 16777216

def mix(given, currSecret):
    return given ^ currSecret
def prune(currSecret):
    return currSecret % 16777216


# secret = 42
# ourmix = 15

# ores = mis()

# step1
num2 = num*64
num2 = mix(num2, num)
num2 = prune(num2)

# step2
num2 = int(num2 /32)
num2 = mix(num2, num)
num2 = prune(num2)

#step3
num2 = num2*2048
num2 = mix(num2,num)
num2 = prune(num2)


print(num2)