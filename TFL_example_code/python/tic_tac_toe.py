from typing import List, Optional, Tuple

def display_board(board: List[str]) -> None:
    """Prints the current board to the terminal."""
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    
def is_valid_move(board: List[str], row: int, col: int) -> bool:
    """Checks if a move is valid (index is within range and the cell is empty)."""
    index = row * 3 + col
    return 0 <= index < 9 and board[index] == " "

def make_move(board: List[str], row: int, col: int, player: str) -> None:
    """Applies the player's move to the board."""
    index = row * 3 + col
    board[index] = player

def get_winner(board: List[str]) -> Optional[str]:
    """Returns 'X' or 'O' if there is a winner, or None if there is no winner yet."""
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for combo in win_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def is_full(board: List[str]) -> bool:
    """Returns True if the board is full."""
    return " " not in board

def get_player_input(player: str, board: List[str]) -> Tuple[int, int]:
    """Prompts the current player for a valid move as row and column."""
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter the column (1-3): ")) - 1
            if is_valid_move(board, row, col):
                return row, col
            print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers from 1 to 3.")

def play_game() -> None:
    """Runs the main game loop."""
    board = [" "] * 9
    current_player = "X"
    winner = None

    while not is_full(board) and not winner:
        display_board(board)
        row, col = get_player_input(current_player, board)
        make_move(board, row, col, current_player)
        winner = get_winner(board)
        current_player = "O" if current_player == "X" else "X"

    display_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")


play_game()
