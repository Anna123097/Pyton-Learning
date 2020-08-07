import random

class GameLabirint:


    size = 5
    matrix = [ [ (" " if random.randint(0,1) == 1 else "8")  for j in range(5)]  for i in range(5)]
    
    def __init__(self, name_player='Player'):
        self.name = name_player
        self.Hello()

    def Hello(self):
        print(f'Привет, игрок {self.name}')
        
        if (input('Перейти в игру?(д/н) = ') == 'д'):
            self.StartGame()
        else:
            print("Пока.") 


    def PrintMatrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(self.matrix[i][j], end=' ')
            print()

    def StartGame(self):
        print('\n\nНачинаем игру')

        self.PrintMatrix()




def main():
    game = GameLabirint('Danik')


if __name__ == "__main__":
    main()

