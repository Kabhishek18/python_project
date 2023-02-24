def print_board(board):
    """Print the Tic Tac Toe board."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    """Check if there is a winner."""
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    return None

def get_move(player, board):
    """Get the player's move."""
    valid_move = False
    while not valid_move:
        move = int(input(f"{player}, enter your move (1-9): "))
        if move < 1 or move > 9:
            print("Invalid move. Try again.")
        elif board[move-1] != ' ':
            print("That space is already occupied. Try again.")
        else:
            valid_move = True
    return move

def play_game():
    """Play a game of Tic Tac Toe."""
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    players = ['X', 'O']
    turn = 0
    winner = None
    while not winner and ' ' in board:
        print_board(board)
        player = players[turn % 2]
        move = get_move(player, board)
        board[move-1] = player
        winner = check_winner(board)
        turn += 1
    print_board(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie.")

# Play a game
play_game()
