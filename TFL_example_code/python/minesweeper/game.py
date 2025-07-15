from typing import List, Tuple

def validate_dimensions(solution: List[List[bool]]) -> Tuple[int, int]:
    """
    Ensure every row in `solution` has the same length.
    Returns (num_rows, num_cols).
    Raises ValueError on ragged rows or empty board.
    """
    if not solution:
        raise ValueError("Board must have at least one row")
    
    num_cols = len(solution[0])
    if num_cols == 0:
        raise ValueError("Board rows must have at least one column")
    
    for i, row in enumerate(solution):
        if len(row) != num_cols:
            raise ValueError(f"Row {i} has length {len(row)}; expected {num_cols}")
    return len(solution), num_cols

def get_neighbors_coords(row: int, col: int, num_rows: int, num_cols: int) -> List[Tuple[int, int]]:
    """
    Return list of valid (r, c) neighbors around (row, col) in 2D.
    """
    deltas = [(-1,-1), (-1,0), (-1,1),
              ( 0,-1),         ( 0,1),
              ( 1,-1), ( 1,0), ( 1,1)] # postions of all neighboring tiles relative to this tile
    neighbors: List[Tuple[int,int]] = []


    for row_diff, col_diff in deltas:
        row_pos = row + row_diff # calculate row position of tile being checked
        col_pos =  col + col_diff # calculate column position of tile being checked

        if 0 <= row_pos < num_rows and 0 <= col_pos < num_cols: # Ensure within bounds
            neighbors.append((row_pos, col_pos))
    return neighbors

def count_adjacent_bombs(solution: List[List[bool]], row: int, col: int, num_rows: int, num_cols: int) -> int:
    """
    Count bombs in the 8 neighbors of (row, col).
    Assumes (row, col) itself is not a bomb.
    """
    count = 0
    for r, c in get_neighbors_coords(row, col, num_rows, num_cols):
        if solution[r][c]:
            count += 1
    return count

def generate_hint_grid(solution: List[List[bool]]) -> List[List[int]]:
    """
    Given a 2D bomb grid, return a same‑size hint grid:
      -1 for bombs, otherwise 0–8 adjacent‑bomb count.
    """
    num_rows, num_cols = validate_dimensions(solution)
    hints: List[List[int]] = [[0] * num_cols for _ in range(num_rows)]

    for row in range(num_rows):
        for col in range(num_cols):
            if solution[row][col]:
                hints[row][col] = -1
            else:
                hints[row][col] = count_adjacent_bombs(solution, row, col, num_rows, num_cols)
    return hints

def all_safe(solution: List[List[bool]]) -> bool:
    """
    Return True if _no_ bombs remain on the board.
    Demonstrates “all” logic.
    """
    for row in solution:
        for cell in row:
            if cell:
                return False
    return True
    # Equivalently: return not any(cell for row in solution for cell in row)
