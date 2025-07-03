from random import randint
from typing import List, Union, Tuple, Dict
from abc import ABC, abstractmethod

class Food():
    def __init__(self, food_type: str):
        pass

class Plant(Food):

    def __init__(self, growth_mul: int):
        #assign food_type to plant using super
        #set self.cal to 0
        #assign class property growth mul
        pass

    def grow(self, growth_rate: int):
        # set plant calories to existing calories plus growth_mul times growth rate
        pass


    def grazed(self) -> int:
        # sets plants calories to zero 
        # returns number of calories in plant
        pass

class Meat(Food):

    def __init__(self, food_type: str, cal:  int):
        # assign food_type to Meat
        # assign cal to class property
        pass


class Animal(ABC):

    def __init__(self, move_cost: int, cal_val: int = 100, max_move: int = 3):
        # assign args to class properties
        # assign is_alive class property to True
        # assign has_moved property to False
        pass

    def move(self, distance: int):
        #adjust animal remaning calories by distance times move_cost
        #if animals starved (calories <= 0) post move modify is_alive property
        pass

    def reset_movement(self):
        #assign has_moved property to False
        pass

    @abstractmethod
    def eat(self, food: Food):
        #abstract methods
        pass
    
class Herbivore(Animal):
    def __init__(self, cal_val: int = 500, move_cost = 50, meat_val: int = 300, max_move = 3):
        # use super to assign all class properties except for meat_val
        # assign meat_val as class property
        pass

    def eat(self, plant: Plant):
        #use plant grazed method to increase animals calories
        pass

    def get_eaten(self) -> Meat:
        #adjust is alive property
        #return appropriate meat object
        pass

class Carnivore(Animal):
    
    def __init__(self, cal_val: int  = 100, move_cost: int = 100, max_move = 2) -> None:
        #use super to assign all arguments to class properties
        pass
    
    def eat(self, food: Meat):
        #use food to adjust animals calories
        pass

class Tile():

    def __init__(self, contains: List[Animal], growth_mul: int):
        #assign property growth_rate to random int b/w 0 and 9 inclusive
        #assign property contains
        #assign property class to be a plant with growth_mul
        pass

    def add_animal(self, animal: Animal):
        #add passed animals end of property contains
        pass

    def get_num_by_type_animals(self):
        #return a list containing number of herbivores and number of carnivores
        pass

            
class Board():

    def __init__(self, height: int, width: int, growth_mul = 5, num_herb: int = 10, num_carni: int = 3, days: int = 10):
        self.corpse_count: int = 0
        self.grid: List[List[Tile]] = height * [None]
        self.height: int = height
        self.width: int = width
        self.create_board(growth_mul)
        self.add_animals(num_herb, num_carni)
        self.days: int = days

    def create_board(self, growth_mul: int):
        #creates board of tiles self.height by self.width
        #All tiles should assign their plants growth_mul as growth_mul
        pass
    
    def get_remaining_animals(self) -> Tuple[int, int]:
        #returns tuple of total sum of remaining herbivores and carnivores in our grid
        pass


    def add_animals(self, num_herb: int, num_carni: int):
        #randomly create and add to grid num_herb Herbivores and num_carni Carnivores
        #tile can hold arbitrary number of animals 
        pass

    def cycle_day(self):
        #loop over all tiles 
        #have all plants on all tiles grow
        #have all animals try and eat as specified by animal type
        #move all animals some legal random distance b/w 0 and max_movement
        pass

    def reset_animal_movement(self):
       #reset all animal bool movement properties for next cycle
       pass

    def move_animal(self, animal: Animal, x_cord: int, y_cord: int) -> Tuple[int, int, int]:
        #Move animals at x_cord, y_cord some random distance b/w 0 and max_distance of animals
        #Break up movement into x and y direction movement (note negative movement is allowe indicting downward or leftward movement)
        #Check to make sure movement is in bounds of our grid using validate_move to adjust if needed
        #If an animals starves remove it from game
        pass

    def clean_corpses(self, animals: List[Animal]):
        #remove all animal corpses in animals
        pass

    def feed_animals(self, animals: List[Animal], tile: Tile):
        #All animals on tile try and eat. Herbivores try and eat plants while carnivores can eat herbivores on same tile as them
        #Adjust all calory properties as needed.
        #If a Herbivore is eaten remove it from our game 
        pass
       
    def get_first_herbivore(self, animals: List[Animal]) -> Union[Herbivore, None]:
        #Find the first living herbivore in the list if it exists and return it.
        pass

    def move_all_animals_on_tile(self, animals: List[Animal], x_cord: int, y_cord: int) -> List[Tuple[int, int, int]]:
        #Move all animals on tile x_cord, y_cord, some random distance. 
        #returns list of tuple for x distance traveled, y distance traveled and total distance traveled for testing
        pass

    def validate_move(self, move_dist: int, cur_pos: int, max_val: int) -> int:
       #Check if move is valid if not flip direction of move otherwise do nothing and return current movement
        pass

# run_game():
# take from user following parameters:
# board heigh, width
# number herbivores 
# starting herbivore calories
# herbivore calorie move cost
# staring carnivore calories
# carnivore move cost
# days to run
# plant growth multiple
        
