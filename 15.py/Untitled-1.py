import random
import os
import time

class GameLabirint:




    def __init__(self, name_player='Player'):
        self.name = name_player

        self.size = 10
        self.matrix = [ [ ("8" if random.randint(0,3) == 0 else " ")
                for j in range(self.size)]
                    for i in range(self.size)]
        
        self.matrix[0][0] = 'X'
        self.matrix[self.size - 1][self.size - 1] = "F"

        self.curr_cordinate = [0, 0]


        self.moves = {
            'w':(0,-1),
            'a':(-1, 0),
            's' : (0, 1),
            'd' : (1, 0)
        }


        self.Hello()


    def Hello(self):
        print(f'Привет, игрок {self.name}\n')
        
        if (input('\tПерейти в игру?(д/н) = ') == 'д'):
            time.sleep(1)
            self.StartGame()
        else:
            print("Пока.") 



    def inputWay(self):
        x = input("\n\nВведите ваш ход: ")
        return x


    #
    #!  1111
    #!  1101
    #!  1011
    #!  0101
    #

    def Move(self, way):

        """
        ? Не реализована
        """
        print(self.moves[way])


    def PrintMatrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(self.matrix[i][j], end=' ')
            print()
        print('\n\nF - Выход\nX - Игрок')


    def StartGame(self):
        print('\n\nНачинаем игру')
        time.sleep(1)

        while True:
            os.system("cls")
            
            self.PrintMatrix()
            self.Move(self.inputWay())




def main():
    game = GameLabirint('Danik')


if __name__ == "__main__":
    main()
