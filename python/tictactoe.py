#!/usr/bin/env python3
import copy

board = [[0,0,0],[0,0,0],[0,0,0]]

def draw_board(board):
    size = 3
    # Convert numerical board to drawable strings
    to_draw = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                to_draw[i][j] = " X "
            elif board[i][j] == 2:
                to_draw[i][j] = " O "
            elif board[i][j] == 0:
                to_draw[i][j] = "   "
    
    # Draw board with contents
    for i in range(len(to_draw)):
        print(" ---" * size)
        print("|%s|%s|%s|" % (to_draw[i][0], to_draw[i][1], to_draw[i][2]))
    print(" ---" * size)

def update_board(board, player, coords):
    # Check correctnes of user input
    if (        (len(coords) > 1)
            and (coords[0] and coords[1])
            and (coords[0].isdigit() and coords[1].isdigit())):
        coords = [int(x.strip())-1 for x in coords]
        # Check if coordinates are within board and quadrant is still available
        if(     (coords[0] < len(board[0]))
            and (coords[1] < len(board)) 
            and (board[coords[1]][coords[0]] == 0)):
            board[coords[1]][coords[0]] = int(player)
            return True
    else:
        return False

def get_winner(board):
    # Get rows from board
    col1 = [row[0] for row in board]
    col2 = [row[1] for row in board]
    col3 = [row[2] for row in board]
    
    # Get diagonals from board (1: lt--rb, 2: rt--lb)
    dia1 = [board[i][i] for i in range(len(board))]
    dia2 = [board[abs(i-2)][i] for i in reversed(range(len(board)))]

    # Check rows
    if len(set(board[0])) == 1 and list(set(board[0]))[0] != 0:
        return list(set(board[0]))[0]
    elif len(set(board[1])) == 1 and list(set(board[1]))[0] != 0:
        return list(set(board[1]))[0]
    elif len(set(board[2])) == 1 and list(set(board[2]))[0] != 0:
        return list(set(board[2]))[0]
    # Check colums
    elif len(set(col1)) == 1 and list(set(col1))[0] != 0:
        return list(set(col1))[0]
    elif len(set(col2)) == 1 and list(set(col2))[0] != 0:
        return list(set(col2))[0]
    elif len(set(col3)) == 1 and list(set(col3))[0] != 0:
        return list(set(col3))[0]
    # Check diagonals
    elif len(set(dia1)) == 1 and list(set(dia1))[0] != 0:
        return list(set(dia1))[0]
    elif len(set(dia2)) == 1 and list(set(dia2))[0] != 0:
        return list(set(dia2))[0]
    else:
        return 0

def main():
    # Loop until one player won
    while get_winner(board) == 0:
        # Loop until player inputs valid values
        p1_in = False
        p2_in = False
        while not p1_in:
            p1 = input("[P1] Enter the x,y you want place your \'X\' in: ").split(",")
            p1_in = update_board(board, 1, p1)
        draw_board(board)
        while not p2_in:
            p2 = input("[P2] Enter the x,y you want place your \'O\' in: ").split(",")
            p2_in = update_board(board, 2, p2)
        draw_board(board)
    print("The winner is Player %s" % get_winner(board))
    
if __name__ == "__main__":
    main()
