"""
Дано строку, найти все уникальные элементы и их количество повторений
"""
string = "Hello, world, my name is Anna"
sum=0
for i in range(0,len(string)):
    print(len(set(string)))
    