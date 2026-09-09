# Initial set of fruits
fruits = {"apple", "banana", "cherry"}

# Adding a single item
fruits.add("orange")
print(fruits) # Output: {'apple', 'banana', 'cherry', 'orange '}

# Adding multiple items using update()
fruits.update(["mango", "grape"])
print(fruits) # Output: {'apple', 'banana', 'cherry', 'orange', 'mango', 'grape '}

# Removing an item
fruits.remove("banana")
print(fruits) # Output: {'apple', 'cherry', 'orange', 'mango', 'grape '}

# Discarding an item (no error if the item doesn't exist)
fruits.discard("pineapple")
print(fruits) # Output: {'apple', 'cherry', 'orange', 'mango', 'grape '} (no error raised)
#
# Removing and returning an arbitrary item
removed_item = fruits.pop()
print(removed_item) # Output: (varies , since pop removes an arbitrary item)
print(fruits) # Output: (remaining items after pop)

 # Clearing the set
fruits.clear()
print(fruits) # Output: set() (empty set)