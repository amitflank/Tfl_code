"""
This project represents a simple game theory assignment used to introduce concepts such as nested loops, classes and inheritance to new programers. 
It involves creating a board with carnivores, herbivores and plants and observing how outcomes differ if we give each of these creatures different starting 
properties. """

from random import randint
from typing import List, Union, Tuple, Dict
from abc import ABC, abstractmethod

#Note: Need to cheat and add min board size since we can easily get out of range issues w/small boards and current validate move implementation
class Food():
    """
    Kinda of a unnecessary class for the most part as all it does is store a single class property.
    Mostly we are using this class as a way to highlight how inheritance works. 

    Args:
        food_type: string representing if we are a plant of meat.

    """
    def __init__(self, food_type: str):
        self.food_type: str = food_type

class Plant(Food):
    """
    Represents a plant that grows on our game board and will be consumed by herbivores.

    Args:
        growth_mul: int that represents a scaling factor of plant growth rate (how many calories it adds each day)
    """
    def __init__(self, growth_mul: int):
        super().__init__("Plant")
        self.cal_val: int = 0
        self.growth_mul: int = growth_mul
       
    def grow(self, growth_rate: int):
        """Adds calories to this plant. growth_rate used a scaling multiple for growth. """
        self.cal_val += self.growth_mul * growth_rate

    def grazed(self) -> int:
        """resets plants calories to 0 and returns number of calories reduced"""
        g_cal = self.cal_val
        self.cal_val -= self.cal_val
        return g_cal

class Meat(Food):
    """
    Represents a food created on animal death can be consumed by carnivores.

    Args:
        cal_val: int that caloric value of consuming this meat"""
    def __init__(self, cal_val:  int):
        super().__init__("Meat")
        self.cal_val: int = cal_val

class Animal(ABC):
    """
    Parent class of all movable creatures on our game board.

    Args:
        move_cost: calories cost of moving a tile for this animal.
        cal_val: current calories available for animal to take actions
        max_move: maximum number of tile this animal can move in a day"""

    def __init__(self, move_cost: int, cal_val: int = 100, max_move: int = 3):
        self.move_cost: int = move_cost
        self.cal_val: int = cal_val
        self.max_move: int = max_move
        self.is_alive: bool = True
        self.has_moved: bool = False

    def move(self, distance: int):
        """reduce animal calories based on distance traveled and kill it if calories are <= 0 post move"""
        self.cal_val -= distance * self.move_cost
        self.has_moved = True

        #animal starved
        if self.cal_val <= 0:
            self.is_alive = False

    def reset_movement(self):
        """reset has_moved property to false for next cycle"""
        self.has_moved = False
    
    @abstractmethod
    def eat(self, food: Food):
        pass 
    

class Herbivore(Animal):
    """
    Parent class of all movable creatures on our game board.

    Args:
        move_cost: calories cost of moving a tile for this animal.
        cal_val: current calories available for animal to take actions
        max_move: maximum number of tile this animal can move in a day
        meat_val: caloric value of consuming this herbivore"""

    def __init__(self, cal_val: int = 100, move_cost = 50, meat_val: int = 300, max_move = 2):
        super().__init__(move_cost, cal_val, max_move)
        self.meat_val: int = meat_val
    
    def eat(self, plant: Plant):
        """consume plant and increase calories based on plants caloric output"""
        self.cal_val += plant.grazed()

    def get_eaten(self):
        """kill this animal and return a Meat object with meat_val calories"""
        self.is_alive = False
        return Meat(self.meat_val)


class Carnivore(Animal):
    """
    Represents an animal that only eats meat.

    Args:
        move_cost: calories cost of moving a tile for this animal.
        cal_val: current calories available for animal to take actions
        max_move: maximum number of tile this animal can move in a day"""
    
    def __init__(self, cal_val: int  = 100, move_cost: int = 100, max_move = 2) -> None:
        super().__init__(move_cost, cal_val, max_move)
    
    def eat(self, food: Meat):
        """Add passed meats caloric value to this animals available calories"""
        self.cal_val += food.cal_val

class Tile():
    """
    Represents a location on our game board.

    Args:
        contains: List of animals on this tile. 
        growth_mul: scaling factor for plant growth on this tile.
    """

    def __init__(self, contains: List[Animal], growth_mul: int):
        self.growth_rate: int = randint(0,9)
        self.contains: List[Animal] = contains
        self.plant: Plant = Plant(growth_mul)

    def add_animal(self, animal: Animal):
        """adds animals to contains property"""
        self.contains.append(animal)

    def get_num_by_type_animals(self):
        """So for something like this we prob want so global list of legal animals for best practice but we will assume two for simple imp. 
        Just noting this is bad practice for education. Retruns tuple of (number herbivores, number carnivores) in tile"""
        herb = 0
        carni = 0
        for animal in self.contains:

            if type(animal) is Herbivore:
                herb += 1
            elif type(animal) is Carnivore:
                carni += 1
            else:
                raise ValueError("Found illegal non-animal in Tile contains")

        return herb, carni
            
class Board():

    """
    Represents game board in which all of our activities will take place. 

    Args:
        board_dim {height: int, width: int}
        herb_prop: {num_herb: int, cal_val: int, meat_val: int, move_cost: int}
        carni_prop: {num_carni: int, cal_val: int, move_cost: int}
        growth_mul: scaling factor for plant growth for all board tiles
    """
    def __init__(self, board_dim: Dict[str, int], herb_prop: Dict[str, int], carni_prop: Dict[str, int], growth_mul = 5):
        self.corpse_count: int = 0 
        self.grid: List[List[Tile]] = board_dim['height'] * [None]
        self.height: int = board_dim['height']
        self.width: int =  board_dim['width']
        self.herb_prop: Dict[int, int, int, int] = herb_prop
        self.carni_prop: Dict[int, int, int] = carni_prop
        self.create_board(growth_mul)
        self.add_animals()
       

    def create_board(self, growth_mul: int):
        """creates a 2-D grid of tiles with dims (self.height, self.width) and assigns it to self.grid."""
        for i in range(self.height):
            tmp_row = self.width * [None]

            for j in range(self.width):
                tmp_row[j] = Tile(contains=[], growth_mul = growth_mul)

            self.grid[i] = tmp_row

    def get_remaining_animals(self) -> Tuple[int, int]:
        """returns tuple of total sum of remaining herbivores and carnivores in our grid"""
        total_herb, total_carni = 0, 0

        for row in range(self.height):
            for col in range(self.width):
                herb, carni = self.grid[row][col].get_num_by_type_animals()

                total_herb +=  herb
                total_carni += carni

        return total_herb, total_carni

    def add_animals(self):
        """Add herbivores and carnivores to random tiles in our grid as specified by herb_prop and carni_prop"""
        y_cord = randint(0, self.height - 1)
        x_cord = randint(0, self.width - 1)
        
        for _ in range(self.herb_prop["num_herb"]):
            #create herbivores with passed user properties
            my_herb = Herbivore(self.herb_prop["cal_val"], self.herb_prop["move_cost"], self.herb_prop["meat_val"]) 
            self.grid[y_cord][x_cord].add_animal(my_herb)

        for _ in range(self.carni_prop["num_carni"]):
            my_carni = Carnivore(self.carni_prop["cal_val"], self.carni_prop["move_cost"])
            self.grid[y_cord][x_cord].add_animal(my_carni)
            

    def cycle_day(self):
        """loop over all tiles, have all plants on all tiles grow, have all animals try and eat as specified by animal type then
        move all animals some legal random distance b/w 0 and max_movement"""

        for row in range(self.height):
            for col in range(self.width): 
                cur_tile = self.grid[row][col]
                growth_rate = randint(1, 5) #generate random growth rate for this tile
                cur_tile.plant.grow(growth_rate) #First grow out plants

                self.feed_animals(cur_tile.contains, cur_tile)

                #We can't actually eat after movement b/c we can move in any direction so some animals may miss feeding time if we do
                #we would need to loop again. This is allowed but an intresting design decision. I like keeping my O(n) low so I'll flip it.
                self.move_all_animals_on_tile(cur_tile.contains, row, col) 

        self.reset_animal_movement() #make sure all our animals are allowed to move

    def reset_animal_movement(self):
        """reset movement properties of animals so that can legally move on next day"""
        for row in range(self.height):
            for col in range(self.width):
                animals = self.grid[row][col].contains

                for animal in animals:
                    animal.reset_movement()

    def move_animal(self, animal: Animal, x_cord: int, y_cord: int) -> Tuple[int, int, int]:
        """Have passed animal move some legal random distance b/w 0 and it's max distance.
        x_cord and y_cord represent animals current location used to help validate legality of animal movement.
        Returns tuple of x_dist, y_dist, total_distance to help with unit testing"""
        distance = randint(0, animal.max_move)
        x_dist = randint(-distance, distance) #we want to randomly select between going left or right

        #get y distance, need to add abs so we don't get illegal distance
        abs_y_dist = distance - abs(x_dist) 
       
        y_dist = abs_y_dist
        coin_flip = randint(0, 1) 

        #flip sign with 50% prob
        if coin_flip == 0:
            y_dist = -y_dist

        x_dist = self.validate_move(x_dist, x_cord, self.width)
        y_dist = self.validate_move(y_dist, y_cord, self.height)

        return x_dist, y_dist, distance


    def feed_animals(self, animals: List[Animal], tile: Tile):
        """have all animals in passed animals list try and eat as specified by their animal type. Tile is used to extract plant for herbivores.
        Removes any dead animals from game after feeding is complete"""
        for animal in animals:
            if type(animal) is Herbivore and animal.is_alive: #can't eat if dead
                animal.eat(tile.plant)
            else:
                bambi = self.get_first_herbivore(animals) #get first herbivore if it exists
                if bambi != None:
                    animal.eat(bambi.get_eaten()) 

        self.clean_corpses(animals)   

    def clean_corpses(self, animals: List[Animal]):
        """remove dead animals from out game and increase corpse count for each removed animal"""
        animals_copy = animals.copy() #shallow copy to prevent pass by reference errors in loop
        for animal in animals_copy:
            if not animal.is_alive:
                animals.remove(animal)  #still sketch
                self.corpse_count += 1

    def get_first_herbivore(self, animals: List[Animal]) -> Union[Herbivore, None]:
        """Find the first living herbivore in the list if it exists. Returns herbivore is it exists"""
        for animal in animals:
            if type(animal) is Herbivore and animal.is_alive:
                return animal
        
        return None

    def move_all_animals_on_tile(self, animals: List[Animal], x_cord: int, y_cord: int) -> List[Tuple[int, int, int]]:
        """Move all animals on tile x_cord, y_cord, some random distance. 
        returns list of tuple for x distance traveled, y distance traveled and total distance traveled for testing"""
        animals_copy =  animals.copy() #shallow copy to prevent pass by reference errors in loop
        distances = []
        idx = 0

        for animal in animals_copy:
            if not animal.has_moved:
                x_dist, y_dist, distance =  self.move_animal(animal, x_cord, y_cord)
                animal.move(distance)

                if distance != 0:
                    animals.remove(animal) #kinda sketch please test
                    self.grid[y_cord + y_dist][x_cord + x_dist].add_animal(animal)
                    self.clean_corpses(self.grid[y_cord + y_dist][x_cord + x_dist].contains) #remove animals that starved
        
                distances.append((x_dist, y_dist, distance, idx))
            idx += 1
        return distances
    
    def validate_move(self, move_dist: int, cur_pos: int, max_val: int) -> int:
        """Check if move is valid if not flip direction of move otherwise do nothing"""
        if cur_pos + move_dist >= max_val or cur_pos + move_dist < 0:
            return -move_dist
        return move_dist


def run_game():
    """Main method for this game. asks user for starting conditions, runs simulation and reports results"""
    height = int(input("please enter a board height: "))
    width = int(input("please enter a board width: "))

    num_herb = int(input("please enter how many herbivores you would like: "))
    herb_cal = int(input("please enter how many calories herbivores should start with: "))
    herb_move = int(input("please enter how many calories it takes a herbivore to move: "))
    herb_meat_val = int(input("please enter how many calories consuming a herbivore provides: "))

    num_carni = int(input("please enter how many carnivores you would like: "))
    carni_cal = int(input("please enter how many calories carnivores should start with: "))
    carni_move = int(input("please enter how many calories it takes a carnivore to move: "))

    days = int(input("please enter a number of days to run: "))
    growth_mul = int(input("please enter scaling value for plant growth rate: "))

    board_dim = {"height": height, "width": width}
    herb_prop = {"num_herb": num_herb, "cal_val": herb_cal, "meat_val": herb_meat_val, "move_cost": herb_move}
    carni_prop = {"num_carni": num_carni, "cal_val": carni_cal, "move_cost": carni_move}

    my_board = Board(board_dim, herb_prop, carni_prop, growth_mul)
    
    for _ in range(days):
        my_board.cycle_day()

    herbs_left, carni_left =  my_board.get_remaining_animals()
    corpses = my_board.corpse_count

    print("After {0} days we killed {1} animals and have {2} herbivores and {3} carnivores left".format(days, corpses, herbs_left, carni_left))
