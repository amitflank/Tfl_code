from random import randint
from typing import Tuple


from animals import Board, Tile
import pytest

def test_board_create():
    pass

def test_animal_add():
    pass


#This code is so trash. Really needs refactoring revamp. technically does the job but i kinda wanna throw up.
height = 10
width = 10

def board_create_test(height, width):
    new_board = Board(height, width)
    num_rows = len(new_board.grid)
    num_col = len(new_board.grid[0])
    assert num_rows == height, "Expected board to have {0} rows but found {1}".format(width, num_rows)
    assert num_col == width, "Expected board to have {0} rows but found {1}".format(height, num_col)

def random_board_create_test(tests: int):
    rand_h = randint(1, 100)
    rand_w =  randint(1, 100)

    for _ in range(tests):
        board_create_test(rand_h, rand_w)

    print("Successfully created {0} boards".format(tests))

def get_num_animals(board: Board, exp_herb, exp_carni):
    sum_herb, sum_carni = 0, 0
    for row in board.grid:
        for tile in row:
            assert type(tile) is Tile, "Found non tile object in grid"

            herb, carni  = tile.get_num_by_type_animals()

            sum_herb += herb
            sum_carni += carni

    assert exp_carni == sum_carni, "Expected {0} carnivores but found {1}".format(exp_carni, sum_carni)
    assert exp_herb == sum_herb, "Expected {0} herbivores but found {1}".format(exp_herb, sum_herb)


def randomize_num_animals(tests: int):
    for _ in range(tests):  
        rand_h = randint(1, 100)
        rand_w =  randint(1, 100)

        herbs = randint(0, 100)
        carni = randint(0, 100)

        new_board = Board(rand_h, rand_w, num_herb=herbs, num_carni=carni)

        get_num_animals(new_board, herbs, carni)

    print("Successfully intialized correct number animals {0} times".format(tests))

def gen_rand_int_tuples(num_ints: int, max_val: int) -> Tuple[int]:
    """returns a tuple of num_ints randoms integers, b/w 1 and max_val """
    return tuple([randint(1, max_val) for _ in range(num_ints)])

def test_plant_growth():
    my_tups = gen_rand_int_tuples(5, 10)
    print(my_tups)

    new_board = Board(*my_tups)

    print(new_board)

    for i in range(height):
        for j in range(width): 
            cur_tile = new_board.grid[i][j]
            cur_tile.plant.grow() #First grow out plants


random_board_create_test(20)
randomize_num_animals(20)
test_plant_growth()
