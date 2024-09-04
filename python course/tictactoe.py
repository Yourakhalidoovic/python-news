from random import randrange

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+')

    for row in board:

        print('|       |       |       |')
        for col in row:
            if col == 'X':
                color = Fore.BLUE
            elif col == 'O':
                color = Fore.RED
            else:
                color = Fore.RESET
            print(f'|   {color}{col}{Style.RESET_ALL}   ', end = '')
        print()
        print('|       |       |       |')
        print('+-------+-------+-------+')
    



def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    loop = True
    while loop: 
        try:
            move = int(input('Enter your move: '))
            if move > 9 or move < 1:
                print('Invalid range')
            else:
                row, col = ((move-1)//3, (move-1)%3)
                row, col = divmod(move - 1, 3)
                # print(f'[{row}][{col}]')
                if board[row][col] !='O' and board[row][col] != 'X':
                    board[row][col] = 'O'
                    loop = False
                else:
                    print('Invalid place')
        except ValueError:
            print('Invalid Input')



def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_list = []
    for row in range(3):
        for col in range(3):
            if board[row][col] !='O' and board[row][col] != 'X':
                free_list.append((row,col))
    return free_list



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    s = f'The winner is {sign}'

    for row in range(3):
        # print(f'=={row}==')
        summ = 0
        for col in range(3):
            # print(f"[{row}][{col}]")
            if board[row][col] == sign:
                summ+=1
        # print(summ)
        if summ == 3:
            print(s)
            return 0
        


    for col in range(3):
        summ = 0
        for row in range(3):
            # print(f"[{row}][{col}]")
            if board[row][col] == sign:
                summ+=1
        # print('='*10)
        if summ == 3:
            print(s)
            return 0


    summ = 0
    for x in range(3):
        # print(f"[{x}][{x}]")
        if board[x][x] == sign:
                summ+=1
    if summ == 3:
        print(s)
        return 0
    
    summ = 0
    for x in range(3):
        # print(f"[{x}][{2-x}]")
        if board[x][2-x] == sign:
                summ+=1
    if summ == 3:
        print(s)
        return 0

    
    return 1



def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    # print()
    r = randrange(len(free_fields)) # get a random number in the range of the number of free fields
    row, col = free_fields[r] # (row, col)
    board[row][col]='X'




def main():
    k = 1
    board = []

    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(k)
            k += 1
        board.append(temp)

    board[1][1] = 'X'

    while True:
        display_board(board)

        enter_move(board)
        if victory_for(board, 'O') == 0:
            break
        
        draw_move(board)
        if victory_for(board, 'X') == 0:
            break

        if len(make_list_of_free_fields(board)) == 0:
            print('Draw')
            break

    display_board(board)
