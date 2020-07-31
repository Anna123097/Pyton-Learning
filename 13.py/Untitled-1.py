"""
class Toy:
    def __init__(self, name ='lol', year='29.07.2020'):
        self.name = name
        self.year = year
    def Toys(self):
        print(f"игрушка по имени {self.lol}  c year {self.29.07.2020}")

    def year_of_toy(self):
        print(f"дата покупки игрушки{year}")
#__1.__ Создать класс с именем `Toy`. В методе `__init__` должны быть свойства `name` - имя игрушки. И `year` - дата покупки игрушки.  
#И создать методы `play` и `sleep`. Метод `sleep` - выводит на экран `Я иду спать`. Метод `play` - выводит на экран `Я играюсь с игрушкой под
# именем {name_of_toy}`.
# А так же, создать метод `year_of_toy` - который возвращает дату создания/покупки игрушки.
"""


a=int(input("a= "))
b=int (input("b= "))
sum=0
for i in range(b,a+1):
    sum+=i
print(sum)    
#__2.__ Найти сумму чисел от `a` до `b` включительно на двух отрезках. `a` и `b` вводятся с клавиатуры