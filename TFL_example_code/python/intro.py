from random import randint

# Topics covered: loops, types, lists, conditionals, operators

# This file includes the following programs:
    # Print "even" if number is even, otherwise print "odd", repeat with a list of numbers
    # Print "fizz" if divisible by 3, "buzz" if divisible by 5, and "fizzbuzz" if divisible by both
    # Check if a string is a palindrome
    # Check if a list is a palindrome
    # Check if all values in a list are greater than 10
    # Loop over randomly generated addends until we get a sum greater than 100
    # Get the absolute value of a number
    # Swap the values of 2 variables
    # Raise one number to the power of another number
    # Bonus project: try to re-write all these as methods

# Print "even" if a number is even, "odd" if it's odd
# Use the modulo operator (%) which returns the remainder of a number
num = 20
if num % 2 == 0:
    print("I'm even")
else:
    print("I'm odd")

# Repeat this process for each element in a list of numbers
num_list = [1,2,3,4,5]
for val in num_list:
    if val % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")

# Print "fizz" if divisible by 3, "buzz" if divisible by 5, and "fizzbuzz" if divisible by both
word = ""
if num % 3 == 0:
    word += "fizz"
if num % 5 == 0:
    word += "buzz"
print(word)

# Check to see if a string is a palindrome
# This works for lists as well, because a string is just a list of characters
word = "101"
start = 0               # Find the item at index 0
end = len(word) - 1     # Find the last item
is_pal = True           # Assume "True" by default

for letter in word:
    if word[start] != word[end]:
        is_pal = False
        break
    start = start + 1
    end = end - 1
    if start >= end:
        break

'''

# check if all values in a list are greater than 10
my_list = [1,30, 288, 20, 11]

is_gt_ten = True

for val in my_list:
    num_gt_ten = val > 10
    is_gt_ten = is_gt_ten and num_gt_ten 

if is_gt_ten:
    print("all numbers greater than 10")
else:
    print("not all numbers greater than 10")


# loop until we randomly generate a number greater than 100
sum_num = 0

while (sum_num <= 100):
    sum_num = sum_num + randint(1,10)

print(sum_num)

#get absolute value
num = -6

if num < 0:
    abs_num = num * -1
else:
    abs_num = num

print("the absolute value of {0} is {1}".format(num, abs_num))

#swap 2 numbers
a = 20
b= 10
c = b
b = a
a = c
print(a,b)

# raise one number to the power of another number
val = 2
power = 4
raised_val = 1

for i in range(power):
    raised_val *= val

print(raised_val)

'''