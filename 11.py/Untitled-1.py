#1 Найти минимальное из 3-х чисел
#a = int(input('Введите число A = '))
#b = int(input('Введите число B = '))
#c = int(input('Введите число C = '))

#min = 0
#if a <= b:
#    min = a
#else:
#    min = b

#if c <= min:
#    min = c

#print(min)

#2 Найти максимальное из 4-х чисел
#a = int(input('Введите число A = '))
#b = int(input('Введите число B = '))
#c = int(input('Введите число C = '))
#d = int(input('Введите число D = '))

#max1 = 0
#max2 = 0
#max = 0
#if a >= b:
#    max1 = a
#else:
#    max1 = b

#if c >= d:
#    max2 = c
#else:
#    max2 = d
#if max1>max2:
#    max=max1
#else:
#    max=max2        
#print(max)

#3 Найти все делители числа N (Число N вводится с консоли)
#n = int(input('Введите N = '))

#for i in range(2, n+1):
#    k = 0
#    for j in range(1, n+1):
#        if i % j == 0:
#            k += 1
#    if k == 2:
#        print(f'{i} - простое число')

#4  Найти все делители числа N и записать их в словарь
#for i in range(2, n+1):
#    k = 0
#    for j in range(1, n+1):
#        if i % j == 0:
#            k += 1
#    if k == 2:
#        print(f'{i} - простое число')
        #dict.clear()

#5 Найти все уникальные числа
import random

x = [random.randint(1,16) for i in range(10)]
print(x, "-")

x.sort()
print("-"*10)
for i in range(len(x)-1):
    if x[i] != x[i+1]:
        print(x[i], end=' ')        