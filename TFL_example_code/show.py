"""Introducing idea of classes"""
class Milk():
    
    def __init__(self):
        self.calories = 100


class Cow():

    #This is a constructor. It uses the special name __init__.
    #It's job is to setup the class when we create a new instance of it.
    def __init__(self, has_milk: bool, weight: int, gender: str): # not all cows are the same so we add some variety here
        
        #self is a special class specific keyword that references the instance of the class. You can only use this internally.
        self.has_milk = has_milk
        self.weight = weight
        self.gender = gender


    @staticmethod
    def do_something():
        print("hi")


    def get_milk(self) -> Milk: #Why can't we see milk
        if self.has_milk: #why is self complaining?
            return Milk()
        print("sorry no mily for you")



#topics loops, types, lists, conditionals, operators


#print even if number is even, otherwise print odd, repeat with list of numbers
#print fizz if divisible by 3, buzz if divisible by 5 and fizzbuzz if divisible by both
#check if a string is a palindrome
#check is a list is a palindrome 
#check if all values in a list are greater then 10
#loop until we randomly generate a number greater than 100
#get the absolute value of a number
#add next number to cumulative value if would not result in the new number being greater than 50
#swap the values of 2 variables
#raise one number to the power of another number
