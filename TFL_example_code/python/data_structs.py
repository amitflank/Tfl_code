"""
Python Topic: List vs Set vs Dictionary
Covers basic definitions, how to access data, how to loop through structures, and some example problems.
"""

# --- Definitions ---

# List
# Ordered, allows duplicates, indexable.
animals = ["dog", "cat", "dog"]
print("First animal in list:", animals[0])

# Set
# Unordered, unique items, fast membership checks.
unique_animals = {"dog", "cat"}
print("Is 'dog' in set?", "dog" in unique_animals)

# Dictionary
# Key-value pairs, ordered since Python 3.7, fast lookups.
animal_sounds = {
    "dog": "woof",
    "cat": "meow",
    "bird": "tweet"
}
print("Sound a dog makes:", animal_sounds["dog"])

# Checking safe lookup in dict:
print("Lion sound:", animal_sounds.get("lion", "unknown"))

# --- Looping Examples ---

# Loop over list
print("\nLooping through list:")
for animal in animals:
    print(animal)

# Loop over set
print("\nLooping through set:")
for animal in unique_animals:
    print(animal)

# Loop over dictionary keys
print("\nLooping through dictionary keys:")
for animal in animal_sounds:
    print(animal)

# Loop over dictionary values
print("\nLooping through dictionary values:")
for sound in animal_sounds.values():
    print(sound)

# Loop over dictionary items
print("\nLooping through dictionary items:")
for animal, sound in animal_sounds.items():
    print(f"{animal} goes {sound}")

print("What does the fox say?", animal_sounds.get("fox", "unknown"))

# --- Performance Note ---
print("\nPerformance Note:")
print("Lists are ordered and indexable but slower for membership checks.")
print("Sets and dictionaries are fast for membership testing.")
print("Dictionaries preserve insertion order starting from Python 3.7.")

# --- Example Problems ---

# Example 1: Remove duplicates from list
colors = ["red", "blue", "red", "green", "blue"]
unique_colors = set(colors)
print("\nUnique colors:", unique_colors)

# Example 2: Count items in list
color_counts = {}
for color in colors:
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1
print("Color counts:", color_counts)

# Example 3: Check membership
print("Is 'yellow' in colors list?", "yellow" in colors)
print("Is 'yellow' in unique_colors set?", "yellow" in unique_colors)
print("Is 'yellow' a key in color_counts dict?", "yellow" in color_counts)

# Example 4: Loop through dictionary
print("\nLooping through color_counts dict:")
for color, count in color_counts.items():
    print(f"{color} → {count}")

# Example 5: Loop through dictionary of students
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}
print("\nStudent names:")
for name in students:
    print(name)

print("\nStudent scores:")
for score in students.values():
    print(score)

print("\nStudent names and scores:")
for name, score in students.items():
    print(f"{name}: {score}")

# Mini Exercise
fruits = ["apple", "banana", "apple", "orange"]
fruit_set = set(fruits)
print("\nUnique fruits:", fruit_set)
print("Is 'pear' in the fruit set?", "pear" in fruit_set)
fruit_dict = dict.fromkeys(fruit_set, "fruit")
print("Fruit dictionary:", fruit_dict)

"""
Python Topic: List vs Set vs Dictionary
Adds timing measurements to illustrate O(n) costs for different operations.
"""

import time

# Create large data sets
large_list = list(range(30000000))
large_set = set(large_list)
large_dict = {x: x for x in large_list}

search_value = 999_999

print("\nPerformance Testing with Large Data Sets measured in seconds:")
# Measure time to check membership in list
start = time.perf_counter()
found_in_list = search_value in large_list
elapsed = time.perf_counter() - start
print("Membership test in list:", found_in_list, "Time:", f"{elapsed:.7f}")

# Measure time to check membership in set
start = time.perf_counter()
found_in_set = search_value in large_set
elapsed = time.perf_counter() - start
print("Membership test in set:", found_in_set, "Time:", f"{elapsed:.7f}")

# Measure time to check membership in dict keys
start = time.perf_counter()
found_in_dict = search_value in large_dict
elapsed = time.perf_counter() - start
print("Membership test in dict:", found_in_dict, "Time:", f"{elapsed:.7f}")

# Measure time to add element to list
start = time.perf_counter()
large_list.append(-1)
elapsed = time.perf_counter() - start
print("\nAppend to list time:", f"{elapsed:.7f}")

# Measure time to add element to set
start = time.perf_counter()
large_set.add(-1)
elapsed = time.perf_counter() - start
print("Add to set time:", f"{elapsed:.7f}")

# Measure time to add element to dict
start = time.perf_counter()
large_dict[-1] = -1
elapsed = time.perf_counter() - start
print("Add to dict time:", f"{elapsed:.7f}")

# Measure time to remove element from list
start = time.perf_counter()
large_list.remove(-1)
elapsed = time.perf_counter() - start
print("\nRemove from list time:", f"{elapsed:.7f}")

# Measure time to remove element from set
start = time.perf_counter()
large_set.remove(-1)
elapsed = time.perf_counter() - start
print("Remove from set time:", f"{elapsed:.7f}")

# Measure time to remove element from dict
start = time.perf_counter()
del large_dict[-1]
elapsed = time.perf_counter() - start
print("Remove from dict time:", f"{elapsed:.7f}")

print("\nNote:")
print("List operations like membership testing are O(n).")
print("Set and dictionary membership testing and additions/removals are approximately O(1).")
