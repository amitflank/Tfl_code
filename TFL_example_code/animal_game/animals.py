from random import randint
import re
from typing import List, Union, Tuple

from abc import ABC, abstractmethod

class Food():

    def __init__(self, food_type: str):
        self.food_type = food_type

class Plant(Food):

    def __init__(self, growth_mul: int):
        super().__init__("Plant")
        self.cal_val = 0
        self.growth_mul = growth_mul
       
    def grow(self, growth_rate: int):
        self.cal_val += self.growth_mul * growth_rate

    def grazed(self) -> int:
        g_cal = self.cal_val
        self.cal_val -= self.cal_val
        return g_cal

class Meat(Food):

    def __init__(self, cal_val:  int):
        super().__init__("Meat")
        self.cal_val = cal_val

class Animal(ABC):

    def __init__(self, move_cost: int, cal_val: int = 100, max_move: int = 3):
        self.move_cost = move_cost
        self.cal_val = cal_val
        self.max_move = max_move
        self.is_alive = True

    def move(self, distance: int):
        self.cal_val -= distance * self.move_cost

    def legal_move(self, distance: int) -> bool:
        return distance <= self.max_move
    
    @abstractmethod
    def eat(self, food: Food):
        pass
    

class Herbivore(Animal):
    def __init__(self, cal_val: int = 100, move_cost = 50, meat_val: int = 300, max_move = 3):
        super().__init__(move_cost, cal_val, max_move)
        self.meat_val = meat_val
    
    def eat(self, plant: Plant):
        self.cal_val += plant.grazed()

    def get_eaten(self):
        self.is_alive = False
        return Meat(self.meat_val)


class Carnivore(Animal):
    
    def __init__(self, cal_val: int  = 100, move_cost: int = 100, max_move = 2) -> None:
        super().__init__(move_cost, cal_val, max_move)
    
    def eat(self, food: Meat):
        self.cal_val += food.cal_val

class Tile():

    def __init__(self, contains: List[Animal], growth_mul: int) -> tuple:
        self.growth_rate: int = randint(0,9)
        self.contains: List[Animal] = contains
        self.plant: Plant = Plant(growth_mul)

    def add_animal(self, animal: Animal):
        self.contains.append(animal)

    def get_num_by_type_animals(self):
        """So for something like this we prob want so global list of legal animals for best practice but we will assume two for simple imp. 
        Just noting this is bad practice for education"""
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

    def __init__(self, height: int, width: int, growth_mul = 5, num_herb: int = 10, num_carni: int = 3):
        self.corpse_count: int = 0
        self.grid: List[List[Tile]] = height * [None]
        self.height: int = height
        self.width: int = width
        self.create_board(growth_mul)
        self.add_animals(num_herb, num_carni)

    def create_board(self, growth_mul: int):
        for i in range(self.height):
            tmp_row = self.width * [None]

            for j in range(self.width):
                tmp_row[j] = Tile(contains=[], growth_mul = growth_mul)

            self.grid[i] = tmp_row

    def add_animals(self, num_herb: int, num_carni: int):

        for _ in range(num_herb):
            y_cord = randint(0, self.height - 1)
            x_cord = randint(0, self.width - 1)

            self.grid[y_cord][x_cord].add_animal(Herbivore())

        for _ in range(num_carni):
            y_cord = randint(0, self.height - 1)
            x_cord = randint(0, self.width - 1)

            self.grid[y_cord][x_cord].add_animal(Carnivore())

            

    def cycle_day(self):
        height = self.height
        width = self.width

        for i in range(height):
            for j in range(width): 
                cur_tile = self.grid[i][j]
                growth_rate = randint(1, 5) #generate random growth rate for this tile
                cur_tile.plant.grow(growth_rate) #First grow out plants

                self.feed_animals(cur_tile.contains, cur_tile)

                #We can't actually eat after movement b/c we can move in any direction so some animals may miss feeding time if we do
                #we would need to loop again. This is allowed but an intresting design decision. I like keeping my O(n) low so I'll flip it.
                self.move_all_animals_on_tile(cur_tile.contains, i, j) 


    def move_animal(self, animal: Animal, x_cord: int, y_cord: int) -> Tuple[int, int, int]:
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


    #Currently first herbivore eats all food and first carnivore eats first herbivore which is kinda sus implementation. 
    #Not sure I'll change it but thought I would note it.
    def feed_animals(self, animals: List[Animal], tile: Tile):
        for animal in animals:
            if type(animal) is Herbivore and animal.is_alive: #can't eat if dead
                animal.eat(tile.plant)
            else:
                bambi = self.get_first_herbivore(animals) #get first herbivore if it exists
                if bambi != None:
                    animal.eat(bambi.get_eaten()) 
                    
        #clean corpses
        for animal in animals:
            if not animal.is_alive:
                animals.remove(animal)  #still sketch
                self.corpse_count += 1


    def get_first_herbivore(self, animals: List[Animal]) -> Union[Herbivore, None]:
        """Find the first living herbivore in the list if it exists. """
        for animal in animals:
            if type(animal) is Herbivore and animal.is_alive:
                return animal
        
        return None

    def move_all_animals_on_tile(self, animals: List[Animal], x_cord: int, y_cord: int):
        for animal in animals:
            x_dist, y_dist, distance =  self.move_animal(animal, x_cord, y_cord)
            animal.move(distance)

            if distance != 0:
                animals.remove(animal) #kinda sketch please test
            else:
                self.grid[y_cord + y_dist][x_cord + x_dist].append(animal)
        
    def validate_move(self, move_dist: int, cur_pos: int, max_val: int) -> int:
        """Check if move is valid if not flip direction of move otherwise do nothing"""
        if cur_pos + move_dist >= max_val or cur_pos + move_dist < 0:
            return -move_dist
        return move_dist
