
"""
class Food():
    def __init__(self, food_type: str):

class Plant(Food):

    def __init__(self, growth_mul: int):
        assign food_type to plant using super
        set self.cal to 0
        assign class property growth mul

    def grow(self, growth_rate: int):
        set plant calories to existing calories plus growth_mul times growth rate


    def grazed(self) -> int:
        sets plants calories to zero 
        returns number of calories in plant

class Meat(Food):

    def __init__(self, food_type: str, cal:  int):
        assign food_type to Meat
        assign cal to class property


class Animal(ABC):

    def __init__(self, move_cost: int, cal_val: int = 100, max_move: int = 3):
        assign args to class properties
        assign is_alive class property to True

    def move(self, distance: int):
        adjust animal remaning calories by distance times move_cost


    def legal_move(self, distance: int) -> bool:
        return if we moved a legal distance for this animal
    
    @abstractmethod
    def eat(self, food: Food):
        abstract methods

    
class Herbivore(Animal):
    def __init__(self, cal_val: int = 500, move_cost = 50, meat_val: int = 300, max_move = 3):
        use super to assign all class properties except for meat_val
        assign meat_val as class property
    
    def eat(self, plant: Plant):
        use plant grazed method to increase animals calories

    def get_eaten(self) -> Meat:
        adjust is alive property
        return appropriate meat object

class Carnivore(Animal):
    
    def __init__(self, cal_val: int  = 100, move_cost: int = 100, max_move = 2) -> None:
        #use super to assign all arguments to class properties
    
    def eat(self, food: Meat):
        use food to adjust animals calories

class Tile():

    def __init__(self, contains: List[Animal], growth_mul: int):
        assign property growth_rate to random int b/w 0 and 9 inclusive
        assign property contains
        assign property class to be a plant with growth_mul

    def add_animal(self, animal: Animal):
        add passed animals end of property contains

    def get_num_by_type_animals(self):
        return a list containing number of herbivores and number of carnivores

            
class Board():

    def __init__(self, height: int, width: int, growth_mul = 5, num_herb: int = 10, num_carni: int = 3):
        self.corpse_count: int = 0
        self.grid: List[List[Tile]] = height * [None]
        self.height: int = height
        self.width: int = width
        self.create_board(growth_mul)
        self.add_animals(num_herb, num_carni)

    def create_board(self, growth_mul: int):
        #creates board of tiles self.height by self.width

    def add_animals(self, num_herb: int, num_carni: int):
    randomly 

    def cycle_day(self):
    

    def reset_animal_movement(self):
       

    def move_animal(self, animal: Animal, x_cord: int, y_cord: int) -> Tuple[int, int, int]:
       

    #Currently first herbivore eats all food and first carnivore eats first herbivore which is kinda sus implementation. 
    #Not sure I'll change it but thought I would note it.
    def feed_animals(self, animals: List[Animal], tile: Tile):
       

    def get_first_herbivore(self, animals: List[Animal]) -> Union[Herbivore, None]:
        Find the first living herbivore in the list if it exists.
 
    def move_all_animals_on_tile(self, animals: List[Animal], x_cord: int, y_cord: int) -> List[Tuple[int, int, int]]:
        Move all animals on tile x_cord, y_cord, some random distance. 
        returns list of tuple for x distance traveled, y distance traveled and total distance traveled for testing

    def validate_move(self, move_dist: int, cur_pos: int, max_val: int) -> int:
       Check if move is valid if not flip direction of move otherwise do nothing
      
#change contains to animals

"""