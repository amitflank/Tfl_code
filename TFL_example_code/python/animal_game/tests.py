"""FYI these are shallowly written tests. I wrote these very quickly to show the concept of unit testing.
DO NOT use this as exhaustive rubric for unit tests. I've added some limited commentary on how you could improve these tests in 
the future and this might be a good example for learning about refactoring."""

from random import randint
from typing import Tuple, List
from animals import Board, Tile, Herbivore, Carnivore

def create_random_board(height = None, width = None, num_herb = None, num_carni = None, growth_mul = 5):
    new_h = height if height else randint(5, 20)
    new_w = width if height else randint(5, 20)
    
    herb_prop = {'num_herb': randint(1, 20) if num_herb is None else num_herb, 'cal_val': 200, 'meat_val': 400, 'move_cost': 50}
    carni_prop = {'num_carni': randint(1, 20) if num_carni is None else num_carni, 'cal_val': 200, 'move_cost': 50}
    board_dim = {'height': new_h, 'width': new_w}
    return Board(board_dim, herb_prop, carni_prop, growth_mul= growth_mul)

def board_create_test(height, width):
    new_board = create_random_board(height, width)
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

        herbs = randint(0, 1)
        carni = randint(0, 1)
        new_board = create_random_board(rand_h, rand_w, num_herb = herbs, num_carni = carni)
        get_num_animals(new_board, herbs, carni)

    print("Successfully intialized correct number animals {0} times".format(tests))

def gen_rand_int_tuples(num_ints: int, max_val: int) -> Tuple[int]:
    """returns a tuple of num_ints random integers, b/w 1 and max_val """
    return tuple([randint(1, max_val) for _ in range(num_ints)])

#pretty bad way to test btw, since we copy pasted code as we have no good method. Just a note as likely will not change this
def test_plant_growth():
    growth_mul = randint(1,20)
    new_board = create_random_board(growth_mul= growth_mul)
    board_h = new_board.height
    board_w = new_board.width

    for i in range(board_h):
        for j in range(board_w):
            growth_rate = randint(1, 5) #generate random growth rate for this tile 
            cur_tile = new_board.grid[i][j]
            cur_tile.plant.grow(growth_rate) #First grow out plants

            exp_cal = growth_mul * growth_rate #calculate expected calories

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

    new_board = create_random_board(height=3, width=3, num_herb= 0, num_carni = 0)

   
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

def adj_exp_positions(x_init: int, y_init: int, distances: List[Tuple[int, int, int, int]], expected_animals: List[List[List[int]]], animal_idxs: List[int]):
    idx = 0
    for x_dist, y_dist,  _, _  in distances:
        exp_x_cord = x_init + x_dist
        exp_y_cord = y_init + y_dist

        try:
            expected_animals[exp_y_cord][exp_x_cord][animal_idxs[idx]] += 1
            expected_animals[y_init][x_init][animal_idxs[idx]] -= 1
        except:
            raise ValueError(exp_y_cord, exp_x_cord, idx)

        idx += 1

def test_move_all_animals_on_tile():
    expected_animals = [ 
                        [
                            [1, 0], [0, 0], [2, 0], [0, 0]],
                            [[1, 1], [0, 0], [0, 2], [0, 0]],
                            [[0, 2], [0, 0], [0, 0], [0, 0]],
                            [[0, 0], [0, 0], [0, 0], [0, 0]]
    ]


    new_board = create_random_board(height=4, width=4, num_herb= 0, num_carni = 0)

    add_animals_to_tile(new_board.grid[0][0], 1, 0) #add 1 herbivore to tile 0,0
    add_animals_to_tile(new_board.grid[0][2], 2, 0) #add 2 herbivore to tile 0,2
    
    add_animals_to_tile(new_board.grid[1][0], 2, 1) #add 2 herbivore to tile and 1 carnivore 1,0

    add_animals_to_tile(new_board.grid[1][2], 1, 2) #add 1 herbivore 2 carnivore to tile 1,2
    add_animals_to_tile(new_board.grid[2][0], 0, 2) #add 2 carnivore to tile 2,0

    for row in range(4):
        for col in range(4):
            cur_tile_animals = new_board.grid[row][col].contains
            copied_animals = cur_tile_animals.copy()

            #Example of being to fancy for ones own good this is bad code. It is pretty dope though.
            #Gets a list of 1's and 0's representing animals index's for herbivores and carnivores  

            #create lambda fxn assign to var then pass w/list to map
            #animal_index = [(lambda T: 0 if type(T) is Herbivore else 1)(animal) for animal in cur_tile_animals]
            
            test = (lambda T: 0 if type(T) is Herbivore else 1)
            animal_index = list(map(test, cur_tile_animals)) #map creates a generator so we need to save it in a persistent form
            
            distances = new_board.move_all_animals_on_tile(cur_tile_animals, row, col)
            adj_exp_positions(col, row, distances, expected_animals, list(animal_index))

            for idx, animal in enumerate(copied_animals):
                
                dist_idx = distances[idx][3]
                exp_cal = 100 - distances[dist_idx][2] * animal.move_cost
                assert animal.cal_val == exp_cal, "Expected animal to have {0} calories after moving but found {1} instead, {2}".format(exp_cal, animal.cal_val, distances[idx][2])

    for row in range(3):
        for col in range(3):
            cur_tile = new_board.grid[row][col]
            num_animals = cur_tile.get_num_by_type_animals() #Get number animals on tile

            assert num_animals[0] == expected_animals[row][col][0], "Expected {0} herbivores on tile {1}, {2} but found {3}".format(expected_animals[row][col][0], row, col, num_animals[0])
            assert num_animals[1] == expected_animals[row][col][1], "Expected {0} carnivores on tile {1}, {2} but found {3}".format(expected_animals[row][col][1], row, col, num_animals[1])



random_board_create_test(20)
test_add_animals(20)
test_plant_growth()
test_feed_animals()
test_move_all_animals_on_tile()


#Note we can talk about downside of efficient implementation of board loop on tests since it make it difficult to write clean tests for internal loop elements
#Feed, move, grow cycle day