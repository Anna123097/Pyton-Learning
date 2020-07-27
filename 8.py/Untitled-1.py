import random
x = [random.randint(1,16) for i in range(10)]
print(x, "BEFORE")


print(len(set(x)))