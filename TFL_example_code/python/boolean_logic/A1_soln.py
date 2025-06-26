"""
Boolean Logic Intro Assignment
Covers Tier 1 (Boolean Basics) and Tier 2 (Compound Expressions)
"""

# --- Tier 1: Foundations ---

# Concept 1: Boolean Values
# Predict the output before running each line add a comment with your prediction
print("--- Boolean Values ---")
print(5 > 3)   # True -> first solution example
print(2 == 4)  # False
print("dog" != "cat") # True 
print(bool(0))   # False
print(bool("hello"))  # True
print(bool([])) # False
print(bool("")) # False



# Concept 2: Basic Boolean Operators
# Fill in a truth table manually 

True and True # True -> first solution example
True or True # True 
not True # False
True and False # False
True or False # True
not True # False
False and True # False
False or True # True
not False # True
False and False # False
False or False # False
not False # True

print("\n--- Truth Tables ---")
values = [True, False]
for a in values:
    for b in values:
        print(f"{a} AND {b} = {a and b}")
        print(f"{a} OR {b} = {a or b}")
        print(f"NOT {a} = {not a}")


# --- Tier 2: Compound Expressions ---

# Concept 3: Grouped Expressions
print("\n--- Grouped Expressions ---")
# Students should evaluate step-by-step
expr1 = (True or False) and False  # False
expr2 = not (False or False)       # True
expr3 = True and (False or True)   # True
print(f"(True or False) and False = {expr1}")
print(f"not (False or False) = {expr2}")
print(f"True and (False or True) = {expr3}")


# Concept 4: Operator Precedence
print("\n--- Operator Precedence ---")
# Show how Python resolves without parentheses
# not > and > or
expr4 = True or not False and False # True
# Step 1: not False -> True
# Step 2: True and False -> False
# Step 3: True or False -> True
print(f"True or not False and False = {expr4}")


# Predict, evaluate step-by-step, then verify:
print("\n--- Practice Section ---")
ex1 = (False and True) or True # True
ex2 = not (True and False) # True
ex3 = (not True) or (True and not False) # True
print(f"(False and True) or True = {ex1}")
print(f"not (True and False) = {ex2}")
print(f"(not True) or (True and not False) = {ex3}")



