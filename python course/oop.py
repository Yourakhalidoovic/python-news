import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class board:
    board: list = []
    def __init__(self):
        temp = 1
        for row in range(3):
            temp_list = []
            for col in range(3):
                temp_list.append(temp)
                temp += 1
            self.board.append(temp_list)

    def display_board(self):
        print('+-------+-------+-------+')
        for row in self.board:
            print('|       |       |       |')
            for col in row:
                if col == 'X':
                    color = Fore.BLUE
                elif col == 'O':
                    color = Fore.RED
                else:
                    color = Fore.RESET
                print(f'|   {color}{col}{Style.RESET_ALL}   ', end = '')
            print('|')
            print('|       |       |       |')
            print('+-------+-------+-------+')

    def enter_move(self, cell:int, sign):
        row, col = divmod(cell - 1, 3)
        if self.board[row][col] !='O' and self.board[row][col] != 'X':
            self.board[row][col] = sign
            return True
        else:
            print('Invalid place')
            return False



game = board()
game.display_board()

move = int(input('Enter your move: '))
game.enter_move(move, 'X')
game.display_board()

move = int(input('Enter your move: '))
game.enter_move(move, 'O')
game.display_board()