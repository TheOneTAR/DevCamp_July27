__author__ = 'TheOneTAR'
import time
import sys
import os



def percentage_count():
    for i in range(100):
        time.sleep(1)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()

raw_board = [[' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ']]

board = [['X','O','X',' ',' ',' '],
         ['O','X','O',' ',' ',' '],
         ['X','O','X',' ',' ',' '],
         ['O','X','O','X',' ',' '],
         ['X','O','X',' ',' ',' '],
         ['X','O','X',' ',' ',' '],
         ['O','X',' ',' ',' ',' ']]

def drop_piece(target, current, old, board, piece="\u25cb"):

    if target != old:
        time.sleep(0.2)
        #Then 'drop' it down through the rows
        # Tuples is (column,row)
        if old != None:
            board[old[0]][old[1]] = ' '
        board[current[0]][current[1]] = piece
        new_current = (current[0], current[1]-1)
        print_board(board)

        #Recursive!
        drop_piece(target, new_current, current, board, piece)

    # else:
    #     print_board(board)


def print_board(board):

    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write("\r")
    for i in range(5,0,-1):
        print('|',"|".join(column[i] for column in board), end='|\n', sep="")
    print("|-------------|")
    print("-             -")

    sys.stdout.flush()

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    drop_piece((2,-5),(2,-1),None,raw_board)

    drop_piece((3,-5),(3,-1),None,raw_board,"\u25cf")

    drop_piece((3,-4),(3,-1),None,raw_board)

    drop_piece((4,-5),(4,-1),None,raw_board,"\u25cf")