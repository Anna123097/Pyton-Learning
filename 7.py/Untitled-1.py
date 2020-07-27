"""
import random

"""
#!Вывести на экран все уникальные элементы
#!1-й способ
"""


x = [random.randint(0,15) for i in range(10000)]
y = []

print(x, "ARRAY BEFORE")

for i in range(len(x)):
    if x[i] not in y:

        y.append(x[i])


print(y, "NEW")

import random
"""
"""
!Вывести на экран все уникальные элементы
!2-й способ
"""


x = [random.randint(1,16) for i in range(10)]
print(x, "BEFORE")

x.sort()
print("-"*10)
for i in range(len(x)-1):
    if x[i] != x[i+1]:c
        print(x[i], end=' ')