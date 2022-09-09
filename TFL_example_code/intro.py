from random import randint

# topics loops, types, lists, conditionals, operators

#This file includes the following program's
# print even if number is even, otherwise print odd, repeat with list of numbers
# print fizz if divisible by 3, buzz if divisible by 5 and fizzbuzz if divisible by both
# check if a string is a palindrome
# check is a list is a palindrome
# check if all values in a list are greater then 10
# loop until we sum of all numbers greater than 100 with random numbers b/w 1 and 10
# get the absolute value of a number
# swap the values of 2 variables
# raise one number to the power of another number

# check if all values in a list are greater then 10
# print if number is even or odd
# % modulo operator, returns the remained of a number
num = 20
if num % 2 == 0:
    print("im even")
else:
    print("im odd")

# print if number is even or odd for each element in list
num_list = [1,2,3,4,5]
for val in num_list:
    if val % 2 == 0:
        print("im even")
    else:
        print("im odd")

# print fizz if divisible by 3, buzz if divisible by 5 and fizzbuzz if divisible by both
word = ""
if num % 3 == 0:
    word += "fizz"
if num % 5 == 0:# loop until we randomly generate a number greater than 100
    word += "buzz"
print(word)


# check if a string is a palindrome, works for list as well, shows string is just a fancy list
word = "101"
start = 0 #get first letter location
end = len(word) - 1 #get last letter location
is_pal = True

for letter in word:
    if word[start] != word[end]:
        is_pal = False
        break
    
    start = start + 1
    end = end - 1
    if start >= end:
        break



# check if all values in a list are greater then 10
my_list = [1,30, 288, 20, 11]

is_gt_ten = True

for val in my_list:
    num_gt_ten = val > 10
    is_gt_ten = is_gt_ten and num_gt_ten 

if is_gt_ten:
    print("all numbers greater then 10")
else:
    print("not all numbers greater then 10")


# loop until we randomly generate a number greater than 100

sum_num = 0

while (sum_num <= 100):
    sum_num = sum_num + randint(1,10)

print(sum_num)

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
