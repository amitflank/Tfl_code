#lets build a calculator app!
from typing import Union

def add_int(num1: int, num2: int)-> int:
    """add_int expects two arguments that are ints and returns their sum.
    If both arguments are not int's warns user and returns first value"""
 

#implement sub_int
def add_float(num1: Union[int, float], num2: Union[int, float]) -> float:
    """add_float expects two arguments that are floats and returns their sum.
    If both arguments are not float's warns user and returns first value"""
 




cur_val = 0
keep_running = 0
      
while(keep_running != 5):
    print(f"current value is {cur_val}")
    print("enter 1 for adding an int, 2 for subtracting int, 3 for adding float, 4 for subtracting float and 5 for exiting program")
    print("Warning: if int methods used while current value is a float decimals will be chopped")
    user_out = input("Enter number: ")
    keep_running = int(user_out)


