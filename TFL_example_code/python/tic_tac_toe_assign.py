# tic_tac_toe.py

from typing import List, Optional, Tuple

def display_board(board: List[str]) -> None:
    """Prints the current board to the terminal."""
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    
def is_valid_move(board: List[str], row: int, col: int) -> bool:
    """Checks if a move is valid (index is within range and the cell is empty)."""
    pass

def make_move(board: List[str], row: int, col: int, player: str) -> None:
    """Applies the player's move to the board."""
    pass

def get_winner(board: List[str]) -> Optional[str]:
    """Returns 'X' or 'O' if there is a winner, or None if there is no winner yet."""
    pass

def is_full(board: List[str]) -> bool:
    """Returns True if the board is full."""
    pass

def get_player_input(player: str, board: List[str]) -> Tuple[int, int]:
    """Prompts the current player for a valid move as row and column."""
    pass

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

if __name__ == "__main__":
    play_game()
