import random

x = [random.randint(0,50) for i in range(200)]
unique_items = list( set(x) )
print(unique_items, "Вывод элементов")
print( sum(list(set(x))) )