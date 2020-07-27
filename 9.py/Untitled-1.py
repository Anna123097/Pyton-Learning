аниил 11:17
"""
! Получить словарь чисел с их квадратами
! 3 ^ 2 = 3 * 3
! 4 ^ 2 = 4 * 4
! 4 ^ 3 = 4  4  4
"""

dict_square = {i : i ** 2  for i in range(10)}
print(dict_square)









"""
* Дано массив. Найти количество повторений каждого элемента
"""


"""
! [1,4,3,5,6,7,7,8] => 1 - 1раз, 4 - 1 раз, 3 - 1 раз, 7 - 2 раза ...
"""


import random

array_x = [random.randint(0, 20) for i in range(15)]

unique_values = list(set(array_x))

dict_x = { i:array_x.count(i)  for i in unique_values}
print(array_x)
print(dict_x)