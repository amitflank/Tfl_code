# test_minesweeper.py
from minesweeper import (
    validate_dimensions,
    get_neighbors_coords,
    count_adjacent_bombs,
    generate_hint_grid,
    all_safe,
)

def expect_exception(exc_type, fn, *args, **kwargs):
    """
    Helper: assert that calling fn(*args, **kwargs) raises exc_type.
    """
    try:
        fn(*args, **kwargs)
    except Exception as e:
        assert isinstance(e, exc_type), f"Expected {exc_type}, got {type(e)}"
    else:
        assert False, f"Expected exception {exc_type}, but none was raised"

def run_all_tests():
    # validate_dimensions
    expect_exception(ValueError, validate_dimensions, [])
    expect_exception(ValueError, validate_dimensions, [[True, False], [True]])
    assert validate_dimensions([[True, False],[False,True]]) == (2,2)

    # get_neighbors_coords
    center = set(get_neighbors_coords(1,1,3,3))
    assert center == {
        (0,0),(0,1),(0,2),
        (1,0),       (1,2),
        (2,0),(2,1),(2,2),
    }
    edge = set(get_neighbors_coords(0,1,3,3))
    assert edge == {(0,0),(0,2),(1,0),(1,1),(1,2)}

    # count_adjacent_bombs
    board = [
        [False, False, False],
        [False, True,  False],
        [False, False, False],
    ]
    assert count_adjacent_bombs(board, 0, 0, 3, 3) == 1
    assert count_adjacent_bombs(board, 1, 1, 3, 3) == 0

    # generate_hint_grid & all_safe
    sol = [
        [True, False],
        [False, True],
    ]
    expected = [
        [-1, 2],
        [ 2, -1],
    ]
    assert generate_hint_grid(sol) == expected
    assert not all_safe(sol)
    assert all_safe([[False, False], [False, False]])

    print("✅ All tests passed!")

if __name__ == "__main__":
    run_all_tests()
