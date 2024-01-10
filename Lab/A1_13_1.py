import random

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_victory(board):
    # Check rows
    for row in board:
        if all(cell == row[0] and cell != ' ' for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(3)):
        return True
    if all(board[i][2 - i] == board[0][2] and board[i][2 - i] != ' ' for i in range(3)):
        return True

    return False

def is_board_filled(board):
    return all(cell != ' ' for row in board for cell in row)

def player_turn(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def computer_turn(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)

def play():
    game_board = [[' ' for _ in range(3)] for _ in range(3)]
    player_symbol = 'X'
    computer_symbol = 'O'

    while True:
        display_board(game_board)

        # Player's move
        row, col = player_turn(game_board)
        game_board[row][col] = player_symbol

        # Check for victory or tie
        if check_victory(game_board):
            display_board(game_board)
            print("Congratulations! You win!")
            break
        elif is_board_filled(game_board):
            display_board(game_board)
            print("It's a tie!")
            break

        # Computer's move
        print("Computer's turn:")
        row, col = computer_turn(game_board)
        game_board[row][col] = computer_symbol

        # Check for victory or tie
        if check_victory(game_board):
            display_board(game_board)
            print("Sorry, you lose. The computer wins.")
            break
        elif is_board_filled(game_board):
            display_board(game_board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play()
