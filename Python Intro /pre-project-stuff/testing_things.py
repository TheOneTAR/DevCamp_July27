__author__ = 'TheOneTAR'
import time
import sys
import os



def percentage_count():
    for i in range(100):
        time.sleep(1)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()

raw_board = [[' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ']]

board = [['X','O','X',' ',' ',' ',' '],
         ['O','X','O',' ','O','X','O'],
         ['X','O','X',' ','X','O','X'],
         ['O','X','O','X','O','X','O'],
         ['X','O','X','O','X','O','X'],
         ['O','X','O','X','O','X','O']]

def drop_piece(target, current, old, board, piece="O"):

    if target != old:
        time.sleep(0.2)
        #Then 'drop' it down through the rows
        # Tuples is (column,row)
        if old != None:
            board[old[0]][old[1]] = ' '
        board[current[0]][current[1]] = piece
        new_current = (current[0]-1, current[1])
        print_board(board)

        #Recursive!
        drop_piece(target, new_current, current, board, piece)

    # else:
    #     print_board(board)


def print_board(board):

    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write("\r")
    for column in reversed(board):
        print('|',end='')
        for row in column:
            print(row,"|",sep='',end='')
        print()
    print("|-------------|")
    print("-             -")

    sys.stdout.flush()

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    drop_piece((-6,2),(-1,2),None,raw_board)