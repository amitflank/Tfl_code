# minesweeper_assignment.py

from typing import List, Tuple

def validate_dimensions(solution: List[List[bool]]) -> Tuple[int, int]:
    """
    Ensure every row in `solution` has the same length.
    Returns (num_rows, num_cols).
    """
    # TODO: 
    # 1. Check that `solution` is not empty.
    # 2. Check that each row has the same number of columns.
    # 3. If invalid, raise ValueError with an informative message.
    # 4. Otherwise, return (number of rows, number of columns).
    pass


def get_neighbors_coords(row: int, col: int, num_rows: int, num_cols: int) -> List[Tuple[int, int]]:
    """
    Return list of valid (r, c) neighbor coordinates around (row, col) in the grid.
    """
    # TODO:
    # 1. Define the eight relative neighbor offsets.
    # 2. For each offset, compute the candidate (r, c).
    # 3. Include only those within [0, num_rows) and [0, num_cols).
    # 4. Return the list of valid neighbor tuples.
    pass


def count_adjacent_bombs(solution: List[List[bool]],row: int, col: int,num_rows: int, num_cols: int) -> int:
    """
    Count how many bombs (True values) are in the neighboring cells of (row, col).
    Assumes (row, col) itself is not a bomb.
    """
    # TODO:
    # 1. Use get_neighbors_coords to get valid neighbors.
    # 2. Iterate over those neighbors and count how many are True in `solution`.
    # 3. Return the total count.
    pass


def generate_hint_grid(solution: List[List[bool]]) -> List[List[int]]:
    """
    Given a 2D bomb grid (`solution`), return a same-size 2D hint grid:
      -1 indicates a bomb cell;
      otherwise, the count (0–8) of adjacent bombs.
    """
    # TODO:
    # 1. Validate dimensions with validate_dimensions.
    # 2. Create an output grid of zeros with the same shape.
    # 3. For each cell (r, c):
    #      - If solution[r][c] is True, set hint[r][c] = -1.
    #      - Else, set hint[r][c] = count_adjacent_bombs(...).
    # 4. Return the completed hint grid.
    pass


def all_safe(solution: List[List[bool]]) -> bool:
    """
    Return True if there are no bombs left on the board (i.e., all cells are False).
    """
    # TODO:
    # 1. Check every cell in every row.
    # 2. If any cell is True, return False.
    # 3. Otherwise, return True.
    pass
