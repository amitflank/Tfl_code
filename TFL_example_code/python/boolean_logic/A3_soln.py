"""
Boolean Logic - Python Built-in Constructs
Description and examples for in, any, all, and is operators.
"""

# --- Using 'in' ---
animals = ["dog", "cat", "mouse"]
print("Is 'cat' in animals?", "cat" in animals)          # True
print("Is 'dragon' in animals?", "dragon" in animals)   # True

test_str = "hello world"
print(f"Is 'hello' in {test_str}?", "hello" in test_str)    # True
print(f"Is 'goodbye' NOT in {test_str}?", "goodbye" not in test_str)  # True

# --- Using 'any' ---
errors = ["", None]
print("Is any item in errors truthy?", any(errors)) # False

warnings = []
print("Are all items in warnings falsey?", not any(warnings)) # True

# --- Using 'all' ---
fields = ["Alice", "Smith", "alice@example.com"]
print("Are all fields non-empty?", all(fields)) # True

scores = [75, 82, 90, 68]
all_scores_gt_70 = all(value > 70 for value in scores) # Using a generator expression

print("Are all scores above 70?",  all_scores_gt_70)  # False

# --- Using 'is' ---
x = None
print("Is x None?", x is None) # True

a = [1, 2]
b = [1, 2]
print("Are lists a and b equal?", a == b)# True (values equal)
print("Are lists a and b the same object?", a is b) # False (different objects)

value = "hello"
print("Is value NOT None?", value is not None) # True
