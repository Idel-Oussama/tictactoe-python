import math

# Initialize the board
def init_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('|'.join(row))
        print('-' * 5)

# Check for a win
def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

# Check if the board is full
def is_board_full(board):
    return ' ' not in board

# Get the available moves
def get_available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

# Find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = 0
    for i in get_available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move

# Player move
def player_move(board, player):
    move = int(input(f"Enter your move ({player}) (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = player
    else:
        print("Invalid move. Try again.")
        player_move(board, player)

# Main game loop
def main():
    board = init_board()
    print("Welcome to Tic-Tac-Toe!")
    
    mode = input("Enter '1' to play with a friend or '2' to play against the AI: ")
    
    if mode == '1':
        print("You chose to play with a friend.")
        print_board(board)
        while True:
            player_move(board, 'X')
            print_board(board)
            if is_winner(board, 'X'):
                print("Player X wins!")
                break
            if is_board_full(board):
                print("It's a tie!")
                break

            player_move(board, 'O')
            print_board(board)
            if is_winner(board, 'O'):
                print("Player O wins!")
                break
            if is_board_full(board):
                print("It's a tie!")
                break
                
    elif mode == '2':
        print("You chose to play against the AI.")
        print_board(board)
        while True:
            player_move(board, 'X')
            print_board(board)
            if is_winner(board, 'X'):
                print("You win!")
                break
            if is_board_full(board):
                print("It's a tie!")
                break

            ai_move = best_move(board)
            board[ai_move] = 'O'
            print("AI's move:")
            print_board(board)
            if is_winner(board, 'O'):
                print("AI wins!")
                break
            if is_board_full(board):
                print("It's a tie!")
                break
    else:
        print("Invalid choice. Please restart the game and choose either '1' or '2'.")

if __name__ == "__main__":
    main()
