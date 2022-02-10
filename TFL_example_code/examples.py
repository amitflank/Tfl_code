def add_int(num1: int, num2: int)-> int:
    pass

a = 10
a = a +5

#shallow copy
old_list = [1,2,3]
copied_list = old_list[:]

print(a)
num_loops = 5
for _ in range(num_loops):
    print("hi")


player_input = input("hi")
dir_dict = {"North": possible_movement[0], "South": possible_movement[1]}

try:
    end_location = dir_dict[player_input]
except KeyError:
    print("Enter a valid direction")
    return fxn_name(input_val)

