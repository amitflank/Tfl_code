#lets build a calculator app!
from typing import Union

def add_int(num1: int, num2: int)-> int:
    """add_int expects two arguments that are ints and returns their sum.
    If both arguments are not int's warns user and returns first value"""
 
    if(type(num1) is int and type(num2) is int):
        print("The sum of these numbers is {0}".format(num1 + num2))
        return num1 + num2
    else:
        print("num1 and num2 should be int please try again")
        return num1

def sub_int(num1: int, num2: int) -> int:
    if(type(num1) is int and type(num2) is int):
        return num1 - num2
    else:
        print("num1 and num2 should be int please try again")
        return num1
    

#implement sub_int
def add_float(num1: Union[int, float], num2: Union[int, float]) -> float:
    valid_num1 = type(num1) is int or type(num1) is float
    valid_num2 = type(num2) is int or type(num2) is float

    if valid_num1 and valid_num2:
        return num1 + num2
    else:
        print("num1 and num2 must by int of float")
        return num1

def sub_float(num1: Union[int, float], num2: Union[int, float]) -> float:
    valid_num1 = type(num1) is int or type(num1) is float
    valid_num2 = type(num2) is int or type(num2) is float

    if valid_num1 and valid_num2:
        return num1 - num2
    else:
        print("num1 and num2 must by int of float")
        return num1




cur_val = 0
keep_running = 0
      
while(keep_running != 5):
    print(f"current value is {cur_val}")
    print("enter 1 for adding an int, 2 for subtracting int, 3 for adding float, 4 for subtracting float and 5 for exiting program")
    print("Warning: if int methods used while current value is a float decimals will be chopped")
    user_out = input("Enter number: ")
    keep_running = int(user_out)

    if(keep_running == 1):

        user_int = input("please enter an int: ")
        cur_val = add_int(int(cur_val), int(user_int))
       
    elif(keep_running == 2):
        user_int = input("please enter an int: ")
        cur_val = sub_int(int(cur_val), int(user_int))
    
    elif(keep_running ==3):
        user_float = input("please enter an float: ")
        cur_val = add_float(cur_val, float(user_float))

    elif(keep_running == 4):
        user_float = input("please enter an float: ")
        cur_val = add_float(cur_val, float(user_float)) 
    else:
        print("please enter a valid value")


print("have a good day")


