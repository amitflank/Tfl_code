"""
Boolean Logic Intro Assignment
Covers Tier 1 (Boolean Basics) and Tier 2 (Compound Expressions)
"""

# --- Tier 1: Foundations ---

# Concept 1: Boolean Values
# Predict the output before running each line add a comment with your prediction
print("--- Boolean Values ---")
print(5 > 3)   # True 
print(2 == 4)   
print("dog" != "cat")  
print(bool(0))  
print(bool("hello"))  
print(bool([])) 
print(bool("")) 


# Concept 2: Basic Boolean Operators
# Fill in a truth table manually 
print("\n--- Truth Tables ---")
#preidct the output of each line
True and True # True -> first solution example
True or True 
not True 
True and False 
True or False 
not True
False and True 
False or True 
not False 
False and False 
False or False 
not False

#This will display the solutions to the above boolean expressions
values = [True, False]
for a in values:
    for b in values:
        print(f"{a} AND {b} = {a and b}")
        print(f"{a} OR {b} = {a or b}")
        print(f"NOT {a} = {not a}")


# Concept 3: Grouped Expressions
print("\n--- Grouped Expressions ---")
# Students should predict the result of expressions below then check thier work by running the script
expr1 = (True or False) and False  
expr2 = not (False or False)      
expr3 = True and (False or True)
print(f"(True or False) and False = {expr1}")
print(f"not (False or False) = {expr2}")
print(f"True and (False or True) = {expr3}")


# Concept 4: Operator Precedence
print("\n--- Operator Precedence ---")
# Show how Python resolves without parentheses
# not > and > or
expr4 = True or not False and False
print(f"True or not False and False = {expr4}")


# Predict, predict each experssion, then verify:
print("\n--- Practice Section ---")
ex1 = (False and True) or True
ex2 = not (True and False)
ex3 = (not True) or (True and not False)
print(f"(False and True) or True = {ex1}")
print(f"not (True and False) = {ex2}")
print(f"(not True) or (True and not False) = {ex3}")



