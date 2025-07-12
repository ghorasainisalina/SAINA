# Creating sets
unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue", "red"}  # Duplicates are removed

print(f"Unique numbers: {unique_numbers}")
print(f"Colors: {colors}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")

# Adding to sets
colors.add("yellow")
print(f"After adding yellow: {colors}")