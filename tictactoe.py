import numpy as np


def game_representation(data):
    matrix = np.array(data, dtype='str').reshape((3, 3))
    print('---------')
    for i in range(3):
        print(f"| {str(matrix[i, 0])} {str(matrix[i,1])} {str(matrix[i, 2])} |")
    print('---------')
    return matrix


def winner(board, symbol):
    if board[0, 0] == board[1, 1] == board[2, 2] == symbol:
        return True, symbol
    elif board[0, 2] == board[1, 1] == board[2, 0] == symbol:
        return True, symbol
    for i in range(3):
        if (board[i, :] == symbol).all():
            return True, symbol
        if (board[:, i] == symbol).all():
            return True, symbol
    else:
        return False, symbol


def x_wins(board):
    condition, player = winner(board, 'X')
    if condition and player == 'X':
        return True
    return False


def o_wins(board):
    condition, player = winner(board, 'O')
    if condition and player == 'O':
        return True
    return False


def draw(board):
    if np.count_nonzero(board == ' ') == 0:
        return True
    return False


def situation(board):
    if x_wins(board):
        print('X wins')
        exit()
    elif o_wins(board):
        print('O wins')
        exit()
    elif draw(board):
        print('Draw')
        exit()


def coordinates(board, symbol):
    while True:
        info = input('Enter the coordinates: ').split()
        try:
            info = [int(number) for number in info]
        except (ValueError, TypeError):
            print('You should enter numbers!')
        else:
            if len(info) != 2 or info[0] not in [1, 2, 3] or info[1] not in [1, 2, 3]:
                print('Coordinates should be from 1 to 3!')
            elif board[info[0] - 1, info[1] - 1] == ' ':
                board[info[0] - 1, info[1] - 1] = symbol
                return board
            else:
                print('This cell is occupied! Choose another one!')


def main():
    data = [' ' for _ in range(9)]
    board = game_representation(data)
    move = 0
    while True:
        move += 1
        if move % 2 != 0:
            symbol = 'X'
        else:
            symbol = 'O'
        board = game_representation(coordinates(board, symbol))
        situation(board)


main()
