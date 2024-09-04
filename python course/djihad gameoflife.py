
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


class grid:

    def __init__(self, row, col):
        self.board = []
        # k = 1
        for i in range(row):
            temp_list = []
            for j in range(col):
                temp_list.append(0)
                # k += 1
            self.board.append(temp_list)
            

    def display_board(self):
        # for i in range(len(self.board)):
        #     for j in range(len(self.board[i])):
        #         print(self.board[i][j], end="  ")
        #     print() 
        # print()
        print('='*(len(self.board[0])*3))
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    print(Fore.WHITE + ".", end="  ")
                if self.board[i][j] == 1:
                    print(Fore.RED + "0", end="  ")
                if self.board[i][j] == 2:
                    print(Fore.BLUE + " ", end="  ")
            
            print(Fore.RESET+"|")
        print('='*(len(self.board[0])*3))
        print()

    def update_board(self, row, col, value):
        self.board[row][col] = value

    def update(self):
        future_board = []
        for i in range(len(self.board)):
            temp_list = []
            for j in range(len(self.board[i])):
                summ = 0
                if i+1 < len(self.board):
                    summ += self.board[i+1][j]
                if i-1 >= 0:
                    summ += self.board[i-1][j]
                if j+1 < len(self.board[i]):
                    summ += self.board[i][j+1]
                if j-1 >= 0:
                    summ += self.board[i][j-1]

                if i+1 < len(self.board) and j+1 < len(self.board[i]):
                    summ += self.board[i+1][j+1]
                if i-1 >= 0 and j-1 >= 0:
                    summ += self.board[i-1][j-1]

                if i+1 < len(self.board) and j-1 >= 0:
                    summ += self.board[i+1][j-1]
                if i-1 >= 0 and j+1 < len(self.board[i]):
                    summ += self.board[i-1][j+1]
                
                if self.board[i][j] == 0:
                    if summ == 3:
                        temp_list.append(1)
                    else:
                        temp_list.append(0)
                else:
                    if summ == 2 or summ == 3:
                        temp_list.append(1)
                    else:
                        temp_list.append(0)
            future_board.append(temp_list)
        self.board = future_board

g1 = grid(3, 3)
g1.update_board(1, 1, 1)
g1.update_board(1, 2, 1)
g1.update_board(1, 0, 1)
for i in range(10):
    g1.update()
    g1.display_board()
    time.sleep(0.5)