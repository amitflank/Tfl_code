"""FYI these are pretty slopilly written tests. I wrote these very quickly to show the concept of unit testing.
DO NOT use this as rubric for unit tests. I've added some limited commentary on how you could improve these tests in 
the future and this might be a good example for learning about refactoring."""

from random import randint
from typing import Tuple, List


from animals import Board, Tile, Herbivore, Carnivore

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


def test_add_animals(tests: int):
    for _ in range(tests):  
        rand_h = randint(1, 100)
        rand_w =  randint(1, 100)

        herbs = randint(0, 100)
        carni = randint(0, 100)

        new_board = Board(rand_h, rand_w, num_herb=herbs, num_carni=carni)

        get_num_animals(new_board, herbs, carni)

    print("Successfully intialized correct number animals {0} times".format(tests))

def gen_rand_int_tuples(num_ints: int, max_val: int) -> Tuple[int]:
    """returns a tuple of num_ints random integers, b/w 1 and max_val """
    return tuple([randint(1, max_val) for _ in range(num_ints)])

#pretty bad way to test btw, since we copy pasted code as we have no good method. Just a note as likely will not change this
def test_plant_growth():
    my_tups = gen_rand_int_tuples(5, 10)
    new_board = Board(*my_tups)

    for i in range(my_tups[0]):
        for j in range(my_tups[1]):
            growth_rate = randint(1, 5) #generate random growth rate for this tile 
            cur_tile = new_board.grid[i][j]
            cur_tile.plant.grow(growth_rate) #First grow out plants

            exp_cal = my_tups[2] * growth_rate #calculate expected calories

            assert cur_tile.plant.cal_val == exp_cal, "Expected {0} calories in plant but found {1}".format(exp_cal, cur_tile.plant.cal_val)

    print("Successfully grew plants")


def add_animals_to_tile(tile: Tile, num_herb: int, num_carni: int):
    """adds num_herb herbivores and num_carni carnivores to passed tile"""

    for _ in range(num_herb):
       tile.add_animal(Herbivore())

    for _ in range(num_carni):
        tile.add_animal(Carnivore())

#note we hardcoded all results but for a real test we would want to write the logic for calculating all this and generate with random conditions
def test_feed_animals():
    #format: [num_herb, num_carni]
    expected_animals = [ 
                        [
                            (1, 0), (0, 0), (2, 0)],
                            [(1, 1), (0, 0), (0, 2)],
                            [(0, 2), (0, 0), (0, 0)]
    ]

    #format: [plant_cal, numb_herb0, .., num_herb_N, num_carni0, ..., num_carni_N]
    expected_cal_vals = [
                            [[0, 125], [25], [0, 125, 100]],
                            [[0, 100, 400], [25], [0, 400, 100]],
                            [[25, 100, 100], [25], [25]]
    ]

    new_board = Board(height=3, width=3, num_herb= 0, num_carni = 0)

   
    add_animals_to_tile(new_board.grid[0][0], 1, 0) #add 1 herbivore to tile 0,0
    add_animals_to_tile(new_board.grid[0][2], 2, 0) #add 2 herbivore to tile 0,2
    
    add_animals_to_tile(new_board.grid[1][0], 2, 1) #add 2 herbivore to tile and 1 carnivore 1,0

    add_animals_to_tile(new_board.grid[1][2], 1, 2) #add 1 herbivore 2 carnivore to tile 1,2
    add_animals_to_tile(new_board.grid[2][0], 0, 2) #add 2 carnivore to tile 2,0

    for i in range(3):
        for j in range(3):
            cur_tile = new_board.grid[i][j]
            cur_tile.plant.grow(5) #grow all plants with 25 calories

            new_board.feed_animals(cur_tile.contains, cur_tile)

            num_herb, num_carni = cur_tile.get_num_by_type_animals()
            exp_herb, exp_carni = expected_animals[i][j]

            assert num_herb == exp_herb, "Expected {0} herbivores on tile at index {1}, {2}, but found {3}".format(exp_herb, i, j, num_herb)
            assert num_carni == exp_carni, "Expected {0} carnivores on tile at index {1}, {2}, but found {3}".format(exp_carni, i, j, num_carni)
            
            #get calories for all plants and animals in our current tile
            tile_cal_vals = [cur_tile.plant.cal_val]
            for animal in cur_tile.contains:
                tile_cal_vals.append(animal.cal_val)

            assert tile_cal_vals == expected_cal_vals[i][j], "Expected {0} calorie distribution on tile at index {1}, {2}, but found {3}".format(expected_cal_vals[i][j], i, j, tile_cal_vals)



    print("Successfully fed the animals")

def test_move_animals():
    pass


random_board_create_test(20)
test_add_animals(20)
test_plant_growth()
test_feed_animals()


#Note we can talk about downside of efficient implementation of board loop on tests since it make it difficult to write clean tests for internal loop elements
#Feed, move, grow cycle day