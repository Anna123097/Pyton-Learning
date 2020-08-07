"""
?Дан массив с рандомными числами. Найти минимальное и максимальное в массиве. 
!Заготовка кода ниже import random x = [random.random(1,5) for i in range(100)]
"""
import random 
x = [random.randint(-3,100) for i in range(100)]
print(x)
min=0
max=0
for i in range(0,len(x)):
    if min>x[i]:
        min=x[i]
    if(max<x[i]):
        max=x[i]
print(min)
print(max)
  


 

