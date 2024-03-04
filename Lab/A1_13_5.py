# AIM 5 : Write program to implement Min-Max algorithm on Tic-Tac-Toe game 

import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return row[0]

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

    # Check for a tie
    if all([cell != '-' for row in board for cell in row]):
        return 'tie'

    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner is not None:
        if winner == 'X':
            return -10 + depth, None
        elif winner == 'O':
            return 10 - depth, None
        else:
            return 0, None

    if is_maximizing:
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score, _ = minimax(board, depth + 1, False)
                    board[i][j] = '-'
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score, _ = minimax(board, depth + 1, True)
                    board[i][j] = '-'
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move

def play():
    board = [['-' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's move
        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == '-':
                board[row][col] = 'X'
                break
            else:
                print("Invalid move! Try again.")

        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

        # Computer's move
        score, move = minimax(copy.deepcopy(board), 0, True)
        board[move[0]][move[1]] = 'O'
        print("Computer's move:")
        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

play()
