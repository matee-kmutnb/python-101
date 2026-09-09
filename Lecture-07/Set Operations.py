set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1.intersection(set2)) # Output: {3}

# Difference
print(set1.difference(set2)) # Output: {1, 2}

# Symmetric Difference
print(set1.symmetric_difference(set2)) # Output: {1, 2, 4, 5}